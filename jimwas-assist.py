import os
import time
import threading
import pyautogui
from PIL import Image
import google.generativeai as genai
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, simpledialog

# ----------------------------
# Gemini Config
# ----------------------------
def get_api_key():
    api_key = simpledialog.askstring("API Key", "Enter your Gemini API Key:", show="*")
    if not api_key:
        messagebox.showerror("API Key Error", "No API key provided. The application will exit.")
        exit(1)
    return api_key

API_KEY = get_api_key()
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# ----------------------------
# Screenshot Worker Thread
# ----------------------------
class ScreenshotWorker(threading.Thread):
    def __init__(self, interval, output_box, stop_event):
        super().__init__(daemon=True)
        self.interval = interval
        self.output_box = output_box
        self.stop_event = stop_event

    def run(self):
        while not self.stop_event.is_set():
            try:
                # Take screenshot
                screenshot = pyautogui.screenshot()
                screenshot.save("screenshot.png")
                img = Image.open("screenshot.png")

                # Ask Gemini
                response = model.generate_content([
                    "answer this question?",
                    img
                ])

                # Update GUI output
                self.output_box.config(state="normal")
                self.output_box.insert(tk.END, f"\nGemini: {response.text}\n")
                self.output_box.see(tk.END)
                self.output_box.config(state="disabled")

            except Exception as e:
                self.output_box.config(state="normal")
                self.output_box.insert(tk.END, f"\n[Error] {e}\n")
                self.output_box.see(tk.END)
                self.output_box.config(state="disabled")

            # Sleep until next interval or stop
            for _ in range(self.interval):
                if self.stop_event.is_set():
                    break
                time.sleep(1)

# ----------------------------
# GUI App
# ----------------------------
class ScreenshotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("JimWas Gemini Screenshot Assistant")
        self.root.geometry("700x500")

        self.stop_event = threading.Event()
        self.worker = None

        # Interval input
        ttk.Label(root, text="Interval (seconds):").pack(pady=5)
        self.interval_var = tk.StringVar(value="120")
        ttk.Entry(root, textvariable=self.interval_var, width=10).pack()

        # Start/Stop buttons
        button_frame = ttk.Frame(root)
        button_frame.pack(pady=10)
        ttk.Button(button_frame, text="Start", command=self.start).grid(row=0, column=0, padx=5)
        ttk.Button(button_frame, text="Stop", command=self.stop).grid(row=0, column=1, padx=5)

        # Output box
        self.output_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, state="disabled")
        self.output_box.pack(expand=True, fill="both", padx=10, pady=10)

    def start(self):
        if self.worker and self.worker.is_alive():
            messagebox.showinfo("Info", "Already running.")
            return

        try:
            interval = int(self.interval_var.get())
            if interval < 10:
                messagebox.showwarning("Warning", "Interval too short. Must be >= 10 seconds.")
                return
        except ValueError:
            messagebox.showerror("Error", "Invalid interval. Please enter a number.")
            return

        self.stop_event.clear()
        self.worker = ScreenshotWorker(interval, self.output_box, self.stop_event)
        self.worker.start()

        self.output_box.config(state="normal")
        self.output_box.insert(tk.END, f"\n[Started] Capturing every {interval} seconds...\n")
        self.output_box.config(state="disabled")

    def stop(self):
        if self.worker and self.worker.is_alive():
            self.stop_event.set()
            self.output_box.config(state="normal")
            self.output_box.insert(tk.END, "\n[Stopped]\n")
            self.output_box.config(state="disabled")
        else:
            messagebox.showinfo("Info", "Not running.")

# ----------------------------
# Run GUI
# ----------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = ScreenshotApp(root)
    root.mainloop()