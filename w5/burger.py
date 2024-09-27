from functools import wraps
import time
import random

def timethis(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    start = time.perf_counter()
    r = func(*args, **kwargs)
    end = time.perf_counter()
    print('{}.{} : {}'.format(func.__module__, func.__name__, end - start))
    return r
  return wrapper

d={'B':0.5,'C':0.8,'P':1.5,'V':0.7,'O':0.4,'M':0.9}

def calc(s):
  tot=0
  for w in s:
    tot+=d[w]
  return tot

def check_age():
  num =1
  age = int(input("Enter age:"))
  if age <1 or age > 100:
    num += 1
  else:
    print("Your age is ",age)
    print("Number of attempts=",num)

def prime_factors(n):
  cnt=0
  r=n
  for i in range(2,n+1):
    if is_prime(i) and r%i==0:
      cnt+=i
      while r%i==0:
        r//=i
    if r==1:
      break
  return cnt

def max3(a, b, c):
  if compare(a,b)==1:
    return a if compare(a,c)==1 else c
  return b if compare(b,c)==1 else c

def is_anagram(s1, s2):
  s1,s2=s1.lower(),s2.lower()
  if len(s1)!=len(s2):
    return False
  dic={}
  for i in range(len(s1)):
    if s1[i] in dic:
      dic[s1[i]]+=1
    else:
      dic[s1[i]]=1
    if s2[i] in dic:
      dic[s2[i]]-=1
    else:
      dic[s2[i]]=-1
  for x in dic.values():
    if x!=0:
      return False
  return True

@timethis
def binom_coeff(n, k):
  k=min(k,n-k)
  b=[[0]*(k+1),[0]*(k+1)]
  cur,last=1,0;b[0][0]=1
  for i in range(1,n+1):
    for j in range(0,min(k+1,i+1)):
      b[cur][j]=1 if j==0 else b[last][j-1]+b[last][j]
    cur,last=1-cur,1-last
  return b[last][k]

def binom_coeff_recur(n, k):
  return 1 if k==0 or n==k else binom_coeff_recur(n-1,k)+binom_coeff_recur(n-1,k-1)

@timethis
def birec(n,k):
  return binom_coeff_recur(n,k)


# You can assume that we have run "import random" in Coursemology.
# You SHOULD NOT add any import statements!

def monte_carlo_pi(n):
  r=1000;k=0
  for _ in range(n):
    x,y=random.uniform(-r,r),random.uniform(-r,r)
    if x*x+y*y<=r*r:
      k+=1
  return 4*k/n

def occurrence(s1, s2):
  l1,l2=len(s1),len(s2)
  i,ans=0,0
  while i<l1-l2+1:
    if s1[i:i+l2]==s2:
      ans+=1
      i+=l2
    else:
      i+=1
  return ans

def stern_brocot(n):
  seq=[(0,1),(1,1)]
  for _ in range(n):
    nseq=[]
    for i in range(len(seq)-1):
      nseq+=[seq[i],(seq[i][0]+seq[i+1][0],seq[i][1]+seq[i+1][1])]
    nseq+=[seq[-1]]
    seq=nseq
  return seq

def luhn(num):
    s,i=0,0
    while num:
        n=(num%10)*(1 if i%2 else 2)
        if n>9:
            n=n%10+n//10
        s+=n
        num//=10
        i+=1
    return (10-(s%10))%10

def R(n):
  rs=[0,1,3,7]
  ss=[0,2,4,5,6]
  if n<4:
    return rs[n]
  for t in range(4,n+1):
    rs+=[rs[t-1]+ss[t-1]]
    ss+=[i for i in range(rs[-2]+1,rs[-1])]
  return rs[n]

def sum_digit_square_I(n):
    res=0
    while n:
        res+=(n%10)**2
        n//=10
    return res

def sum_digit_square_R(n):
    return 0 if n==0 else (n%10)**2+sum_digit_square_R(n//10)
    
def is_happy_number(n):
    return n==1 or n==7 if n<10 else is_happy_number(sum_digit_square_I(n))
    
def all_happy_number(n,m):
    t,d=m,0
    while t:
        t//=10
        d+=1
    li=[2]*(max(m,81*d)+1)
    for i in range(1,10):
        li[i]=1 if i==1 or i==7 else 0
    def check(k):
        if li[k]==2:
            li[k]=check(sum_digit_square_I(k))
        return li[k]
    return [i for i in range(n,m+1) if check(i)]

def is_unique(seq):
  while seq:
    for p in seq[1:]:
      if seq[0]==p:
        return False
    seq=seq[1:]
  return True

def rotate(bouquet,step):
  step%=len(bouquet)
  return bouquet[step:]+bouquet[:step]

def flower_I(bouquet, k):
  s=""
  while bouquet:
    bouquet=rotate(bouquet,k)
    s+=bouquet[-1]
    bouquet=bouquet[:-1]
  return s

def flower_R(bouquet, k):
  return bouquet[(k-1)%len(bouquet)]+flower_R(rotate(bouquet,k)[:-1],k) if bouquet else ""

def pink_rose(bouquet):
  idx=[i for i in range(len(bouquet)) if bouquet[i]=='P']
  def compute(n,k):
    return 0 if n==1 else (compute(n-1,k)+k)%n
  if idx:
    k=1
    while compute(len(bouquet),k) not in idx:
      k+=1
    return k
  else:
    return -1

flowers_r_us = [("R", 5, 3), ("R", 3, 2), ("W", 4, 3), ("W", 2, 2), ("P", 3, 4)]

def make_bouquet(shop, number):
  n=len(shop)
  for i in range(n):
    for j in range(i+1,n):
      for k in range(j+1,n):
        if shop[i][0]!='P' and shop[j][0]!='P' and shop[k][0]!='P':
          continue
        if shop[i][1]+shop[j][1]+shop[k][1]==number:
          return True
  return False

def minimum_cost(shop, number):
  n,mi=len(shop),-1
  for i in range(n):
    for j in range(i+1,n):
      for k in range(j+1,n):
        if shop[i][0]!='P' and shop[j][0]!='P' and shop[k][0]!='P':
          continue
        if shop[i][1]+shop[j][1]+shop[k][1]==number:
          mi=min(mi if mi!=-1 else 999999,shop[i][2]+shop[j][2]+shop[k][2])
  return mi


def paint_area(S, C, D):
  n=10000 ###############
  def chk(x,y,s,t,r):
    return (x-s)**2+(y-t)**2<r**2
  S/=2;C/=2;D/=2
  d,m=S-D,0
  for _ in range(n):
    x,y=random.uniform(-S,S),random.uniform(-S,S)
    if chk(x,y,0,d,D) or chk(x,y,d,0,D) or chk(x,y,0,-d,D) or chk(x,y,-d,0,D):
      if not chk(x,y,0,0,C):
        m+=1
  return (m/n)*S*S*4