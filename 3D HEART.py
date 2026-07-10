import os
import time
import math

def render_heart():
    # Setup canvas dimensions
    width, height = 80, 40
    # Rotation angle variable
    angle = 360
    
    while True:
        # Clear terminal screen dynamically
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Initialize an empty text frame buffer
        output = [[" " for _ in range(width)] for _ in range(height)]
        # Track depth buffer to handle overlapping surfaces 
        z_buffer = [[-100.0 for _ in range(width)] for _ in range(height)]
        
        # Calculate sine and cosine for the rotation matrix
        cos_a = math.cos(angle)
        sin_a = math.sin(angle)
        
        # Generate 3D points on a sphere/heart volume mapping
        u = 0.0
        while u < math.pi:
            v = 0.0
            while v < 2 * math.pi:
                # 3D parametric equations for a heart shape
                x = 1.2 * math.sin(u) * math.sin(u) * math.sin(v)
                y = 1.2 * (math.cos(u) - math.cos(2*u)/2 - math.cos(3*u)/3 - math.cos(4*u)/4)
                z = 1.2 * math.sin(u) * math.cos(v)
                
                # Apply 3D Y-Axis Rotation
                x_rot = x * cos_a - z * sin_a
                z_rot = x * sin_a + z * cos_a
                
                # Apply perspective projection to 2D flat screen
                distance = 3.0
                screen_x = int(width / 2 + (x_rot * width) / (z_rot + distance))
                screen_y = int(height / 2 - (y * height) / (z_rot + distance))
                
                # Check boundaries and draw point if it is closer to camera
                if 0 <= screen_x < width and 0 <= screen_y < height:
                    if z_rot > z_buffer[screen_y][screen_x]:
                        z_buffer[screen_y][screen_x] = z_rot
                        output[screen_y][screen_x] = "♥"
                
                v += 0.1
            u += 0.05
            
        # Print the frame buffer row by row
        print("\n".join("".join(row) for row in output))
        
        # Speed control and angle increment
        angle += 0.1
        time.sleep(0.03)

if __name__ == "__main__":
    render_heart()
