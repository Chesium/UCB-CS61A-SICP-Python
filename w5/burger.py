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