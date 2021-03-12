

#!/usr/bin/env python3

'''
Authors: Daniel M. Low
License: Apache 2.0
'''



import datetime
import os
from pathlib import Path
import pandas as pd
import numpy as np
import opensmile
import convert_to_wav
import config





if __name__ == "__main__":
	# Config
	input_dir = config.input_dir
	output_dir = config.output_dir
	wav_conversion = config.wav_conversion
	sampling_rate = config.sampling_rate
	bit_rate = config.bit_rate
	feature_level = config.feature_level
	file_extension = config.file_extension

	# run
	# ========================================
	if file_extension:
		audio_filenames = list(Path(input_dir).rglob(f"*.{file_extension}"))
	else:
		audio_filenames = list(Path(input_dir).rglob(f"*"))
	
	audio_filenames = [str(n) for n in audio_filenames]
	audio_filenames = [filepath for filepath in audio_filenames if not any(word in filepath for word in ['.DS_Store'])]
	print(audio_filenames)


	
	try: 
		os.mkdir(output_dir)
		print('created output_dir')
	except: 
		print('did not create output_dir')
		pass

	if wav_conversion:
		# Convert to wav and output in this dir
		wav_dir = input_dir[:-1] + f'_wavs-{sampling_rate}fs-{bit_rate}/'

		try: os.mkdir(wav_dir)
		except: pass

		for filename in audio_filenames:
			print(filename)
			convert_to_wav.to_wav(input_dir=input_dir, filename=filename, output_dir=wav_dir,
			       output_filename=filename[:-4] + '.wav',
			       sampling_rate=sampling_rate, bit_rate=bit_rate)


		paths_to_audio = list(Path(wav_dir).rglob("*.[wW][aA][vV]"))
	else:
		paths_to_audio = list(Path(input_dir).rglob("*"))
		paths_to_audio = [str(n) for n in paths_to_audio]
		paths_to_audio = [n for n in paths_to_audio if n not in ['.DS_Store']]


	

	# Make sure all wavs have been converted
	# https://stackoverflow.com/questions/16196712/python-to-wait-for-shell-command-to-complete
	# p.wait()
	# while p.returncode == 0:
	# 	pass  # put code that must only run if successful here.

	# alternative import a config file: https://audeering.github.io/opensmile-python/usage.html#custom-config
	smile = opensmile.Smile(
		feature_set=opensmile.FeatureSet.eGeMAPSv02, #or path to conf: 'gemaps/eGeMAPSv02.conf'
		feature_level=feature_level,
	)

	
	vectors = smile.process_files(paths_to_audio)


	output_path = output_dir+ f"{input_dir.split('/')[-2]}_eGeMAPSv02_{feature_level}_{str(datetime.datetime.now()).replace(' ', '-').replace(':', '-').replace('.', '-')}.csv"

	vectors.to_csv(output_path)


