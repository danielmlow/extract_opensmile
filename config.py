import argparse
from distutils.util import strtobool
# Modify default values
sampling_rate = 16000
bit_rate = '64k'
feature_level = 'func'  # or 'lld' for matrix

# Instantiate the parser
parser = argparse.ArgumentParser(description='Extract OpenSmile features')

parser.add_argument('input_dir', type=str,
                    help='path to directory of audios. Required. ')

# Optional positional argument
parser.add_argument('--output_dir', type=str,nargs='?',
                    help='path to output for features or output to current dir')

parser.add_argument('--wav_conversion', type=str,nargs='?',
                    help='True or False. Default False because OpenSmile can handle most audio common files')

parser.add_argument('--file_extension', type=str,nargs='?',
                    help='wav, au, mp3, etc. default None.')


args = parser.parse_args()

input_dir = args.input_dir
# if input_dir ==None:
# 	input_dir = './data/input/audio_examples/' #default

output_dir = args.output_dir
if output_dir == None:
	output_dir = input_dir+'../' #default



wav_conversion = args.wav_conversion
if wav_conversion == None:
	wav_conversion = True
else:
	wav_conversion = strtobool(args.wav_conversion)



file_extension = args.file_extension



