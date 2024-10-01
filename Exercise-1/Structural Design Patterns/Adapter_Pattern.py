class MediaPlayer:
    def play(self, media_type, file_name):
        if media_type == "mp3":
            mp3_player = MP3Player()
            mp3_player.play_mp3(file_name)
        elif media_type == "mp4":
            mp4_player = MP4Player()
            mp4_player.play_mp4(file_name)
        else:
            print(f"Unsupported media type: {media_type}")


class MP3Player:
    def play_mp3(self, file_name):
        print(f"Playing MP3 file: {file_name}")


class MP4Player:
    def play_mp4(self, file_name):
        print(f"Playing MP4 file: {file_name}")

media_player = MediaPlayer()
media_player.play("mp3", "song.mp3")  
media_player.play("mp4", "video.mp4")  
