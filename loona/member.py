import datetime


class Member:

    def __init__(self, name, **kwargs):
        self.name = name
        self.name_kr = kwargs.get('name_kr')
        self.birthname = kwargs.get('birthname')
        self.birthname_kr = kwargs.get('birthname_kr')
        self.birthday = kwargs.get('birthday')
        self.zodiac = kwargs.get('zodiac')
        self.bloodtype = kwargs.get('bloodtype')
        self.color = kwargs.get('color')
        self.animal = kwargs.get('animal')
        self.fruit = kwargs.get('fruit')
        self.song = kwargs.get('song')
        self.song_url = kwargs.get('song_url')
        self.subunit = kwargs.get('subunit')
        self.location = kwargs.get('location')
        self.debut = kwargs.get('debut')

    def __str__(self):
        return self.name

    def stream(self):
        print(self.song_url)

    def age(self):
        return int((datetime.date.today() - self.birthday).days/365.2425)

    def age_kr(self):
        return datetime.date.today().year - self.birthday.year + 1

    def days_since_debut(self):
        return (datetime.date.today() - self.debut).days


class Heejin(Member):

    def __init__(self):
        Member.__init__(self, "Heejin",
                        name_kr="희진",
                        birthname="Jeon Heejin",
                        birthname_kr="전희진",
                        birthday=datetime.date(2000, 10, 19),
                        zodiac="Libra",
                        bloodtype="A",
                        color="Hot Pink",
                        animal="Rabbit",
                        song="ViViD",
                        song_url="https://www.youtube.com/watch?v=-FCYE87P5L0",
                        subunit="1/3",
                        location="Paris, France",
                        debut=datetime.date(2016, 9, 25)
                        )


class Hyunjin(Member):

    def __init__(self):
        Member.__init__(self, "Hyunjin",
                        name_kr="현진",
                        birthname="Kim Hyunjin",
                        birthname_kr="김현진",
                        birthday=datetime.date(2000, 11, 15),
                        zodiac="Scorpio",
                        bloodtype="AB",
                        color="Yellow",
                        animal="Cat",
                        song="Around You",
                        song_url="https://www.youtube.com/watch?v=mybsDDymrsc",
                        subunit="1/3",
                        location="Tokyo, Japan",
                        debut=datetime.date(2016, 10, 28)
                        )


class Haseul(Member):

    def __init__(self):
        Member.__init__(self, "Haseul",
                        name_kr="하슬",
                        birthname="Jo Haseul",
                        birthname_kr="조하슬",
                        birthday=datetime.date(1997, 8, 18),
                        zodiac="Leo",
                        bloodtype="O",
                        color="Green",
                        animal="White Bird",
                        song="Let Me In",
                        song_url="https://www.youtube.com/watch?v=6a4BWpBJppI",
                        subunit="1/3",
                        location="Iceland & London, England",
                        debut=datetime.date(2016, 12, 8)
                        )


class Yeojin(Member):

    def __init__(self):
        Member.__init__(self, "Yeojin",
                        name_kr="여진",
                        birthname="Im Yeojin",
                        birthname_kr="임여진",
                        birthday=datetime.date(2002, 11, 11),
                        zodiac="Scorpio",
                        bloodtype="B",
                        color="Orange",
                        animal="Frog",
                        song="Kiss Later",
                        song_url="https://www.youtube.com/watch?v=thpTOAS1Vgg",
                        location="Taipei, Taiwan",
                        debut=datetime.date(2017, 1, 4)
                        )


class Vivi(Member):

    def __init__(self):
        Member.__init__(self, "ViVi",
                        name_kr="비비",
                        birthname="Wong Kahei",
                        birthname_kr="황아라",
                        birthday=datetime.date(1996, 12, 9),
                        zodiac="Sagittarius",
                        bloodtype="B",
                        color="Light Pink",
                        animal="Deer",
                        song="Everyday I Love You",
                        song_url="https://www.youtube.com/watch?v=ZNcBZM5SvbY",
                        subunit="1/3",
                        location="Busan, South Korea",
                        debut=datetime.date(2017, 2, 13)
                        )
        self.birthname_ch = "黃珈熙"


