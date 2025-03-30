# graphics.py
from tkinter import *

class CustomCanvas: 
    def __init__(self, width, height):
        self.window = Tk()
        self.window.title("Canvas App")
        self.canvas = Canvas(self.window, width=width, height=height)  # This is tkinter's Canvas
        self.canvas.pack()
        self.mouse_x = 0
        self.mouse_y = 0
        self.click_x = None
        self.click_y = None
        self.window.bind("<Motion>", self.mouse_move)
        self.window.bind("<Button-1>", self.mouse_click)

    def mouse_move(self, event):
        self.mouse_x = event.x
        self.mouse_y = event.y

    def mouse_click(self, event):
        self.click_x = event.x
        self.click_y = event.y

    def get_mouse_x(self):
        return self.mouse_x

    def get_mouse_y(self):
        return self.mouse_y

    def get_last_click(self):
        while self.click_x is None or self.click_y is None:
            self.window.update()
        x, y = self.click_x, self.click_y
        self.click_x, self.click_y = None, None
        return x, y

    def wait_for_click(self):
        while self.click_x is None or self.click_y is None:
            self.window.update()

    def create_rectangle(self, x1, y1, x2, y2, color):
        return self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline='black')

    def set_color(self, obj, color):
        self.canvas.itemconfig(obj, fill=color)

    def find_overlapping(self, x1, y1, x2, y2):
        return self.canvas.find_overlapping(x1, y1, x2, y2)

    def moveto(self, obj, x, y):
        coords = self.canvas.coords(obj)
        dx = x - coords[0]
        dy = y - coords[1]
        self.canvas.move(obj, dx, dy)

    def update(self):
        self.window.update()

