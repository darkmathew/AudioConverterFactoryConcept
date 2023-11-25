import unittest
from os import path
from audio_converter import Mp3ToWavConverter, WavToMp3Converter

class AudioConverterTests(unittest.TestCase):
    def test_mp3_to_wav_conversion(self):
        # Test MP3 to WAV conversion
        mp3_converter = Mp3ToWavConverter()
        input_path = 'path/to/input_file.mp3'  # Update with a valid MP3 file path
        output_path = 'path/to/output_file.wav'  # Update with the expected output WAV file path
        mp3_converter.convert(input_path, output_path)
        self.assertTrue(path.exists(output_path))  # Check if the output file exists

    def test_wav_to_mp3_conversion(self):
        # Test WAV to MP3 conversion
        wav_converter = WavToMp3Converter()
        input_path = 'path/to/input_file.wav'  # Update with a valid WAV file path
        output_path = 'path/to/output_file.mp3'  # Update with the expected output MP3 file path
        wav_converter.convert(input_path, output_path)
        self.assertTrue(path.exists(output_path))  # Check if the output file exists

if __name__ == '__main__':
    unittest.main()
    # python -m unittest test.py
