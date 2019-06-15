import datetime


class Group:

    def __init__(self, name, **kwargs):
        self.name = name
        self.name_kr = kwargs.get('name_kr')
        self.name_zh = kwargs.get('name_zh')
        self.name_ja = kwargs.get('name_ja')
        self.debut = kwargs.get('debut')
        self.leaders = kwargs.get('leaders')
        self.members = kwargs.get('members')
        self.releases = kwargs.get('releases')
        self.concerts = kwargs.get('concerts')

    def __call__(self):
        return """Loona (stylized as LOOΠΔ) is a South Korean girl group formed by Blockberry Creative.
                Its twelve members were revealed in a periodic fashion, corresponding to their Korean 
                name Idarui Sonyeo (이달의 소녀), which translates to "Girl of the Month"."""
    
    def DaysSinceDebut(self):
        return(datetime.date.today() - self.debut).days

class LOONA(Group):
    
    def __init__(self):
        Group.__init__(self, "LOONA",
                        name_kr="이달의 소녀",
                        name_zh='本月少女',
                        name_ja='今月の少女',
                        debut=datetime.date(2018, 8, 20),
                        leaders='Haseul, Kim Lip, Yves',
                        members='Heejin, Hyunjin, Haseul, Yeojin, ViVi, Kim Lip, Jinsoul, Choerry, Yves, Chuu, Go Won, Olivia Hye',
                        releases='favOriTe (2018), [+ +] (2018), Orbit 1.0 (2018), [x x] (2019)',
                        concerts='LOONAbirth (2018), LOONAVERSE (2019)'
                        )