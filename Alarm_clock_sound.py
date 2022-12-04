from pygame import mixer

mixer.init # Initializing the mixer
mixer.music.load('sound1.mp3')
mixer.music.play()