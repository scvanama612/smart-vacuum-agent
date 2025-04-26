import tkinter as tk
from agent import VacuumAgent
from room import Room
import time

CELL_SIZE = 50
ROWS, COLS = 6, 6

def update_gui(canvas, room, agent):
    canvas.delete("all")
    for r in range(ROWS):
        for c in range(COLS):
            x1, y1 = c * CELL_SIZE, r * CELL_SIZE
            x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE
            state = room.grid[r][c]
            color = {
                'clean': 'white',
                'dirty': 'sienna',
                'wall': 'black'
            }.get(state, 'white')
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")

    ar, ac = agent.position
    x1, y1 = ac * CELL_SIZE, ar * CELL_SIZE
    x2, y2 = x1 + CELL_SIZE, y1 + CELL_SIZE
    canvas.create_oval(x1+5, y1+5, x2-5, y2-5, fill="skyblue")

def run_simulation():
    while room.has_dirt():
        update_gui(canvas, room, agent)
        canvas.update()
        time.sleep(0.5)
        agent.act(room)
    update_gui(canvas, room, agent)
    canvas.update()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Smart Vacuum Cleaner Agent")

    canvas = tk.Canvas(root, width=COLS * CELL_SIZE, height=ROWS * CELL_SIZE)
    canvas.pack()

    room = Room(ROWS, COLS)
    agent = VacuumAgent(room.start_pos)

    root.after(1000, run_simulation)
    root.mainloop()
