
p1 >> pasha([2, 5, 6], attack=6)
p2 >> donk([0, -1, -5], amp=1.6)
p3 >> prophet([2, 5, 6], compress=1.5)
p4 >> space([0, 2, 5], decay=0.35)
b1 >> bass([0, -6, 5], pan=[2/5, 3/5, 1/2])
d1 >> play(P['AAJBAS'].bubble())
d2 >> play(P['JKS'].amen())
d3 >> play('C', dur=10)
