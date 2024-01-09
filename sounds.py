from pygame.mixer import Sound
from pygame import mixer
mixer.pre_init(22050, -16, 1, 256)
mixer.init()
music = Sound('./Seventh heaven_ Thornton stuns Kiwis on Aus A debut _ Australia A v New Zealand A 2023(MP3_160K).mp3')
Sound.play(music)