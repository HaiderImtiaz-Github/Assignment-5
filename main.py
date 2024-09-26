from tkinter import *
import time

# Function to start the typing test
def start_test():
    global start_time
    entry.config(state=NORMAL)  # Enable the entry box for typing
    entry.delete(0, END)  # Clear the entry field for user to type
    result_label.config(text="")  # Clear the result label
    start_button.config(state=DISABLED)  # Disable Start button
    end_button.config(state=NORMAL)  # Enable End button
    start_time = time.time()  # Record the start time

# Function to end the test and calculate typing speed
def end_test():
    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time
    typed_text = entry.get()
    word_count = len(typed_text.split())  # Count the words typed
    wpm = round((word_count / elapsed_time) * 60)  # Calculate words per minute
    entry.config(state=DISABLED)  # Disable the entry box after test

    # Determine if the user is above or below average typing speed
    if wpm >= 40:
        result_text = f"Great! Your typing speed is {wpm} WPM (above average)."
    else:
        result_text = f"Your typing speed is {wpm} WPM (below average)."
    
    result_label.config(text=result_text)
    start_button.config(state=NORMAL)  # Enable Start button
    end_button.config(state=DISABLED)  # Disable End button

# Initialize the Tkinter window
window = Tk()
window.title("Typing Speed Test")
window.minsize(600, 400)
window.config(bg="#2c2f33")  # Dark grey background

# Frame for the sample text
sample_frame = Frame(window, bg="#2c2f33")  # Dark grey background
sample_frame.pack(pady=20)

# Sample text for typing
sample_text = "The quick brown fox jumps over the lazy dog. Practice makes perfect."
sample_label = Label(sample_frame, text=sample_text, wraplength=500, font=("Helvetica", 16), bg="#2c2f33", fg="#ffffff")  # White text
sample_label.pack()

# Frame for the typing entry and buttons
input_frame = Frame(window, bg="#2c2f33")
input_frame.pack(pady=20)

# Entry box for typing the text
entry = Entry(input_frame, width=80, font=("Helvetica", 14), state=DISABLED, bg="#23272a", fg="#ffffff", insertbackground="white")  # Darker entry box with white text
entry.pack(pady=10)

# Result label to display WPM and performance feedback
result_label = Label(window, text="", font=("Helvetica", 14), bg="#2c2f33", fg="#ffffff")  # White text
result_label.pack(pady=10)

# Frame for the control buttons
button_frame = Frame(window, bg="#2c2f33")
button_frame.pack(pady=20)

# Buttons to start and end the test
start_button = Button(button_frame, text="Start", command=start_test, font=("Helvetica", 14), bg="#7289da", fg="white", padx=10, pady=5)  # Light blue button
start_button.pack(side=LEFT, padx=10)

end_button = Button(button_frame, text="End", command=end_test, font=("Helvetica", 14), bg="#f04747", fg="white", padx=10, pady=5, state=DISABLED)  # Red button
end_button.pack(side=RIGHT, padx=10)

# Instructions for the user
instructions_label = Label(window, text="Instructions: Click 'Start' to begin, and 'End' to stop the test.", font=("Helvetica", 12), bg="#2c2f33", fg="#999999")  # Light grey instructions
instructions_label.pack(pady=10)

# Run the Tkinter event loop
window.mainloop()
