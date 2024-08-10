import tkinter as tk
from tkinter import messagebox, filedialog
from video_library import video_library

class AddVideo:
    def __init__(self, window):
        self.window = window
        self.window.title("Add Video")

        self.label_number = tk.Label(self.window, text="Video Number:")
        self.label_name = tk.Label(self.window, text="Video Name:")
        self.label_director = tk.Label(self.window, text="Video Director:")
        self.label_rating = tk.Label(self.window, text="Video Rating (1-5):")
        self.label_picture = tk.Label(self.window, text="Video Picture:")
        self.entry_number = tk.Entry(self.window)
        self.entry_name = tk.Entry(self.window)
        self.entry_director = tk.Entry(self.window)
        self.entry_rating = tk.Entry(self.window)
        self.entry_picture = tk.Entry(self.window)
        self.browse_button = tk.Button(self.window, text="Browse", command=self.browse_picture)
        self.add_button = tk.Button(self.window, text="Add Video", command=self.add_video)

        # Grid layout
        self.label_number.grid(row=0, column=0, padx=5, pady=5)
        self.label_name.grid(row=1, column=0, padx=5, pady=5)
        self.label_director.grid(row=2, column=0, padx=5, pady=5)
        self.label_rating.grid(row=3, column=0, padx=5, pady=5)
        self.label_picture.grid(row=4, column=0, padx=5, pady=5)
        self.entry_number.grid(row=0, column=1, padx=5, pady=5)
        self.entry_name.grid(row=1, column=1, padx=5, pady=5)
        self.entry_director.grid(row=2, column=1, padx=5, pady=5)
        self.entry_rating.grid(row=3, column=1, padx=5, pady=5)
        self.entry_picture.grid(row=4, column=1, padx=5, pady=5, columnspan=2)
        self.browse_button.grid(row=4, column=3, padx=5, pady=5)
        self.add_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    def browse_picture(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        self.entry_picture.delete(0, tk.END)
        self.entry_picture.insert(0, file_path)

    def add_video(self):
        number = int(self.entry_number.get())
        name = self.entry_name.get()
        director = self.entry_director.get()
        rating = int(self.entry_rating.get())
        picture = self.entry_picture.get()

        # Check for duplicate video number
        for video in video_library.list_all():
            if video.number == number:
                messagebox.showerror("Error", f"Video with number {number} already exists.")
                return

        # Input validation for rating (1-5)
        if 1 <= rating <= 5:
            video_library.add_to_list(number, name, director, rating, play_count=0, picture=picture)
            messagebox.showinfo("Success", f"Video '{name}' has been added to the library.")
        else:
            messagebox.showerror("Error", "Invalid rating. Please enter a rating between 1 and 5.")


    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    window = tk.Tk()
    app = AddVideo(window)
    app.run()
