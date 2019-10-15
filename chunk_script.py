import os
import shutil

from pydub import AudioSegment
from pydub.silence import detect_silence, split_on_silence

# a function that splits the audio file into chunks
# and applies speech recognition
def silence_based_conversion(path, seconds_waiting=0.1):
    # open the audio file stored in
    # the local system as a wav file.
    extension = path.split(".")[-1]
    if extension == "mp3":
        opener = AudioSegment.from_mp3
        song = opener(path)
    elif extension == "wav":
        opener = AudioSegment.from_wav
        song = opener(path)
    else:
        return "Bye Bye!"

    raw_length = song.duration_seconds

    # split track where silence is 0.5 seconds
    # or more and get chunks
    chunks = split_on_silence(song,
        # must be silent for at least 0.5 seconds
        # or 500 ms. adjust this value based on user
        # requirement. if the speaker stays silent for
        # longer, increase this value. else, decrease it.
        min_silence_len = int(seconds_waiting * 1000),

        # consider it silent if quieter than -16 dBFS
        # adjust this per requirement
        silence_thresh = -16
    )

    # create a directory to store the audio chunks.
    try:
        shutil.rmtree("audio_chunks")
    except:
        pass
    try:
        os.mkdir('audio_chunks')
    except:
        pass

    # move into the directory to
    # store the audio files.
    os.chdir('audio_chunks')

    i = 0
    # process each chunk
    for chunk in chunks:
        chunk_silent = AudioSegment.silent(duration=1000)
        audio_chunk = chunk + chunk_silent + chunk
        audio_chunk = split_on_silence(audio_chunk,
            # must be silent for at least 0.5 seconds
            # or 500 ms. adjust this value based on user
            # requirement. if the speaker stays silent for
            # longer, increase this value. else, decrease it.
            min_silence_len = int(seconds_waiting * 1000),

            # consider it silent if quieter than -16 dBFS
            # adjust this per requirement
            silence_thresh = -16
        )

        audio_chunk[0].export("./chunk{0}.wav".format(i), bitrate ='192k', format ="wav")

        i += 1

    if i == 0:
        combined = song
    else:
        playlist_songs = [opener(mp3_file) for mp3_file in os.listdir()]
        combined = AudioSegment.empty()
        for song in playlist_songs:
            combined += song

    os.chdir('..')
    return raw_length - combined.duration_seconds

if __name__ == '__main__':
    path_name = input("Enter the audio path: ")
    files = [os.path.join(path_name, file) for file in os.listdir(path_name) if file.split(".")[-1] in ["wav", "mp3"]]

    with open("silence.csv", "w") as f:
        f.write("filename,silence_length\n")
        for file in files:
            silence_time = silence_based_conversion(file)
            f.write("{},{}\n".format(file, silence_time))
