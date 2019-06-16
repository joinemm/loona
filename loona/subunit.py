import datetime
from loona.member import Member


class SubUnit:

    def __init__(self, name, **kwargs):
        self.name = name
        self.name_kr = kwargs.get('name_kr')
        self.debut = kwargs.get('debut')
        self.leaders = kwargs.get('leaders', [])
        self.members = kwargs.get('members', [])
        self.releases = kwargs.get('releases', [])
        self.concerts = kwargs.get('concerts', [])
        self.location = kwargs.get('location', [])

    def __str__(self):
        return self.name

    def add_member(self, member: Member):
        self.members.append(member)

    def add_leader(self, member: Member):
        self.leaders.append(member)

    def days_since_debut(self):
        return(datetime.date.today() - self.debut).days


class OneThird(SubUnit):

    def __init__(self):
        SubUnit.__init__(self, "LOONA 1/3",
                         name_kr="이달의 소녀 1/3",
                         debut=datetime.date(2017, 3, 12),
                         location=['New Zealand', 'Hong Kong'],
                         releases=['Love & Live (2017)', 'Love & Evil (2017)']
                         )


class OddEyeCircle(SubUnit):

    def __init__(self):
        SubUnit.__init__(self, "LOONA ODD EYE CIRCLE",
                         name_kr="이달의 소녀 오드아이써클",
                         debut=datetime.date(2017, 9, 21),
                         location=['Los Angeles, California'],
                         releases=['Mix & Match (2017)',
                                   'Loonatic (English Version) (2017)',
                                   'Max & Match (2017)']
                         )


class YYXY(SubUnit):

    def __init__(self):
        SubUnit.__init__(self, "LOONA yyxy",
                         name_kr="이달의 소녀 yyxy",
                         debut=datetime.date(2018, 5, 30),
                         location=['Szabadkígyós, Hungary'],
                         releases=['Beauty & The Beat (2018)']
                         )


class LOONA(SubUnit):

    def __init__(self):
        SubUnit.__init__(self, "LOONA",
                         name_kr="이달의 소녀",
                         debut=datetime.date(2018, 8, 20),
                         releases=['favOriTe (2018)', '[+ +] (2018)',
                                   'Orbit 1.0 (2018)', '[x x] (2019)'],
                         concerts=['LOONAbirth (2018)', 'LOONAVERSE (2019)']
                         )
        self.name_zh = '本月少女',
        self.name_ja = '今月の少女',

    def __repr__(self):
        return """Loona (stylized as LOOΠΔ) is a South Korean girl group
                  formed by Blockberry Creative. Its twelve members were
                  revealed in a periodic fashion, corresponding to their Korean
                  name Idarui Sonyeo (이달의 소녀), which translates to "Girl of
                  the Month".""".replace(
                  "\n", "").replace("                  ", " ")
