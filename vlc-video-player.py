import vlc
import time

player = vlc.Instance()
media_list = player.media_list_new()
media_player = player.media_list_player_new()

# creating a new media path
media = player.media_new_path("video.mp4")

media_list.add_media(media)
media_player.set_media_list(media_list)
media_player.play()

# Wait (review changes pending)
time.sleep(50)
