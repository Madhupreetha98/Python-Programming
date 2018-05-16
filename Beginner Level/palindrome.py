rev=0,rem
n=int(raw_input())
while n>0 && n<=1000:
rem=n%10
rev=rem*10+rem
n=n/10
if rev==n:
print("yes")
else:
print("no")

