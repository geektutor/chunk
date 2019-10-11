# Chunk

Split an audio file into different chunks where silence is identified

## Setting up
* Install Python
* run `pip install pydub` - This is a python wrapper for ffmpeg
* setup `ffmpeg` - follow instructions from the official website [https://www.ffmpeg.org](https://www.ffmpeg.org)

## Usage
* Run the script and provide an audio file (mp3 or wav)
there are also few types of audio files you can add e.g wma, ogg and aiff. 


You can pass an additional `seconds_waiting` parameter. This is the minimum amount of time in seconds for a part of the audio to be classified as silence.
