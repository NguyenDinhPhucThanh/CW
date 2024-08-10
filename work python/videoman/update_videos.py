import tkinter as tk
from tkinter import messagebox
from video_library import VideoLibrary
from font_manager import FontManager

class UpdateVideos:
    def __init__(self, window):
        self.window = window
        self.video_library = VideoLibrary()
        self.font_manager = FontManager()
        self.create_widgets()
    
    def create_widgets(self):
        self.window.title("Update Videos")
        self.window.geometry("400x150")

        # Create video number label and entry
        self.video_number_label = tk.Label(self.window, text="Video Number:", font=self.font_manager.get_label_font())
        self.video_number_label.grid(row=0, column=0, padx=10, pady=10)
        
        self.video_number_entry = tk.Entry(self.window)
        self.video_number_entry.grid(row=0, column=1, padx=10, pady=10)

        # Create rating label and entry
        self.rating_label = tk.Label(self.window, text="New Rating:", font=self.font_manager.get_label_font())
        self.rating_label.grid(row=1, column=0, padx=10, pady=10)
        
        self.rating_entry = tk.Entry(self.window)
        self.rating_entry.grid(row=1, column=1, padx=10, pady=10)

        # Create update video button
        self.update_video_btn = tk.Button(self.window, text="Update Video", command=self.update_video, font=self.font_manager.get_button_font())
        self.update_video_btn.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def update_video(self):
        video_number = self.video_number_entry.get()
        rating = self.rating_entry.get()

        if not video_number.isdigit():
            messagebox.showerror("Invalid Input", "Please enter a valid video number.")
            return

        video = self.video_library.get_video(int(video_number))
        if video:
            video_name = video.name
            play_count = video.play_count
            if not rating.isdigit():
                messagebox.showerror("Invalid Input", "Please enter a valid rating.")
                return
            self.video_library.set_rating(int(video_number), int(rating))
            messagebox.showinfo("Video Updated",
                                f"Video Name: {video_name}\n"
                                f"New Rating: {rating}\n"
                                f"Play Count: {play_count}")
        else:
            messagebox.showerror("Invalid Video Number", "Please enter a valid video number.")

if __name__ == "__main__":
    window = tk.Tk()
    app = UpdateVideos(window)
    window.mainloop()
