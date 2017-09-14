# Implements coding and decoding functions for pairs of integers.
# For coding, start at point (0, 0), move to point (1, 0), and turn
# around in an anticlockwise manner.
#
# Written by Hao for COMP9021


from math import sqrt


def encode(a, b):
        if abs(a) >= abs(b):
                n = abs(a)
        else:
                n = abs(b)
        min_value = (n*2 - 1)**2
        max_value = ((n+1)*2 - 1)**2 - 1
        Number1=max_value
        Number2=min_value
        Number3=min_value+2*n-1
        Number4=min_value+2*n-1+2*n
        Number5=min_value++2*n-1+4*n
        Number=0
        if (a==n and b==-n):
        	Number=max_value
        if (a==n and b==1-n):
        	Number=min_value
        if (a==n and b==n):
        	Number=min_value+2*n-1
        if (a==-n and b==n):
        	Number=min_value+2*n-1+2*n
        if (a==-n and b==-n):
        	Number=min_value++2*n-1+4*n

        if (a==n and b > 1-n and b<n):
        	Number = min_value + (b+n-1)
        if (a>-n and a<n and b==n):
        	Number = Number3 + (n-a)
        if (a==-n and b>-n and b<n):
        	Number = Number4 + (n-b)
        if (b==-n and a>-n and a<n):
        	Number = Number5 + (n-a)

        	
        return Number

def decode(n):
        cycle_value = int((sqrt(n)+1)/2)
        min_value = (cycle_value*2 - 1)**2
        max_value = ((cycle_value+1)*2 - 1)**2-1
        Number1 = min_value+2*cycle_value-1
        Number2 = min_value+2*cycle_value-1+2*cycle_value
        Number3 = min_value+2*cycle_value-1+4*cycle_value
        print(cycle_value)
        print(min_value)
        print(Number1)
        print(Number2)
        print(Number3)
        print(max_value)
        i=0
        j=0
        if n == min_value:
        	i=cycle_value
        	j=1-cycle_value
        	print('1')
        if n == Number1:
        	i=cycle_value
        	j=cycle_value
        	print('2')
        if n == Number2:
                i=-cycle_value
                j=cycle_value
                print('3')
        if n == Number3:
        	i=-cycle_value
        	j=-cycle_value
        	print('4')
        if n == max_value:
        	i=cycle_value
        	j=-cycle_value
        	print('5')
        if n > min_value and n <Number1:
        	i=cycle_value
        	j=1-cycle_value+(n - min_value)
        	print('6')
        if n>Number1 and n < Number2:
        	i=cycle_value-(n-Number1)
        	j=cycle_value
        	print('7')
        if n>Number2 and n < Number3:
        	i=-cycle_value
        	j=cycle_value-(n- Number2)
        	print('8')
        if n > Number3 and n<max_value:
        	i = -cycle_value+(n - Number3)
        	j = -cycle_value
        	print('9')

        return (i,j)
