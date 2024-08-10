import tkinter as tk
from tkinter import messagebox
import os
from PIL import Image, ImageTk #Needed for displaying images
from video_library import video_library
from font_manager import FontManager
from add_video import AddVideo

class VideoChecker:
    def __init__(self, window):
        self.window = window
        self.font_manager = FontManager()
        self.create_widgets()

    def create_widgets(self):
        self.window.title("Check Videos")
        self.window.geometry("900x600")

        self.list_videos_btn = tk.Button(self.window, text="List Videos", command=self.list_all_videos, font=self.font_manager.get_button_font())
        self.list_videos_btn.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.add_videos_btn = tk.Button(self.window, text="Add Videos", command=self.add_videos_window, font=self.font_manager.get_button_font())
        self.add_videos_btn.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.video_list_text = tk.Text(self.window, height=10, width=30, font=self.font_manager.get_text_font())
        self.video_list_text.grid(row=1, column=0, padx=10, pady=10, sticky="nsew", columnspan=2)

        self.video_number_label = tk.Label(self.window, text="Enter Video Number:", font=self.font_manager.get_label_font())
        self.video_number_label.grid(row=0, column=2, padx=10, pady=10, sticky="e")

        self.video_number_entry = tk.Entry(self.window)
        self.video_number_entry.grid(row=0, column=3, padx=10, pady=10, sticky="w")

        self.check_video_btn = tk.Button(self.window, text="Check Video", command=self.check_video, font=self.font_manager.get_button_font())
        self.check_video_btn.grid(row=0, column=3, padx=10, pady=10, sticky="e")

        self.canvas = tk.Canvas(self.window, width=180, height=180)
        self.canvas.grid(row=2, column=2)

        self.video_info_text = tk.Text(self.window, height=10, width=30, font=self.font_manager.get_text_font())
        self.video_info_text.grid(row=1, column=2, padx=10, pady=10, sticky="nsew", columnspan=3)

        self.result_label = tk.Label(self.window, text="Output", font=self.font_manager.get_title_font())
        self.result_label.grid(row=2, column=0, padx=10, pady=10, sticky="nw")

        self.result_text = tk.Text(self.window, height=4, width=30, font=self.font_manager.get_text_font())
        self.result_text.grid(row=2, column=0, columnspan=2, padx=10, pady=40, sticky="nw")

        self.search_label = tk.Label(self.window, text="Search Videos/Directors:", font=self.font_manager.get_label_font())
        self.search_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        self.search_entry = tk.Entry(self.window)
        self.search_entry.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        self.search_btn = tk.Button(self.window, text="Search", command=self.search_videos_directors, font=self.font_manager.get_button_font())
        self.search_btn.grid(row=3, column=2, padx=10, pady=10, sticky="w")

        self.search_result_text = tk.Text(self.window, height=6, width=30, font=self.font_manager.get_text_font())
        self.search_result_text.grid(row=4, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        self.window.grid_rowconfigure(1, weight=1)
        self.window.grid_columnconfigure(3, weight=1)

    def list_all_videos(self):
        self.result_text.insert(tk.END, "List all videos button is clicked\n")
        videos = video_library.list_all()
        self.video_list_text.delete(1.0, tk.END)
        for video in videos:
            rating_stars = "*" * video.rating + " " * (5 - video.rating)
            self.video_list_text.insert(tk.END, f"{video.number}: {video.name} - {video.director} {rating_stars}\n")

    def add_videos_window(self):
        window = tk.Toplevel(self.window)
        app = AddVideo(window)

    def check_video(self):
        self.result_text.insert(tk.END, "Check video button is clicked\n")
        video_number = self.video_number_entry.get()

        if not video_number:
            messagebox.showinfo("Missing Video Number", "Please insert video number")
            return

        self.video_info_text.delete(1.0, tk.END)
        
        try:
            video_number = int(video_number)
        except ValueError:
            messagebox.showinfo("Invalid Video Number", "Please enter a valid video number")
            return

        video = video_library.get_video(video_number)
        if video is not None:
            rating_stars = "*" * video.rating + " " * (5 - video.rating)
            self.video_info_text.insert(tk.END, f"Video {video.number}: {video.name}\n")
            self.video_info_text.insert(tk.END, f"Directed by {video.director}\n")
            self.video_info_text.insert(tk.END, f"Rating: {rating_stars}\n")
            play_count = video_library.get_play_count(video.number)
            self.video_info_text.insert(tk.END, f"Play Count: {play_count}\n")
            #Display image
            img = Image.open(video.picture)
            img = img.resize((180, 180), resample=Image.NEAREST)
            self.window.photo_img = photo_img = ImageTk.PhotoImage(img)
            self.canvas.create_image((0, 0), image=photo_img, anchor="nw")
        else:
            self.video_info_text.insert(tk.END, "Video not found")


    def get_name(self):
        video_number = self.video_number_entry.get()
        name = video_library.get_name(int(video_number))
        if name is not None:
            messagebox.showinfo("Video Name", f"The name of video {video_number} is {name}")
        else:
            messagebox.showinfo("Video Not Found", f"Video {video_number} not found")

    def get_director(self):
        video_number = self.video_number_entry.get()
        director = video_library.get_director(int(video_number))
        if director is not None:
            messagebox.showinfo("Video Director", f"The director of video {video_number} is {director}")
        else:
            messagebox.showinfo("Video Not Found", f"Video {video_number} not found")

    def get_rating(self):
        video_number = self.video_number_entry.get()
        rating = video_library.get_rating(int(video_number))
        if rating is not None:
            messagebox.showinfo("Video Rating", f"The rating of video {video_number} is {rating}")
        else:
            messagebox.showinfo("Video Not Found", f"Video {video_number} not found")

    def set_rating(self):
        video_number = self.video_number_entry.get()
        rating = messagebox.askinteger("Set Rating", f"Enter new rating for video {video_number}: ")
        if rating is not None:
            success = video_library.set_rating(int(video_number), rating)
            if success:
                messagebox.showinfo("Rating Updated", f"The rating of video {video_number} has been updated to {rating}")
            else:
                messagebox.showinfo("Video Not Found", f"Video {video_number} not found")

    def get_play_count(self):
        video_number = self.video_number_entry.get()
        play_count = video_library.get_play_count(int(video_number))
        if play_count is not None:
            messagebox.showinfo("Play Count", f"The play count of video {video_number} is {play_count}")
        else:
            messagebox.showinfo("Video Not Found", f"Video {video_number} not found")

    def increment_play_count(self):
        video_number = self.video_number_entry.get()
        success = video_library.increment_play_count(int(video_number))
        if success:
            play_count = video_library.get_play_count(int(video_number))
            messagebox.showinfo("Play Count Updated", f"The play count of video {video_number} has been incremented to {play_count}")
        else:
            messagebox.showinfo("Video Not Found", f"Video {video_number} not found")

    def search_videos_directors(self):
        query = self.search_entry.get().strip().lower()
        if not query:
            return

        found_videos = []
        for video in video_library.list_all():
            if query in video.name.lower() or query in video.director.lower():
                found_videos.append(video)

        self.search_result_text.delete(1.0, tk.END)
        if found_videos:
            for video in found_videos:
                rating_stars = "*" * video.rating + " " * (5 - video.rating)
                self.search_result_text.insert(tk.END, f"{video.number}: {video.name} - {video.director} {rating_stars}\n")
        else:
            self.search_result_text.insert(tk.END, "No matching videos/directors found.")


if __name__ == "__main__":
    window = tk.Tk()
    app = VideoChecker(window)
    window.mainloop()