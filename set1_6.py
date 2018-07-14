a=int(input())
b=int(input())
c=int(input())
if(a<0) and (b<0) and (c<0):
 print(max(a,b,c))
else:
 if(a>=b) and (a>=c):
  print(a)
 elif(b>=a) and (a>=c):
  print(b)
 else:
  print(c)
