# Chunk

Takes in a directory then extract the silent durations of every audio file present. Then it will return a csv file with the durations.

Silence is defined by 1/10 of a second.

## Setting up
* Install Python
* run `pip install pydub` - This is a python wrapper for ffmpeg
* setup `ffmpeg` - follow instructions from the official website [https://www.ffmpeg.org](https://www.ffmpeg.org)

## Usage
* Run the script and provide a directory for it to scan


You can pass an additional `seconds_waiting` parameter. This is the minimum amount of time in seconds for a part of the audio to be classified as silence.
