import io
import sys
import pdb
from collections import defaultdict, deque, Counter
from itertools import permutations, combinations, accumulate
from heapq import heappush, heappop
sys.setrecursionlimit(10**6)
from bisect import bisect_right, bisect_left
from math import gcd
import math

_INPUT = """\
6
(???(?
)))))
??????????????(????????(??????)?????????(?(??)
"""

def solve(test):
  S=input()
  mod=998244353
  dp=[0]*(len(S)+1)*3001
  def idx(i,j):
    return i*3001+j
  dp[idx(0,0)]=1
  for i in range(len(S)):
    for j in range(3001):
      if S[i]=="(":
        if j!=0:
          dp[idx(i+1,j)]=dp[idx(i,j-1)]
      elif S[i]==")":
        if j!=3000:
          dp[idx(i+1,j)]=dp[idx(i,j+1)]
      else:
        if j!=0:
          dp[idx(i+1,j)]+=dp[idx(i,j-1)]
        if j!=3000:
          dp[idx(i+1,j)]+=dp[idx(i,j+1)]
        dp[idx(i+1,j)]%=mod
  ans=dp[idx(len(S),0)]
  if test==0:
    print(ans)
  else:
    return None

def random_input():
  from random import randint,shuffle
  N=randint(1,10)
  M=randint(1,N)
  A=list(range(1,M+1))+[randint(1,M) for _ in range(N-M)]
  shuffle(A)
  return (" ".join(map(str, [N,M]))+"\n"+" ".join(map(str, A))+"\n")*3

def simple_solve():
  return []

def main(test):
  if test==0:
    solve(0)
  elif test==1:
    sys.stdin = io.StringIO(_INPUT)
    case_no=int(input())
    for _ in range(case_no):
      solve(0)
  else:
    for i in range(1000):
      sys.stdin = io.StringIO(random_input())
      x=solve(1)
      y=simple_solve()
      if x!=y:
        print(i,x,y)
        print(*[line for line in sys.stdin],sep='')
        break

#0:提出用、1:与えられたテスト用、2:ストレステスト用
main(0)