a=input("zadaj meno 1. cloveka:")
am=float(input("zadaj vahu 1. cloveka:"))
b=input("zadaj meno 2. cloveka:")
bm=float(input("zadaj vahu 2. cloveka:"))
c=input("zadaj meno 3. cloveka:")
cm=float(input("zadaj vahu 3. cloveka:"))
P = (am+bm+cm)/3

print('priemerna vaha je:', P)

if am > P:
    print("a nadpriemernu vahu ma", a)
elif bm > P:
    print("a nadpriemernu vahu ma", b)
elif cm > P:
    print('a nadpriemernu vahu ma', c)
else:
    print('gratulujem nikto nie je tucny')


