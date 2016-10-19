"""
This module holds the Track class for representing playable audio files.
"""

from . import afplay
from . import errors


class Track(object):
    """
    Represents a playable audio file
    """

    def __init__(self, filepath):
        assert filepath
        self.filepath = filepath
        self.process = None

    def play(self, volume=1.0, time=0, rate=1.0, quality=1.0):
        if self.process:
            raise errors.AlreadyPlayingError()
        self.process = afplay.play(
            self.filepath, volume=volume, time=time, rate=rate, quality=quality
        )

    def stop(self):
        if not self.process:
            return
        if self.process.poll() is None:
            self.process.terminate()
        self.process = None

    def __repr__(self):
        return "Track({})".format(repr(self.filepath))
