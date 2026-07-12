import tkinter as tk
import math
import random
from datetime import datetime

class ParadoxClock:
    def __init__(self, root):
        self.root = root
        self.root.title("The Time-Inversion Engine")
        self.canvas = tk.Canvas(root, bg="#0b0c10", width=600, height=600)
        self.canvas.pack()
        
        self.angle = 0
        self.phrases = [
            "Gathering yesterday's starlight...",
            "Unwinding the mainspring of tomorrow...",
            "Measuring the weight of forgotten echoes...",
            "Subtracting seconds from the horizon...",
            "Listening to the shadows stretch...",
            "Counting the breaths between heartbeats..."
        ]
        self.current_phrase = self.phrases[0]
        self.update_clock()

    def draw_quantum_ticks(self):
        """Draws dynamic, floating geometric calibrations around the dial."""
        for i in range(12):
            ang = i * (2 * math.pi / 12) + (self.angle * 0.05)
            x1 = 300 + 180 * math.cos(ang)
            y1 = 300 + 180 * math.sin(ang)
            x2 = 300 + 200 * math.cos(ang)
            y2 = 300 + 200 * math.sin(ang)
            self.canvas.create_line(x1, y1, x2, y2, fill="#45f3ff", width=2, tags="clock_face")

    def update_clock(self):
        self.canvas.delete("all")
        self.angle -= 0.04 # Inverted physics: hands move backwards
        
        # Draw elegant, glowing concentric backing rings
        self.canvas.create_oval(100, 100, 500, 500, outline="#1f2833", width=4)
        self.canvas.create_oval(80, 80, 520, 520, outline="#c5a880", width=1, dash=(5, 5))
        self.draw_quantum_ticks()
        
        # Calculate dynamic inverted vector hands
        hx = 300 + 140 * math.cos(self.angle)
        hy = 300 + 140 * math.sin(self.angle)
        mx = 300 + 160 * math.cos(self.angle * 0.5)
        my = 300 + 160 * math.sin(self.angle * 0.5)
        
        # Render vector structural beams
        self.canvas.create_line(300, 300, hx, hy, fill="#fc4445", width=4, arrow=tk.LAST, tags="hands")
        self.canvas.create_line(300, 300, mx, my, fill="#66fcf1", width=2, arrow=tk.LAST, tags="hands")
        self.canvas.create_oval(292, 292, 308, 308, fill="#ffffff")
        
        # Change the dream status text periodically
        if random.random() < 0.02:
            self.current_phrase = random.choice(self.phrases)
            
        # HUD readout text display
        self.canvas.create_text(300, 430, text=self.current_phrase, fill="#95a5a6", font=("Courier", 10, "italic"))
        self.canvas.create_text(300, 150, text="INVERTED PERSPECTIVE MATRIX", fill="#c5a880", font=("Courier", 11, "bold"))
        
        self.root.after(30, self.update_clock)

if __name__ == "__main__":
    window = tk.Tk()
    app = ParadoxClock(window)
    window.mainloop()
