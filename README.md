# AudioSlicer for Python
This repository contains a Python based audio slicer that slices/trims audio file(s) into multiple files based on input that specifies start and end times.

Because the script uses FFmpeg, also video files can be sliced by using the appropriate FFmpeg options. We encourage people to adapt the script to slice media files for their own purposes, and refer to the FFmpeg documentation for more details about this.

This script is relevant for people who work with experimental phonetics, phonology, prosody and other academic disciplines dealing with segmenting media files, but also any other person who wants a powerful way to segment media files based on a prespecified batch (input file).

## Contents
* Python scripts
  *  AudioSlicer.py
  *  AudioSlicer_NWD.py
* Input containing start and end timestamps etc., three TXT files
* Four generated example audio files (not authentic)

## Usage
To use the script, you must:
* have installed FFmpeg
* customise the paths of InputDir, OutputDir and FFmpeg
* provide an appropriate input file (e.g., TXT) with an appropriate time format (HH:MM:SS.ms) that at the bare minimum specifies start and end timestamps and media filename(s)
* customise the FFmpeg input and output parameters accordingly

## About the scripts
We provide both the original script and a more general one. The original script was created to generate audio recordings for use in a prosodic analysis project based on data from [Nordic Word Order Database](https://www.hf.uio.no/iln/english/about/organization/text-laboratory/projects/nwd/index.html). The original script contains several tailored details that are appropriate for the purpose of that project, and can serve as a reference if you want to tailor it to your own project. The general script has been stripped down to a minimum.

### About the AudioSlicer_NWD.py script parameters
The original script sets out to slice audio files that are relevant for specific research purposes drawing on experimental data. Here, the script sets out to output separate audio files corresponding to experimental items which are prespecified with the categories of Informant (participant ID), UniqueNumb (experimental item ID), Begin_Time_ss_msec (start timestamp), End_Time_ss_msec (end timestamp), Type (experimental category: either "Read" or "Produce"), Sentence (experimental category: transcription of produced sentence), Pair (experimental linguistic category: e.g., "S(ubject)P(article)"), and Sex (participant category).

The prespecified information is based on a spreadsheet that contains rows corresponding to all of the experimental items in the database. The filtering of the relevant experimental items was done with Microsoft® Excel® (2016 32-bit, latest run version: 16.0.5173.1000), exported to TXT format (UTF-8 encoding), with some minor changes to the headers row.

The combination of headers information is used to output relevant audio files that has the following name format: Informant_Sex_UniqueNumb_Pair_Sentence_Type.wav (example: "OS03_M_1126_SP_Den nye studenten ryddet opp på kjøkkenet i går_Read.wav").

To test the script and reproduce the audio output files, the following file combination from the repository can be used (TXT and WAV files in input folder):
* AudioSlicer_NWD.py
* TXT files (here two separate files based on two different Pair-categories, to illustrate that it is possible this way)
  * slicelist_1.txt
  * slicelist_2.txt (Sentence and timestamps non–authentic)
* Audio files (here with Audacity® generated tones)
  * OS03.wav
  * OS04.wav
  * OS06.wav
  * OS07.wav

### About the AudioSlicer.py script parameters
This general version is stripped-down. The TXT file has stored Begin_Time and End_Time in the appropriate FFmpeg format HH:MM:SS.ms, and provides the audio filenames and UniqueNumb.

To test the script and reproduce the audio output files, the following file combination from the repository can be used (TXT and WAV files in input folder):
* AudioSlicer.py
* TXT file
  * slicelist.txt
* Audio files (here with Audacity® generated tones)
  * OS03.wav
  * OS04.wav
  * OS06.wav
  * OS07.wav

### Software
The following software has been used in the making of this script and the audio files:

* PyCharm 2021.3.1 (Community Edition) (latest runtime version: 11.0.13+7-b1751.21 amd64)
* Python 3.8
  * Libraries:
	  * math
	  * os
	  * glob
	  * subprocess
* FFmpeg 64-bit static Windows build (version: 2021-10-07-git-b6aeee2d8b-full_build-www.gyan.dev)
* Audacity® 2.1.2

## History
**Version 1.0.1** (2022.02.22): Added citation information.
**Version 1.0.0** (2022.01.22): Added repository to GitHub.

## Citation information
Please cite the script if you use it. The following citation example could be used (but it should be customised according to relevant citation style in academic contexts):

Tengesdal, Eirik and Moura, Marcel. 2022. AudioSlicer for Python (Version 1.0.0). [Software]. DOI: https://doi.org/10.5281/zenodo.5889527

Example of BibTeX entry:
```
@software{Tengesdal_Moura_AudioSlicer_2022,
    author	= {Tengesdal, Eirik and Moura, Marcel},
    title	= {{AudioSlicer for Python}},
    version	= {1.0.0},
    year	= {2022},
    doi		= {https://doi.org/10.5281/zenodo.5889527}
}
```
Please note that the following Concept DOI represents all of the versions of our record: https://doi.org/10.5281/zenodo.5889526
You can choose to cite a specific version of the repository, which is the recommended practice. Check the Version DOI at Zenodo.

## Funding
Part of this work has been funded by the Research Council of Norway project *Variation and Change in the Scandinavian Verb Phrase* (project number: 250755, PI: Ida Larsson).

## DOI
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5889526.svg)](https://doi.org/10.5281/zenodo.5889526)

## License and copyright
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

© 2022 Eirik Tengesdal and Marcel Moura

Licensed under the [MIT License](LICENSE).

## Authors
Eirik Tengesdal   
Department of Linguistics and Scandinavian Studies, University of Oslo   
eirik.tengesdal@iln.uio.no / eirik@tengesdal.name   
ORCID iD: [0000-0003-0599-8925](https://orcid.org/0000-0003-0599-8925)

Marcel Moura   
Department of Physics, University of Oslo   
