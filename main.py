from tkinter import *
from tkinter import ttk

window = Tk()
window.title('Dangerous App')

counter = 0
timer_running = False


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    number = spinbox.get()
    seconds = int(number)
    old_text = entry1.get('1.0', '1000.0')
    count_down(seconds, old_text)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count, text):
    if count > 0:
        global tracker
        tracker = window.after(1000, count_down, count - 1, text)
    else:
        new_text = entry1.get('1.0', '1000.0')
        if text == new_text:
            entry1.delete('1.0', '1000.0')
        start_timer()


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(tracker)

# Create a custom style for the button with rounded edges
style = ttk.Style()
style.configure("Button1.TButton", borderwidth=0, bordercolor="black", relief="flat", foreground="green",
                background="green", padding=6, focuscolor="none")
style.map("Button1.TButton", foreground=[('pressed', 'red'), ('active', 'green')],
          background=[('pressed', '!disabled', 'darkblue'), ('active', 'green')])
new = ttk.Style()
new.configure("Button2.TButton", borderwidth=0, bordercolor="black", relief="flat", foreground="red", background="red",
              padding=6, focuscolor="none")
new.map("Button2.TButton", foreground=[('pressed', 'green'), ('active', 'red')],
        background=[('pressed', '!disabled', 'darkblue'), ('active', 'red')])

# Create Canvas
canvas1 = Canvas(window, width=1000, height=900, relief='raised')
canvas1.pack()

text = Label(window, text="Dangerous Writing App")
text.config(font=('helvetica', 25))
canvas1.create_window(500, 100, window=text)

text2 = Label(window, text="Set disappearing text max time: ")
text2.config(font=('helvetica', 15, "normal"))
canvas1.create_window(430, 150, window=text2)

text3 = Label(window, text="seconds")
text3.config(font=('helvetica', 15, "normal"))
canvas1.create_window(670, 150, window=text3)

entry1 = Text(window)
entry1.config(width=100, height=20)
canvas1.create_window(500, 350, window=entry1)

spinbox = Spinbox(window, from_=1, to=5, width=5)
canvas1.create_window(600, 150, window=spinbox)

button = ttk.Button(window, text="Start Timer", style="Button1.TButton", command=start_timer)
canvas1.create_window(300, 550, window=button)

button2 = ttk.Button(window, text="Stop Timer", style="Button2.TButton",command=reset_timer)
canvas1.create_window(700, 550, window=button2)

window.mainloop()
