import os
import wave
import codecs

url = r"\\server10\Voice\Source\task2\wav"
rs = codecs.open("samplerate.txt", "+w", encoding="utf-8")

for dirs, folders, filenames in os.walk(url):
    for file_name in filenames:
        if file_name.endswith(".wav"):
            path = os.path.join(dirs, file_name)
            with wave.open(path, "rb") as wave_file:
                frame_rate = wave_file.getframerate()
                if frame_rate != 48000:
                    rs.write(dirs + "\t" + file_name + "\t" + str(frame_rate) + "\n")
            wave_file.close()