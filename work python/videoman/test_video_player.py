# content of test_video_library.py
from video_library import Video, VideoLibrary

def test_list_all():
    # Create a video library instance
    video_library = VideoLibrary()

    # Get the list of all videos
    videos = video_library.list_all()

    # Check if the list has 7 videos
    assert len(videos) == 7

    # Check if the first video has the correct attributes
    assert videos[0].number == 1
    assert videos[0].name == "Tom and Jerry"
    assert videos[0].director == "Fred Quimby"
    assert videos[0].rating == 4
    assert videos[0].play_count == 0
    assert videos[0].picture == "img/tomandjerry.jpg"

