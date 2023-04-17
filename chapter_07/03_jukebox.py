import unittest


class Jukebox:
    def __init__(self):
        self.collection = {}
        self.playing = False
        self.playlist = []

    def play_song(self, song_id, current_song_id=None):
        if self.playing:
            self.stop_song()
            if current_song_id:
                self.collection[current_song_id].is_playing = False
        self.playing = True
        self.collection[song_id].is_playing = True

    def play_playlist(self):
        pass

    def stop_song(self):
        self.playing = False;

    def setup_collection(self, songs):
        for song in songs:
            self.collection[song.id] = song

class Song:
    def __init__(self, title, id):
        self.id = id
        self.title = title
        self.is_playing = False

    def play(self):
        self.is_playing = True

    def stop(self):
        self.is_playing = False

class Playlist:
    def __init__(self, song, queue):
        self.song = song;
        self.queue = queue;

    def get_next_song(self):
        return self.queue.pop(0)

    def queue_up_song(self, song):
        self.queue.append(song)

class Test(unittest.TestCase):
  def test_jukebox(self):
    song1 = Song("Just Dance", "1")
    song2 = Song("When You Wish Upon a Beard", "2")
    jukebox = Jukebox()
    jukebox.setup_collection([song1, song2])
    jukebox.play_song("2")
    self.assertEqual(jukebox.collection[song2.id].is_playing, True)

if __name__ == "__main__":
  unittest.main()