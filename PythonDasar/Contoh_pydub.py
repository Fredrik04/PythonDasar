from pydub import AudioSegment
from pydub.playback import play

#membaca file audio
audio = AudioSegment.from_file("input.mp3")
#memutar audio
play(audio)