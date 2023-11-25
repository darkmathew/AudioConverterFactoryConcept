from abc import ABC, abstractmethod
from moviepy.editor import AudioFileClip
from os.path import exists, splitext
from os import makedirs, listdir, path

class AudioConverter(ABC):
    @abstractmethod
    def convert(self, input_path : str, output_path : str):
        pass

class Mp3ToWavConverter(AudioConverter):
    def convert(self, input_path : str, output_path : str):
        audio = AudioFileClip(input_path)
        audio.write_audiofile(output_path, codec='pcm_s16le')

class WavToMp3Converter(AudioConverter):
    def convert(self, input_path : str, output_path : str):
        audio = AudioFileClip(input_path)
        audio.write_audiofile(output_path, codec='libmp3lame')

class MpegToMp3Converter(AudioConverter):
    def convert(self, input_path : str, output_path : str):
        audio = AudioFileClip(input_path)
        audio.write_audiofile(output_path, codec='libmp3lame')

class MpegToWavConverter(AudioConverter):
    def convert(self, input_path : str, output_path : str):
        audio = AudioFileClip(input_path)
        audio.write_audiofile(output_path, codec='pcm_s16le')

class AudioConverterFactory:
    @staticmethod
    def create_converter(file_extension : str, convert_to : str):
        if file_extension == '.mp3' and convert_to == '.wav':
            return Mp3ToWavConverter()
        elif file_extension == '.wav' and convert_to == '.mp3':
            return WavToMp3Converter()
        elif file_extension == '.mpeg' and convert_to == '.mp3':
            return MpegToMp3Converter()
        elif file_extension == '.mpeg' and convert_to == '.wav':
            return MpegToWavConverter()

        raise ValueError(f'Conversion from {file_extension} to {convert_to} not supported.')

def convert_files_in_folder(folder_path : str, convert_to_format : str, output_folder : str):
    if not exists(folder_path):
        print(f'The path {folder_path} does not exist.')
        return

    files = listdir(folder_path)
    audio_converter = AudioConverterFactory()

    supported_extensions = ['.mp3', '.wav', '.mpeg']

    for file in files:
        file_extension = splitext(file)[1].lower()

        if file_extension not in supported_extensions or file_extension == convert_to_format: continue

        try:
            converter = audio_converter.create_converter(file_extension, convert_to_format)
            input_path = path.join(folder_path, file)
            makedirs(output_folder, exist_ok=True)
            output_path = path.join(output_folder, splitext(file)[0] + convert_to_format)
            converter.convert(input_path, output_path)
        except ValueError as e:
            print(e)

    print(f'Conversion completed. Converted files saved in {output_folder}.')

if __name__ == '__main__':
    folder_path = './audio_path/'  # Update with the input folder containing audio files
    output_folder = './converted_files'  # Update with the desired output folder for converted files
    convert_to_format = '.wav'  # Update with the desired audio format to convert to

    convert_files_in_folder(folder_path, convert_to_format, output_folder)

