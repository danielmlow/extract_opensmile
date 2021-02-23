FROM python:3.7

COPY main.py ./

RUN pip install opensmile numpy pandas

CMD [ "python3", "./main.py", "/path/to/audio_files/"]