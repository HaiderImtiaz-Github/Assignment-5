from tkinter import *
import time

# Function to start the typing test
def start_test():
    global start_time
    entry.config(state=NORMAL)  # Enable the entry box for typing
    entry.delete(0, END)  # Clear the entry field for user to type
    result_label.config(text="")  # Clear the result label
    start_time = time.time()  # Record the start time

# Function to end the test and calculate typing speed
def end_test():
    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time
    typed_text = entry.get()
    word_count = len(typed_text.split())  # Count the words typed
    wpm = round((word_count / elapsed_time) * 60) # Calculate words per minute
    entry.config(state=DISABLED)  # Disable the entry box after test

    # Determine if the user is above or below average typing speed
    if wpm >= 40:
        result_text = f"Great! Your typing speed is {wpm} WPM (above average)."
    else:
        result_text = f"Your typing speed is {wpm} WPM (below average)."
    
    result_label.config(text=result_text)

# Initialize the Tkinter window
window = Tk()
window.title("Typing Speed Test")
window.minsize(600, 400)

# Sample text for typing
sample_text = "The quick brown fox jumps over the lazy dog. Practice makes perfect."

# Display the sample text in a label
sample_label = Label(window, text=sample_text, wraplength=500, font=("Arial", 14), pady=10)
sample_label.pack()

# Entry box for typing the text
entry = Entry(window, width=80, font=("Arial", 14))
entry.pack(pady=20)
entry.config(state=DISABLED)  # Disable the entry until the test starts

# Result label to display WPM and performance feedback
result_label = Label(window, text="", font=("Arial", 14))
result_label.pack()

# Buttons to start and end the test
start_button = Button(window, text="Start", command=start_test, font=("Arial", 14))
start_button.pack(side=LEFT, padx=20, pady=20)

end_button = Button(window, text="End", command=end_test, font=("Arial", 14))
end_button.pack(side=RIGHT, padx=20, pady=20)

# Run the Tkinter event loop
window.mainloop()
