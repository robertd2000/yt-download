import pytube


def get_video(id, path=''):
    yt = pytube.YouTube(id)

    videos = yt.streams.filter(progressive=True, file_extension='mp4')
    video = videos[-1]

    video.download(path)

    print(videos)

    return video

# 'https://www.youtube.com/watch?v=EJ5L9Ed2z5Q'
# '\\Users\\капитал\\Desktop\\udemy'
