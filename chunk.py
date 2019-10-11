import os

from pydub import AudioSegment
from pydub.silence import split_on_silence

# a function that splits the audio file into chunks
# and applies speech recognition
def silence_based_conversion(path, seconds_waiting=1):
    # open the audio file stored in
    # the local system as a wav file.
    extension = path.split(".")[-1]
    if extension == "mp3":
        song = AudioSegment.from_mp3(path)
    elif extension == "wav":
        song = AudioSegment.from_wav(path)
    else:
        return "Bye Bye!"

    # split track where silence is 0.5 seconds
    # or more and get chunks
    chunks = split_on_silence(song,
        # must be silent for at least 0.5 seconds
        # or 500 ms. adjust this value based on user
        # requirement. if the speaker stays silent for
        # longer, increase this value. else, decrease it.
        min_silence_len = seconds_waiting * 1000,

        # consider it silent if quieter than -16 dBFS
        # adjust this per requirement.
        silence_thresh = -16
    )

    # create a directory to store the audio chunks.
    try:
        os.mkdir('audio_chunks')
    except(FileExistsError):
        pass

    # move into the directory to
    # store the audio files.
    os.chdir('audio_chunks')

    i = 0
    # process each chunk
    for chunk in chunks:
        # Create silence chunk
        chunk_silent = AudioSegment.silent(duration = 10)

        # add 0.5 sec silence to beginning and
        # end of audio chunk. This is done so that
        # it doesn't seem abruptly sliced.
        audio_chunk = chunk_silent + chunk + chunk_silent

        # export audio chunk and save it in
        # the current directory.
        print("saving chunk{0}.wav".format(i))

        # specify the bitrate to be 192 k
        audio_chunk.export("./chunk{0}.wav".format(i), bitrate ='192k', format ="wav")

        i += 1

    os.chdir('..')


if __name__ == '__main__':
    silence_based_conversion(input("Enter audio file name: "))
