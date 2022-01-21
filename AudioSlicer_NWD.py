#!python3
# -*- coding: utf-8 -*-

# This is a Python script for slicing/trimming audio or video file(s) based on input specifying start and end time(s)
# per audio or video file.

__author__ = "Eirik Tengesdal and Marcel Moura"
__copyright__ = "Copyright 2022"
__credits__ = ["Eirik Tengesdal", "Marcel Moura"]
__license__ = "MIT"
__version__ = "1.0.0"
__email__ = ["eirik@tengesdal.name", "eirik.tengesdal@iln.uio.no"]

# Created by Eirik Tengesdal, with help from Marcel Moura, released 21.01.2022. ET had the overall responsibility for
# the script. MM helped with defining the convert() function.

import math
import os
import glob
import subprocess


# Because the input TXT file used here has specified the start and end timestamps in the format (S...)SS.ms(...[≤3]),
# it should be converted to the HH:MM:SS.ms[...] format to be used for FFmpeg in CMD, hence the following convert()
# function definition. The function will convert into hours, minutes, seconds and milliseconds. If days are needed,
# additional calculations must be done (for days and ensuring that the hours do not exceed 24 hours.) This function
# requires a real number as an input, not a string. If the input is based on a TXT file string, and the milliseconds
# must be intact, try using float("str"). int("str") will give an error message like: "ValueError: invalid literal
# for int( ) with base 10: "1858.893"" Note that the output formatting might be necessary to customise further;
# "%02d" and "%d" do not output the same amount of digits. "%d" is a placeholder for a decimal integer (which are
# necessary for the function calculations), while "%s" is a placeholder for string values.


def convert(seconds_full):
    seconds = math.floor(seconds_full)
    milliseconds = round((seconds_full - seconds) * 1000)
    hour = seconds // 3600
    minutes = (seconds - hour * 3600) // 60
    seconds = (seconds - hour * 3600) - (minutes * 60)
    return "%02d:%02d:%02d.%d" % (hour, minutes, seconds, milliseconds)


# A test (manipulate length of input number to test whether the returned number has correct conversion and format):
# n = float("1858.893") # Must coerce string into float number because of the input TXT list.
# n = 1858.893 # If "n = "1858.893"", then "TypeError: must be real number, not str".
# print(convert(n))
# (Given the value of n above, the function should yield: "00:30:58.893")

# Specify the input and output folders. The input folder should contain any audio or video file and file(s) containing
# the start and end timestamps that the script will use during slicing/trimming.

InputDir = "C:/Users/Eirik/Desktop/AudioSlicer/input/"
OutputDir = "C:/Users/Eirik/Desktop/AudioSlicer/output/"

# Check whether the specified path, here OutputDir, exists or not:
os.path.exists(OutputDir)
isExist = os.path.exists(OutputDir)
if not isExist:
    # Create a new directory because it does not exist:
    os.makedirs(OutputDir)
    print("The new directory is created as specified!")

# Run the script. Here, the input tab-delimited TXT file is located in InputDir. (This script loops over all TXT
# files in the same folder; either one or several TXT files with the same structure (identical headers) should work.)
# Here, "encoding="utf-8"" is added because the TXT files are saved with UTF-8 encoding. Remove it if necessary.

for file in glob.glob(InputDir + "*.txt"):
    first = True
    with open(file, encoding="utf-8") as f:
        for line in f.readlines():
            if first:
                first = False
            else:
                Informant, UniqueNumb, Begin_Time_ss_msec, End_Time_ss_msec, Type, Sentence, Pair, Sex = line.strip().split(
                    "\t")  # TXT tabulator separated values -> "\t"
                print(line)
                cmd = [r"C:\FFmpeg\bin\ffmpeg.exe",
                       "-i",
                       InputDir + Informant + ".wav",
                       "-ss",
                       convert(float(Begin_Time_ss_msec)),
                       "-to",
                       convert(float(End_Time_ss_msec)),
                       "-c",
                       "copy",
                       OutputDir + Informant + "_" + Sex + "_" + UniqueNumb + "_" + Pair + "_" + Sentence[:-1] + "_" + Type + ".wav"]
                print(" ".join(cmd))
                subprocess.run(cmd, stderr=subprocess.STDOUT)

# In this input TXT file, the input audio file corresponds in part to the Informant number. Therefore,
# the input audio file for FFmpeg is given as "InputDir + Informant + ".wav"". If the input TXT file instead has the
# audio filename itself, e.g., AudioFilename = "OS03.wav" instead of Informant = "OS03", then the output filename
# must be customised differently, e.g., "AudioFilename[:-4] + UniqueNumb + "AudioFilename[-4:]" (i.e., here adding
# UniqueNumb between the filename and its ".wav" extension.) The script also presupposes that all the lines in the
# TXT file will be used for the slicing; it does not filter a subset of rows.

# Acknowledgements:
# This script is based on several online resources:
# https://appdividend.com/2021/07/03/how-to-create-directory-if-not-exist-in-python/
# https://stackoverflow.com/questions/52934200/typeerror-must-be-real-number-not-str
# https://www.gyan.dev/ffmpeg/builds/ (Download and install the latest master build locally, for the cmd = [] # command)
# https://stackoverflow.com/questions/4288973/whats-the-difference-between-s-and-d-in-python-string-formatting/56382046
# https://stackoverflow.com/questions/3964681/find-all-files-in-a-directory-with-extension-txt-in-python
# Most influential: https://stackoverflow.com/questions/56767886/trimming-videos-using-ffmpeg-python-invalid-argument
