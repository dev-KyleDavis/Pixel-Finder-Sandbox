import pyautogui
import tkinter as tk

class PixeFinder:
    def __init__(self, master):
        self.master = master
        master.title("Pixie Finder")
        master.geometry("300x400")  # Set the starting size of the window
        master.minsize(400, 300)

        # Set the size of the canvas with a bottom margin
        margin = 50
        self.canvas = tk.Canvas(master, bg="white", highlightthickness=0, height=pyautogui.size()[1] - margin)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Bind the <Configure> event to the canvas and update the canvas size
        self.canvas.bind("<Configure>", self.update_canvas_size)
        self.update_canvas_size(None)

        # Bind mouse events to the canvas
        self.canvas.bind("<ButtonPress-1>", self.start_selection)
        self.canvas.bind("<B1-Motion>", self.update_selection)
        self.canvas.bind("<ButtonRelease-1>", self.stop_selection)

        # Create the label for displaying the pixel size of the selected area
        self.label = tk.Label(master, text="")
        self.label.pack()

        # Create the crosshair
        self.crosshair = self.canvas.create_line(0, 0, 0, 0, fill="red", width=1, state=tk.NORMAL)\
        



        # Set the minimum selection box size
        self.min_width, self.min_height = 10, 10

    def update_canvas_size(self, event):
        self.canvas.config(width=self.master.winfo_width(), height=self.master.winfo_height())

    def start_selection(self, event):


        #delete the previous selection box and pixel size label
        self.canvas.delete("selection_box")
        self.canvas.delete("pixel_size_label")

        # Reset the label for displaying the pixel size of the selected area
        self.label.config(text="")

        # Disable events for other windows
        self.master.grab_set()

        # Clear the previous selection box and update the start position
        self.canvas.delete("selection_box")
        self.start_x, self.start_y = event.x, event.y

        # Update the crosshair
        self.update_crosshair(event)

    def update_selection(self, event):

        # Calculate the width and height of the selection box
        width, height = event.x - self.start_x, event.y - self.start_y

        
        # Snap the selection box to whole numbers
        self.start_x = round(self.start_x)
        self.start_y = round(self.start_y)
        width = round(width)
        height = round(height)

        # Check if the selection box is smaller than the minimum size
        if abs(width) < self.min_width or abs(height) < self.min_height:
            # If the selection box is too small, set the width and height to the minimum size and adjust the start position
            width = max(self.min_width, abs(width)) * (1 if width >= 0 else -1)
            height = max(self.min_height, abs(height)) * (1 if height >= 0 else -1)
            event.x, event.y = self.start_x + width, self.start_y + height

        # Update the label with the pixel size of the selection box
        self.label.config(text=f"{abs(width)} x {abs(height)}")

        # Clear the previous selection box and draw a new one based on the current position
        self.canvas.delete("selection_box")

        #pizel size label in black text
        self.canvas.itemconfig("pixel_size_label", fill="black")

        self.label.config(text="") # Clear the label for displaying the pixel size of the selected area

        self.canvas.create_rectangle(self.start_x, self.start_y, event.x, event.y, outline="black", tags="selection_box", stipple="gray12")
        

    
        # Update the crosshair
        self.update_crosshair(event)


    def stop_selection(self, event):
        # Get the coordinates of the selection box and calculate the pixel size
        x1, y1, x2, y2 = self.canvas.coords("selection_box")
        width, height = x2 - x1, y2 - y1
        pixel_size = width * height

        # Create a persistent selection box on the canvas
        self.canvas.create_rectangle(x1, y1, x2, y2, outline="red", width=2, tags="selection_box")

        # Add a label for displaying the pixel size of the selected area
        label_x = (x1 + x2) / 2
        label_y = y1 - 20
        label_text = f"{width} x {height}"
        self.canvas.create_text(label_x, label_y, text=label_text, fill="red", tags="pixel_size_label")

        #make the slelection box lines thicker
        self.canvas.itemconfig("selection_box", width=2)


        # Enable events for other windows
        self.master.grab_release()

    def update_crosshair(self, event):
        # Update the crosshair based on the current mouse position
        x, y = event.x, event.y
        self.canvas.coords("crosshair", x, 0, x, pyautogui.size()[1])
        self.canvas.coords("crosshair", 0, y, pyautogui.size()[0], y)

        #show the crosshair if it is hidden
        self.canvas.itemconfig("crosshair", state="normal")

        #show pixel size label if it is hidden
        self.canvas.itemconfig("pixel_size_label", state="normal")

    def run(self):
        # Start the GUI event loop
        self.master.mainloop()

# Create the GUI window and start the event loop
root = tk.Tk()
snipping_tool = PixeFinder(root)
root.attributes("-topmost", True)  # Keep the Snipping Tool on top of other windows
snipping_tool.run()
