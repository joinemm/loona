import loona.member
import loona.subunit

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

group = loona.subunit.LOONA()
group.add_leader(haseul)
group.add_leader(kimlip)
group.add_leader(yves)
group.add_member(heejin)
group.add_member(haseul)
group.add_member(hyunjin)
group.add_member(vivi)
group.add_member(kimlip)
group.add_member(jinsoul)
group.add_member(choerry)
group.add_member(chuu)
group.add_member(gowon)
group.add_member(olivia)


def get_members():
    return group.members


onethird = loona.subunit.OneThird()
onethird.add_leader(haseul)
onethird.add_member(heejin)
onethird.add_member(haseul)
onethird.add_member(hyunjin)
onethird.add_member(vivi)

oddeyecircle = loona.subunit.OddEyeCircle()
oddeyecircle.add_leader(kimlip)
oddeyecircle.add_member(kimlip)
oddeyecircle.add_member(jinsoul)
oddeyecircle.add_member(choerry)

yyxy = loona.subunit.YYXY()
yyxy.add_leader(yves)
yyxy.add_member(chuu)
yyxy.add_member(gowon)
yyxy.add_member(olivia)


def get_subunits():
    return [onethird, oddeyecircle, yyxy]


if __name__ == "__main__":
    pass
