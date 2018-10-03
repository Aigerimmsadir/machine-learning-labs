import scipy.linalg
from numpy import sin, exp
#сложная функция
def f(x):
    return  sin(x / 5) * exp(x / 10) + 5 * exp(-x / 2)
# значение функции на точках 1 и 15.
b1 = [f(1), f(15)]
# многочлен первой степени. 
x=2

a1f,a1s=[],[]
# в цикле добавляю в оба массива текущую степень едигицы т пятнадцати
for i in range (0,x):
    a1f.append(1**i)
    a1s.append(15**i)
# соеденили их
a1=[a1f,a1s]

# многочлен 2 степени
x=3

a2f,a2s,a2t=[],[],[]

for i in range (0,x):
    a2f.append(1**i)
    a2s.append(8**i)
    a2t.append(15**i)
# соеденили их
a2=[a2f,a2s,a2t]
# значение функции на точках 1,8 и 15.
b2 = [f(1), f(8), f(15)]



# многочлен 3 степени
x=4
a3f,a3s,a3t,a3fo=[],[],[],[]
for i in range (0,x):
    a3f.append(1**i)
    a3s.append(4**i)
    a3t.append(10**i)
    a3fo.append(15**i)
# соеденили их
a3=[a3f,a3s,a3t,a3fo]
# значение функции на точках 1,4,10 и 15.
b3 = [f(1), f(4), f(10), f(15)]


answer = scipy.linalg.solve(a3, b3)
print(answer)