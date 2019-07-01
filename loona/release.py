import datetime


class Song:

    def __init__(self, name, **kwargs):
        self.name = name
        self.duration = kwargs.get('duration')
        self.lyrics = kwargs.get('lyrics')
        self.url = kwargs.get('url')

    def __repr__(self):
        return self.name


class Album:

    def __init__(self, name, **kwargs):
        self.name = name
        self.release_date = kwargs.get('release_date')
        self.songs = kwargs.get('songs', [])

    def __repr__(self):
        return self.name + "\n" + self.tracklist() + "\n"

    def tracklist(self):
        return "\n".join(f"{i}. {song} - {song.duration}" for i, song in enumerate(self.songs, start=1))

    def add_song(self, song: Song):
        self.songs.append(song)


class PlusPlus(Album):

    def __init__(self):
        Album.__init__(self, '[+ +]', release_date=datetime.date(2018, 8, 7))

        self.add_song(Song('+ +',
                           duration=datetime.timedelta(seconds=58),
                           url=""))

        self.add_song(Song('Hi High',
                           duration=datetime.timedelta(minutes=3, seconds=17),
                           url=""))

        self.add_song(Song('favOriTe',
                           duration=datetime.timedelta(minutes=3, seconds=14),
                           url=""))

        self.add_song(Song('Heat',
                           duration=datetime.timedelta(minutes=3, seconds=30),
                           url=""))

        self.add_song(Song('Perfect Love',
                           duration=datetime.timedelta(minutes=3, seconds=42),
                           url=""))

        self.add_song(Song('Stylish',
                           duration=datetime.timedelta(minutes=3, seconds=29),
                           url=""))


class MultipleMultiple(Album):

    def __init__(self):
        Album.__init__(self, '[X X]', release_date=datetime.date(2019, 2, 19))

        self.add_song(Song('X X',
                           duration=datetime.timedelta(seconds=49),
                           url=""))

        self.add_song(Song('Butterfly',
                           duration=datetime.timedelta(minutes=3, seconds=58),
                           url=""))

        self.add_song(Song('Satellite',
                           duration=datetime.timedelta(minutes=3, seconds=10),
                           url=""))

        self.add_song(Song('Curiosity',
                           duration=datetime.timedelta(minutes=3, seconds=9),
                           url=""))

        self.add_song(Song('Colors',
                           duration=datetime.timedelta(minutes=3, seconds=15),
                           url=""))

        self.add_song(Song('Where you at',
                           duration=datetime.timedelta(minutes=3, seconds=27),
                           url=""))
