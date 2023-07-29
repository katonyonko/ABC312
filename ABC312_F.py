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
8 4
0 6
0 6
1 3
1 5
1 15
2 1
2 10
2 100
5 5
1 5
1 5
1 5
1 5
1 5
12 6
2 2
0 1
0 9
1 3
1 5
1 3
0 4
2 1
1 8
2 1
0 1
0 4
"""

def solve(test):
  N,M=map(int,input().split())
  X=[list(map(int,input().split())) for _ in range(N)]
  F,H,K=[],[],[]
  for t,x in X:
    if t==0: F.append(x)
    elif t==1: H.append(x)
    else: K.append(x)
  F.sort(reverse=True)
  H.sort(reverse=True)
  K.sort(reverse=True)
  F2=[0]+list(accumulate(F))
  H2=[0]+list(accumulate(H))
  K2=[0]+list(accumulate(K))
  ans=0
  for h in range(len(H)+1):
    k=bisect_left(K2,h)
    if k==len(K2): continue
    f=M-h-k
    if f<0: continue
    if f>len(F): f=len(F)
    ans=max(ans,F2[f]+H2[h])
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