# Pixel-Finder-Sandbox
Pixel Finder Sandbox using python

This Python code creates a GUI application called "Pixie Finder" that allows the user to select an area on the screen and displays the pixel size of the selection.

The GUI is created using the tkinter library, and the screen capturing and pixel counting functionality is provided by the pyautogui library.

The main class is called "PixeFinder", and its constructor sets up the GUI window with a canvas where the user can make their selection. The canvas is sized to match the size of the screen, with a small margin at the bottom.

The class has three methods for handling the selection: start_selection(), update_selection(), and stop_selection(). When the user clicks the mouse, start_selection() is called, which clears any previous selection and updates the crosshair cursor. As the user drags the mouse, update_selection() is called, which updates the selection box and the pixel size label. When the user releases the mouse button, stop_selection() is called, which creates a persistent selection box and pixel size label.

Finally, the main method creates the GUI window and runs the event loop using the "run()" method of the PixeFinder class.
