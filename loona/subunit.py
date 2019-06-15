import datetime


class SubUnit:

    def __init__(self, name, **kwargs):
        self.name = name
        self.name_kr = kwargs.get('name_kr')
        self.debut = kwargs.get('debut')
        self.leader = kwargs.get('leader')
        self.members = kwargs.get('members')
        self.releases = kwargs.get('releases')

    def days_since_debut(self):
        return(datetime.date.today() - self.debut).days


class OneThird(SubUnit):
    
    def __init__(self):
        SubUnit.__init__(self, "LOONA 1/3",
                         name_kr="이달의 소녀 1/3",
                         debut=datetime.date(2017, 3, 12),
                         leader='Haseul',
                         members='Heejin, Hyunjin, Haseul, ViVi',
                         releases='Love & Live (2017), Love & Evil (2017)'
                         )


class OddEyeCircle(SubUnit):

    def __init__(self):
        SubUnit.__init__(self, "LOONA ODD EYE CIRCLE",
                         name_kr="이달의 소녀 오드아이써클",
                         debut=datetime.date(2017, 9, 21),
                         leader='Kim Lip',
                         members='Kim Lip, Jinsoul, Choerry',
                         releases='Mix & Match (2017), Loonatic (English Version) (2017), Max & Match (2017)'
                         )


class YYXY(SubUnit):

    def __init__(self):
        SubUnit.__init__(self, "LOONA yyxy",
                         name_kr="이달의 소녀 yyxy",
                         debut=datetime.date(2018, 5, 30),
                         leader='Yves',
                         members='Yves, Chuu, Go Won, Olivia Hye',
                         releases='Beauty & The Beat (2018)'
                         )
