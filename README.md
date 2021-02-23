# Extract eGEMAPs features from a given directory

# Conda
conda create --name opensmile --file requirements.txt
conda activate opensmile
python3 main.py /path/to/input_directory/ /path/to/output_directory/ 
python3 main.py ./data/input/audio_examples/ --output_dir=./../egemaps_example/


The the `--output_dir` argument is optional. If not specified will output to directory above the `input_dir`

Then `main.py` will:
1. convert to wav 22050 fs and 64 bits so they're all similar and will leave these wav files in the directory above the `input_dir`
2. extract egemaps features to the output_dir

# Docker:
### TODO

`docker run -v /local/path/to/audio_files/:/container/path/to/audio_files/ -t extract_opensmile python3 main.py /path/to/audio_files/`
Then `/local/path/to/audio_files/` would be the path on your host machine which will override `/container/path/to/audio_files/` on the container.

 
