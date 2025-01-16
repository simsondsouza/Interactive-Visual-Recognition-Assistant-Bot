import subprocess
from main import audio_input

while True:
    if "athena" in audio_input().lower():
        subprocess.Popen("python main.py",shell=True)
        break
    else:
        continue
