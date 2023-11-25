
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
```python
if __name__ == '__main__':
    folder_path = './audio_path/'  # Update with the input folder containing audio files
    output_folder = './converted_files'  # Update with the desired output folder for converted files
    convert_to_format = '.wav'  # Update with the desired audio format to convert to
    
    # Option 1) Use this for convert all files in a folder.
    convert_files_in_folder(folder_path, convert_to_format, output_folder)
    
    # Option 2) Or just use this for a single file conversion
    mp3_converter = Mp3ToWavConverter()
    input_path = 'path/to/input_file.mp3'  # Update with a valid MP3 file path
    output_path = 'path/to/output_file.wav'  # Update with the expected output WAV file path
    mp3_converter.convert(input_path, output_path)
```
6.  Run the script using the command:
```bash
python audio_converter.py
```
7.  Check the specified output folder for the converted audio files.

## Additional Notes
-   Feel free to contribute to the project by expanding functionalities or optimizing the codebase.
