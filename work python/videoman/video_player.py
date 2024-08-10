import tkinter as tk
from tkinter import messagebox
import os
from check_videos import VideoChecker
from create_video_list import CreateVideoList
from update_videos import UpdateVideos
from font_manager import FontManager

class VideoPlayer:
    def __init__(self, window):
        self.window = window
        self.font_manager = FontManager()
        self.create_widgets()

    def create_widgets(self):
        self.window.title("Video Player")
        self.window.geometry("400x120")

        # Create a label for the title
        self.title_label = tk.Label(self.window, text="Select an option by clicking one of the buttons below",
                                    font=self.font_manager.get_title_font())
        self.title_label.grid(row=0, column=0, columnspan=3, pady=10)

        # Create buttons
        self.check_videos_btn = tk.Button(self.window, text="Check Videos", command=self.check_videos_window,
                                          font=self.font_manager.get_button_font())
        self.check_videos_btn.grid(row=1, column=0, padx=10, pady=5)

        self.create_video_list_btn = tk.Button(self.window, text="Create Video List", command=self.create_video_list,
                                               font=self.font_manager.get_button_font())
        self.create_video_list_btn.grid(row=1, column=1, padx=10, pady=5)

        self.update_videos_btn = tk.Button(self.window, text="Update Videos", command=self.update_videos,
                                           font=self.font_manager.get_button_font())
        self.update_videos_btn.grid(row=1, column=2, padx=10, pady=5)

        # Center align the buttons within the window
        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_columnconfigure(1, weight=1)
        self.window.grid_columnconfigure(2, weight=1)

    def check_videos_window(self):
        # Open a new window for video checking
        window = tk.Toplevel(self.window)
        app = VideoChecker(window)

    def create_video_list(self):
        window = tk.Toplevel(self.window)
        app = CreateVideoList(window)

    def update_videos(self):
        window = tk.Toplevel(self.window)
        app = UpdateVideos(window)

# This code is needed to function py file.
if __name__ == "__main__":
    window = tk.Tk()
    app = VideoPlayer(window)
    window.mainloop()
