class Member:

    def __init__(self, name, birthname, birthday, zodiac, bloodtype, color, animal, fruit, song, song_url, subunit):
        self.name = name
        self.birthname = birthname
        self.birthday = birthday
        self.zodiac = zodiac
        self.bloodtype = bloodtype
        self.color = color
        self.animal = animal
        self.fruit = fruit
        self.song = song
        self.song_url = song_url
        self.subunit = subunit

    def stream(self):
        print(self.song_url)


class Jinsoul(Member):

    def __init__(self):
        Member.__init__(self,
                        "Jinsoul",
                        "Jung Jinsol",
                        "June 13, 1997",
                        "Gemini",
                        "B",
                        "Blue",
                        "Blue Betta",
                        None,
                        "Singing in the Rain",
                        "https://www.youtube.com/watch?v=RWeyOyY_puQ",
                        "Odd Eye Circle"
                        )


class Olivia(Member):

    def __init__(self):
        Member.__init__(self,
                        "Olivia Hye",
                        "Son Hyejoo",
                        "November 13, 2001",
                        "Scorpio",
                        "B",
                        "Grey",
                        "Wolf",
                        "Blood Plum",
                        "Egoist",
                        "https://www.youtube.com/watch?v=UkY8HvgvBJ8",
                        "YYXY"
                        )

    def roll(self):
        pass
