class Video:
    def __init__(self, number, name, director, rating, play_count, picture):
        self.number = number
        self.name = name
        self.director = director
        self.rating = rating
        self.play_count = play_count
        self.picture = picture

class VideoLibrary:
    # def __init__(self): This will make it so that value won't get updated.
    videos = [
            Video(1, "Tom and Jerry", "Fred Quimby", 4, 0, "img/tomandjerry.jpg"),
            Video(2, "Oshi no Ko", "Akasaka Aka", 5, 0, "img/oshinoko.jpg"),
            Video(3, "Dragon Ball Super", "Toriyama Akira", 3, 0, "img/goku.png"),
            Video(4, "Birdemic: Shock and Terror", "James Nguyễn", 1, 0, "img/bird.jpg"),
            Video(5, "Super Mario Bros Movie", "Roland Joffé", 2, 0, "img/mario.jpg"),
            Video(6, "Bocchi the Rock!", "Aki Hamaji", 4, 0, "img/bocc.jpg"),
            Video(7, "One Piece", "oda", 3, 0, "img/one piece.png"),
        ]
    
    def __init__(self):
        pass

    def list_all(self):
        return self.videos

    def get_director(self, video_number):
        for video in self.videos:
            if video.number == video_number:
                return video.director
        return None

    def get_rating(self, video_number):
        for video in self.videos:
            if video.number == video_number:
                return video.rating
        return None

    def set_rating(self, video_number, rating):
        for video in self.videos:
            if video.number == video_number:
                video.rating = rating
                return True
        return False

    def get_play_count(self, video_number):
        for video in self.videos:
            if video.number == video_number:
                return video.play_count
        return None

    def increment_play_count(self, video_number):
        for video in self.videos:
            if video.number == video_number:
                video.play_count += 1
                return True
        return False

    def get_video(self, video_number):
        for video in self.videos:
            if video.number == video_number:
                return video
        return None

    def get_name(self, video_number):
        for video in self.videos:
            if video.number == video_number:
                return video.name
        return None

    def add_to_list(self, number, name, director, rating, play_count, picture):
        video = Video(number, name, director, rating, play_count, picture)
        self.videos.append(video)

video_library = VideoLibrary()