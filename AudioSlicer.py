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

import os
import glob
import subprocess

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
                Filename, UniqueNumb, Begin_Time, End_Time = line.strip().split(
                    "\t")  # TXT tabulator separated values -> "\t"
                print(line)
                cmd = [r"C:\FFmpeg\bin\ffmpeg.exe",
                       "-i",
                       InputDir + Filename,
                       "-ss",
                       Begin_Time,
                       "-to",
                       End_Time,
                       "-c",
                       "copy",
                       OutputDir + Filename[:-4] + "_" + UniqueNumb + Filename[-4:]]
                print(" ".join(cmd))
                subprocess.run(cmd, stderr=subprocess.STDOUT)


# Acknowledgements:
# This script is based on several online resources:
# https://appdividend.com/2021/07/03/how-to-create-directory-if-not-exist-in-python/
# https://www.gyan.dev/ffmpeg/builds/ (Download and install the latest master build locally, for the cmd = [] # command)
# https://stackoverflow.com/questions/3964681/find-all-files-in-a-directory-with-extension-txt-in-python
# Most influential: https://stackoverflow.com/questions/56767886/trimming-videos-using-ffmpeg-python-invalid-argument