class KimLip(Member):

    def __init__(self):
        Member.__init__(self, "Kim Lip",
                        name_kr="김립",
                        birthname="Kim Jungeun",
                        birthname_kr="김정은",
                        birthday=datetime.date(1999, 2, 10),
                        zodiac="Aquarius",
                        bloodtype="B",
                        color="Red",
                        animal="Owl",
                        song="Eclipse",
                        song_url="https://www.youtube.com/watch?v=_qJEoSa3Ie0",
                        subunit="Odd Eye Circle",
                        debut=datetime.date(2017, 5, 15)
                        )


class Jinsoul(Member):

    def __init__(self):
        Member.__init__(self, "Jinsoul",
                        name_kr="진솔",
                        birthname="Jung Jinsol",
                        birthname_kr="정진솔",
                        birthday=datetime.date(1997, 6, 13),
                        zodiac="Gemini",
                        bloodtype="B",
                        color="Blue",
                        animal="Blue Betta",
                        song="Singing in the Rain",
                        song_url="https://www.youtube.com/watch?v=RWeyOyY_puQ",
                        subunit="Odd Eye Circle",
                        debut=datetime.date(2017, 6, 13)
                        )


class Choerry(Member):

    def __init__(self):
        Member.__init__(self, "Choerry",
                        name_kr="최리",
                        birthname="Choi Yerim",
                        birthname_kr="최예림",
                        birthday=datetime.date(2001, 6, 4),
                        zodiac="Gemini",
                        bloodtype="O",
                        color="Purple",
                        animal="Fruit Bat",
                        fruit="Cherry",
                        song="Love Cherry Motion",
                        song_url="https://www.youtube.com/watch?v=VBbeuXW8Nko",
                        subunit="Odd Eye Circle",
                        debut=datetime.date(2017, 7, 12)
                        )


class Yves(Member):

    def __init__(self):
        Member.__init__(self, "Yves",
                        name_kr="이브",
                        birthname="Ha Sooyoung",
                        birthname_kr="하수영",
                        birthday=datetime.date(1997, 4, 24),
                        zodiac="Gemini",
                        bloodtype="B",
                        color="Burgundy",
                        animal="Swan",
                        fruit="Apple",
                        song="new",
                        song_url="https://www.youtube.com/watch?v=LIDe-yTxda0",
                        subunit="YYXY",
                        debut=datetime.date(2017, 11, 14)
                        )


class Chuu(Member):

    def __init__(self):
        Member.__init__(self, "Chuu",
                        name_kr="츄",
                        birthname="Kim Jiwoo",
                        birthname_kr="김지우",
                        birthday=datetime.date(1999, 9, 20),
                        zodiac="Libra",
                        bloodtype="A",
                        color="Peach",
                        animal="Penguin",
                        fruit="Strawberry",
                        song="Heart Attack",
                        song_url="https://www.youtube.com/watch?v=BVVfMFS3mgc",
                        subunit="YYXY",
                        debut=datetime.date(2017, 12, 14)
                        )


class Gowon(Member):

    def __init__(self):
        Member.__init__(self, "Go Won",
                        name_kr="고원",
                        birthname="Park Chaewon",
                        birthname_kr="박채원",
                        birthday=datetime.date(2000, 11, 19),
                        zodiac="Scorpio",
                        bloodtype="A",
                        color="Eden Green",
                        animal="Butterfly",
                        fruit="Pineapple",
                        song="One&Only",
                        song_url="https://www.youtube.com/watch?v=m5qwcYL8a0o",
                        subunit="YYXY",
                        debut=datetime.date(2018, 1, 15)
                        )


class Olivia(Member):

    def __init__(self):
        Member.__init__(self, "Olivia Hye",
                        name_kr="올리비아혜",
                        birthname="Son Hyejoo",
                        birthname_kr="손혜주",
                        birthday=datetime.date(2001, 11, 13),
                        zodiac="Scorpio",
                        bloodtype="B",
                        color="Grey",
                        animal="Wolf",
                        fruit="Blood Plum",
                        song="Egoist",
                        song_url="https://www.youtube.com/watch?v=UkY8HvgvBJ8",
                        subunit="YYXY",
                        debut=datetime.date(2018, 3, 17)
                        )

    def roll(self):
        pass
