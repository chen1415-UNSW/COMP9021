# Implements coding and decoding functions for pairs of integers.
# For coding, start at point (0, 0), move to point (1, 0), and turn
# around in an anticlockwise manner.
#
# Written by *** for COMP9021


from math import sqrt


def encode(a, b):
   
    if a>=b:
      if sqrt(a*a)> sqrt(b*b):
        num= ((a-1)*2+1)**2-(b+(a-1))
      else:
        num= (2*(-b)+1)**2-1+(a+b)
    else:
      if sqrt(a*a)>= sqrt(b*b):
        num= (a*2)**2-(a+b)
      else:
        num= (b*2)**2-(a+b)
    return num
def decode(n):
   
    base= int(sqrt(n))
    if base%2==1:
      if n<= base**2+base:
        a=(base+1)/2
        b=n-(base)**2-((base-1)/2)
      else:
        a=(base+1)/2-(n-base**2-base)
        b=(base+1)/2
    else:
      if n<= base**2+base:
        a=-base/2
        b=base/2-(n-base**2)
      else: 
        a=-base/2+n-base**2-base
        b=-base/2
    return int(a),int(b)


