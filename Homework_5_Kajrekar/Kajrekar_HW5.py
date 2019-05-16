# Name: Nikhil Kajrekar
# ID:1001552488

# This program calculates the hypotenuse of a right triangle after the user enters the lengths of two short sides.
# The result is displayed in a disabled input box on the main window.

import tkinter
import math

class CalculateHypotenuseGUI:
    def __init__(self):
        # Create the main window.
        self.main_window = tkinter.Tk()
        self.main_window.title("Right Triangle Calculator")
        # Create four frames to group widgets.
        self.top_frame = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()
        self.button_frame = tkinter.Frame()

        # Create the widgets for the top frame.
        self.side_a = tkinter.Label(self.top_frame, text='Side A:')
        self.side_a_entry = tkinter.Entry(self.top_frame, width=30)

        # Pack the top frame's widgets.
        self.side_a.pack(side='left')
        self.side_a_entry.pack(side='left')

        # Create the widgets for the middle frame.
        self.side_b = tkinter.Label(self.mid_frame, text='Side B:')
        self.side_b_entry = tkinter.Entry(self.mid_frame, width=30)

        # Pack the middle frame's widgets.
        self.side_b.pack(side='left')
        self.side_b_entry.pack(side='left')

        # Create the widgets for the bottom frame.
        self.side_c_label = tkinter.Label(self.bottom_frame, text='Side C:')
        self.side_c_entry = tkinter.Entry(self.bottom_frame, width=30, state="readonly")
        # We need a StringVar object to associate with
        # an output label. Use the object's set method
        # to store a string of blank characters.
        self.side_c_value = tkinter.StringVar()

        # Create a label and associate it with the
        # StringVar object. Any value stored in the
        # StringVar object will automatically be displayed
        # in the label.
        self.side_c_entry = tkinter.Entry(self.bottom_frame, width=30, textvariable=self.side_c_value, state="readonly")

        # Pack the bottom frame's widgets.
        self.side_c_label.pack(side='left')
        self.side_c_entry.pack(side='left')

        # Create the button widgets for the button frame.
        self.calc_button = tkinter.Button(self.button_frame, width=20, text='Calculate', command=self.calculate)
        self.quit_button = tkinter.Button(self.button_frame, width=20, text='Exit', command=self.main_window.destroy)

        # Pack the buttons.
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the frames.
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()
        self.button_frame.pack()

        # Enter the tkinter main loop.
        tkinter.mainloop()

    # The calculate method is a callback function for
    # the Calculate button.

    def calculate(self):
        sidea = float(self.side_a_entry.get())
        sideb = float(self.side_b_entry.get())

        # Calculate hypotenuse and round to 3 decimal places.
        sidec = round(math.sqrt(sidea*sidea + sideb*sideb),3)

        # Convert sidec to a string and store it
        # in the StringVar object. This will automatically
        # update the side_c_label widget.
        self.side_c_value.set(sidec)


# Create an instance of the CalculateHypotenuseGUI class.
calculate_hypotenuse = CalculateHypotenuseGUI()