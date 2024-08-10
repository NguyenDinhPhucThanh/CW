import tkinter as tk
from tkinter import messagebox
from video_library import VideoLibrary
from font_manager import FontManager
#   This is for UI
class CreateVideoList:
    def __init__(self, window):
        self.window = window
        self.video_library = VideoLibrary()
        self.font_manager = FontManager()
        self.playlist = []
        self.create_widgets()
    
    def create_widgets(self):
        self.window.title("Create Video List")
        self.window.geometry("400x300")

        # Create video number label and entry
        self.video_number_label = tk.Label(self.window, text="Video Number:", font=self.font_manager.get_label_font())
        self.video_number_label.grid(row=0, column=0, padx=10, pady=10)
        
        self.video_number_entry = tk.Entry(self.window)
        self.video_number_entry.grid(row=0, column=1, padx=10, pady=10)

        # Create add video button
        self.add_video_btn = tk.Button(self.window, text="Add Video", command=self.add_video, font=self.font_manager.get_button_font())
        self.add_video_btn.grid(row=0, column=2, padx=10, pady=10)

        # Create playlist text area
        self.playlist_textarea = tk.Text(self.window, height=10, width=40)
        self.playlist_textarea.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        # Create play playlist button
        self.play_playlist_btn = tk.Button(self.window, text="Play Playlist", command=self.play_playlist, font=self.font_manager.get_button_font())
        self.play_playlist_btn.grid(row=2, column=0, padx=10, pady=10)

        # Create reset playlist button
        self.reset_playlist_btn = tk.Button(self.window, text="Reset Playlist", command=self.reset_playlist, font=self.font_manager.get_button_font())
        self.reset_playlist_btn.grid(row=2, column=1, padx=10, pady=10)

    def add_video(self):
        video_number = self.video_number_entry.get()
        try:
            video_number = int(video_number)
        except ValueError:
            messagebox.showerror("Invalid Video Number", "Please enter a valid video number (integer).")
            return

        video = self.video_library.get_video(video_number)
        if video:
            video_info = (video.name, video.director)
            if video_info not in self.playlist:
                self.playlist.append(video_info)
                self.playlist_textarea.insert(tk.END, f"{video.number}. {video.name} (Director: {video.director})\n")
            else:
                messagebox.showerror("Duplicate Video", "This video is already in the playlist.")
        else:
            messagebox.showerror("Invalid Video Number", "Please enter a valid video number.")



        """
        video = self.video_library.get_video(int(video_number))
        if video:
            video_name = video['name']
            director_name = video['director']
            self.playlist.append((video_name, director_name))
            self.playlist_textarea.insert(tk.END, f"{video_name} (Director: {director_name})\n")
        else:
            messagebox.showerror("Invalid Video Number", "Please enter a valid video number.")
        """

    def play_playlist(self):
        for video_info in self.playlist:
            video_name, director_name = video_info
            video_number = self.get_video_number(video_name, director_name)
            if video_number:
                self.video_library.increment_play_count(video_number)

    def reset_playlist(self):
        self.playlist = []
        self.playlist_textarea.delete("1.0", tk.END)

    def get_video_number(self, video_name, director_name):
        for video in self.video_library.list_all():
            if video.name == video_name and video.director == director_name:
                return video.number
        return None

    def get_director_number(self, director_name):
        for video in self.video_library.list_all():
            if video['director'] == director_name:
                return video['number']
        return None

if __name__ == "__main__":
    window = tk.Tk()
    app = CreateVideoList(window)
    window.mainloop()
