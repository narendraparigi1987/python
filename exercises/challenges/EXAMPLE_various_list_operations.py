L1 = [2,1,3]
L2 = [4,5,6]
L3 = L1 + L2
print L3
L1.extend([0,6])
print L1

L = [2,1,3,6,3,7,0]
print L
L.remove(2)
print L
L.remove(3)
print L
del(L[1])
print L
print(L.pop())

s = "I<3 cs"
print(list(s))
print(s.split('<'))
L = ['a', 'b', 'c']
print(''.join(L))
print('_'.join(L))

L=[9,6,0,3]
print(sorted(L))
L.sort()
L.reverse()