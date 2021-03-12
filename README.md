# Extract eGEMAPs features from a given directory


Clone this repository:
```
git clone https://github.com/danielmlow/extract_opensmile.git
```

Go to directory:
```
cd ./path/to/extract_opensmile/
```


# Conda

```
conda create --name opensmile --file requirements.txt
conda activate opensmile
python3 main.py /path/to/input_directory/ --output_path=/path/to/output_directory/ --file_extension=mp3 
```

* The the `--output_dir` argument is optional. If not specified will output to directory above the `input_dir`
* The the `--file_extension` argument is optional. If not specified will try to extract features from all files in the directories and subdirectories. Therefore it's best to specify what files you're trying to extract features from (wav, au, mp3).
* A `--wav_conversion` argument is optional. The opensmile package already does conversion to wav. 



Then `main.py` will:
1. convert to wav 22050 fs and 64 bits so they're all similar and will leave these wav files in the directory above the `input_dir`
2. extract egemaps features to the `output_dir`
