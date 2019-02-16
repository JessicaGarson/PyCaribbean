def hi():
    d1 >> play(P['AAJBAS'].bubble())
    d2 >> play(P['JOSS'].amen())
    d3 >> play('good afternoon')
    p3 >> rave()
    Clock.future(12, fun)
hi()

def fun():
    p1 >> bell([0, 8, 2])
    p2 >> dbass([-2, 3, 6])
    p4 >> arpy()
    Clock.future(9, hi)
fun()
