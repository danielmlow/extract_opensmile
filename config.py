import argparse

# Modify default values
sampling_rate = 22050
bit_rate = '64k'
feature_level = 'func'  # or 'lld' for matrix

# Instantiate the parser
parser = argparse.ArgumentParser(description='Extract OpenSmile features')

parser.add_argument('input_dir', type=str,
                    help='path to directory of audios')

# Optional positional argument
parser.add_argument('--output_dir', type=str,nargs='?',
                    help='path to output for features')

args = parser.parse_args()

input_dir = args.input_dir
# if input_dir ==None:
# 	input_dir = './data/input/audio_examples/' #default

output_dir = args.output_dir
if output_dir == None:
	output_dir = input_dir+'../' #default


