
import subprocess


def play(filepath, volume=1.0, time=0, rate=1.0, quality=1.0):
    return subprocess.Popen([
        'afplay', str(filepath),
        '-v', str(volume),
        '-t', str(time),
        '-r', str(rate),
        '-q', str(quality),
    ])
