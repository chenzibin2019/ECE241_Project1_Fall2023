from unittest import TestCase

from song import Song

class TestSong(TestCase):
    def test_constructor(self):
        artist_name = "All Time Low"
        song_title = "Umbrella"
        song_id = "SOPOPLW12A8C13A905"
        duration = 227.70893
        year = 2008

        inst = Song(artist_name, song_title, song_id, duration, year)

    def test_play(self):
        self.fail()
