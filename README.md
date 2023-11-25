
# Audio File Format Converter

## Overview

The Audio File Format Converter is a Python script designed to convert audio files between different formats such as MP3, WAV, and MPEG. It utilizes the Factory design pattern to manage objects and facilitate audio conversions efficiently.

## Functionalities

-   Conversion between MP3, WAV, and MPEG formats.
-   Utilizes MoviePy library to handle audio file operations.
-   Support for multiple audio format conversions.

## Importance of Design Patterns in the Project

Design patterns provide proven solutions to common software design problems. In this project, the Factory design pattern is used to encapsulate the creation of specific audio converter objects based on the desired conversion format. This promotes scalability, maintainability, and flexibility in managing different audio formats for conversion.

## Dependencies

The script relies on the following dependencies:

-   `moviepy`: Library for video editing and audio extraction.

Install the dependencies using the following command:
```bash
pip install moviepy
```
## How to Run the Script

1.  Clone this repository to your local machine.
2.  Ensure Python is installed on your system (Python 3.10^ recommended).
3.  Install the required dependencies using the command provided above.
4.  Place the audio files you want to convert in a folder.
5.  Update the `folder_path`, `output_folder`, and `convert_to_format` variables in the script according to your requirements.
6.  Run the script using the command:
```bash
python audio_converter.py
```
7.  Check the specified output folder for the converted audio files.

## Additional Notes
-   Feel free to contribute to the project by expanding functionalities or optimizing the codebase.
