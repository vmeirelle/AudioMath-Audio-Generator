import random

from audiomath import Sound, MakeRise

sound01 = Sound("cooper_fulleon_sounder_tone_19")

sound01.Play()

soundFadedIn = sound01.Fade(4,0)

soundFadedIn.Play()
sound01.Play()

