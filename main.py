# importing the module
from whisper_mic.whisper_mic import WhisperMic

# taking input
mic = WhisperMic(model="base", english=True)
mic_input = mic.listen(timeout=7)

# printing the recognized speech as output
print(mic_input)
