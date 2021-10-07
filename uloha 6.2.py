
a=input("zadaj meno 1. cloveka:")
am=float(input("zadaj vahu 1. cloveka:"))
b=input("zadaj meno 2. cloveka:")
bm=float(input("zadaj vahu 2. cloveka:"))
c=input("zadaj meno 3. cloveka:")
cm=float(input("zadaj vahu 3. cloveka:"))
P = (am+bm+cm)/3


text = 'a nadpriemernu vahu ma'

if am > P:
    text += ' ' +a
elif bm > P:
    text += ' ' +b
elif cm > P:
    text += ' ' +c
else:
    print('gratulujem nikto nie je tucny')

print('priemerna vaha je:', P, text)




"""
x=1
y=2
print(x)
x += y
print(x)
print(y)
"""

