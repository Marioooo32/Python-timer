# This program was made by Mario idk if i will publish it =)



import tkinter as tk
from tkinter import ttk, messagebox
import winsound  # For Windows sound support
# import pygame  # Uncomment this line if you want cross-platform sound support

class CountdownTimer:
    def __init__(self, master):
        self.master = master
        self.master.title("Countdown Timer")

        # Hide the main window temporarily
        self.master.withdraw()

        self.notebook = ttk.Notebook(master)

        self.hours_frame = ttk.Frame(self.notebook)
        self.minutes_frame = ttk.Frame(self.notebook)
        self.seconds_frame = ttk.Frame(self.notebook)

        self.notebook.add(self.hours_frame, text="Hours")
        self.notebook.add(self.minutes_frame, text="Minutes")
        self.notebook.add(self.seconds_frame, text="Seconds")

        self.notebook.pack(pady=10)

        self.hours_var = tk.StringVar(value="0")
        self.minutes_var = tk.StringVar(value="0")
        self.seconds_var = tk.StringVar(value="0")

        self.hours_label = tk.Label(self.hours_frame, text="Hours", font=("Helvetica", 14))
        self.minutes_label = tk.Label(self.minutes_frame, text="Minutes", font=("Helvetica", 14))
        self.seconds_label = tk.Label(self.seconds_frame, text="Seconds", font=("Helvetica", 14))

        self.hours_label.pack(pady=5)
        self.minutes_label.pack(pady=5)
        self.seconds_label.pack(pady=5)

        self.hours_entry = ttk.Entry(self.hours_frame, textvariable=self.hours_var, font=("Helvetica", 14))
        self.minutes_entry = ttk.Entry(self.minutes_frame, textvariable=self.minutes_var, font=("Helvetica", 14))
        self.seconds_entry = ttk.Entry(self.seconds_frame, textvariable=self.seconds_var, font=("Helvetica", 14))

        self.hours_entry.pack(pady=10)
        self.minutes_entry.pack(pady=10)
        self.seconds_entry.pack(pady=10)

        self.start_button = tk.Button(master, text="Start", command=self.start_timer)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(master, text="Stop", command=self.stop_timer)
        self.stop_button.pack(pady=10)

        self.label = tk.Label(master, text="Countdown Timer", font=("Helvetica", 24))
        self.label.pack(pady=20)

        self.running = False

        # Show the information message when the script is opened
        self.show_info_message("This timer was made by Mario <3")

        # Center the window on the screen
        self.center_window()

        # Show the main window after displaying the information message
        self.master.deiconify()

    def center_window(self):
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        window_width = 400
        window_height = 300

        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.master.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def start_timer(self):
        if not self.running:
            try:
                hours = int(self.hours_var.get())
                minutes = int(self.minutes_var.get())
                seconds = int(self.seconds_var.get())
                total_seconds = hours * 3600 + minutes * 60 + seconds

                if total_seconds <= 0:
                    raise ValueError("Invalid time input")

                self.remaining_time = total_seconds
                self.running = True
                self.update_timer()
            except ValueError as e:
                messagebox.showerror("Error", str(e))

    def update_timer(self):
        if self.running and self.remaining_time > 0:
            hours, remainder = divmod(self.remaining_time, 3600)
            minutes, seconds = divmod(remainder, 60)
            time_str = "{:02d}:{:02d}:{:02d}".format(int(hours), int(minutes), int(seconds))
            self.label.config(text=time_str, fg="green")  # Change the color to green
            self.remaining_time -= 1
            self.master.after(1000, self.update_timer)
        elif self.running and self.remaining_time == 0:
            # Beep sound for 5 seconds when the timer reaches zero
            for _ in range(5):
                winsound.Beep(1000, 500)  # For Windows
                # pygame.mixer.init()  # Uncomment these lines for cross-platform support
                # pygame.mixer.Sound("path/to/beep_sound.wav").play()

            self.show_info_message("This timer was made by Mario with ChatGPT <3")
            self.running = False
            self.label.config(text="Countdown Timer", fg="black")  # Reset color to black

    def stop_timer(self):
        if self.running:
            self.running = False
            self.label.config(text="Countdown Timer", fg="black")  # Reset color to black

    def show_info_message(self, message):
        messagebox.showinfo("Info", message)

if __name__ == "__main__":
    root = tk.Tk()
    timer_app = CountdownTimer(root)
    root.mainloop()
