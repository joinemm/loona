import loona.member
import loona.subunit
import loona.group

heejin = loona.member.Heejin()
hyunjin = loona.member.Hyunjin()
haseul = loona.member.Haseul()
yeojin = loona.member.Yeojin()
vivi = loona.member.Vivi()
kimlip = loona.member.KimLip()
jinsoul = loona.member.Jinsoul()
choerry = loona.member.Choerry()
yves = loona.member.Yves()
chuu = loona.member.Chuu()
gowon = loona.member.Gowon()
olivia = loona.member.Olivia()


def get_members():
    return [heejin, hyunjin, haseul, yeojin, vivi, kimlip, jinsoul, choerry, yves, chuu, gowon, olivia]


onethird = loona.subunit.OneThird()
oddeyecircle = loona.subunit.OddEyeCircle()
yyxy = loona.subunit.YYXY()


def get_subunits():
    return [onethird, oddeyecircle, yyxy]


fullgroup = loona.group.LOONA()


if __name__ == "__main__":
    pass
