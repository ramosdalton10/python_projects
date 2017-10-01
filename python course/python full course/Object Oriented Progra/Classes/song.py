class Song(object):
    """" class to categories songs
    Attributes :
    Title
    Artist
    duration
    """

    def __init__(self, title, artist, duration):
        self.artist = artist
        self.title = title
        self.Duration = duration


class Album:
    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if self.artist is None:
            self.artist = 'various artist'
        else:
            self.artist = artist

        self.track = []

    def add_song(self, song, position=None):
        if position is None:
            self.track.append(song)
        else:
            self.track.insert(position, song)


class Artist:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        self.albums.append(album)

def load_data():
    new_artist = None
    song_name = None
    duration = 0

    with open("brayan_adams.txt") as f:
        for line in f:
            # print line
            number_field ,song_name_field, artist_field, album_field, duration_field = list (line.strip('\n').split('\t'))
            print '{}: {} {} {}' .format(number_field,song_name_field, artist_field, duration_field)

            # if new_artist is None:
            # #     song_name = Song(song_name_field)

if __name__ == '__main__':
    load_data()
