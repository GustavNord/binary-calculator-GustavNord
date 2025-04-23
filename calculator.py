import math
def b(b,B,o):
 E="Error";O="Overflow";t=0;T=0;l=len(b)-1
 for i,d in enumerate(b):
  v=2**(l-i)
  if d=="1":t+=v
  elif d!="0":return E
 L=len(B)-1
 for I,D in enumerate(B):
  V=2**(L-I)
  if D=="1":T+=V
  elif D!="0":return E
 if o=="+":h=t+T
 elif o=="-":h=t-T
 elif o=="/":
  if B=="00000000":return"NaN"
  h=math.floor(t/T)
 elif o=="*":h=t*T
 else:return E
 if h>255 or h<0:return O
 r="00000000";R=list(r)
 if h==0:return r
 if h>=128:R[0]="1";h-=128
 if h>=64:R[1]="1";h-=64
 if h>=32:R[2]="1";h-=32
 if h>=16:R[3]="1";h-=16
 if h>=8:R[4]="1";h-=8
 if h>=4:R[5]="1";h-=4
 if h>=2:R[6]="1";h-=2
 if h>=1:R[7]="1";h-=1
 return''.join(R)
