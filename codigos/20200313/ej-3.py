# while sin break para overflow
a=2.
while a*2.!=float('inf'):
	a=a*2.

print(a)

# while con break para overflow
a=2.
while 1:
	b=2*a
	if b==float('inf'):
		break
	else:
		a=b

print(a)

# while para ver que int tiene precision arbitraria
a=2.
a_int=2
while 1:
	b=2*a
	a_int=2*a_int
	if b==float('inf'):
		break
	else:
		a=b

a_int*2;print(a_int)

# while sin break para underflow
a=2.
while a/2.!=0.:
	a=a/2.

print(a)

# while con break para underflow
a=2.
while 1:
	b=a/2.
	if b==0.:
		break
	else:
		a=b

print(a)

# para chequear
import sys
sys.float_info
