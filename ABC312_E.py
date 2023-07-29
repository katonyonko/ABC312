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
4
0 0 0 1 1 1
0 0 1 1 1 2
1 1 1 2 2 2
3 3 3 4 4 4
3
0 0 10 10 10 20
3 4 1 15 6 10
0 9 6 1 20 10
8
0 0 0 1 1 1
0 0 1 1 1 2
0 1 0 1 2 1
0 1 1 1 2 2
1 0 0 2 1 1
1 0 1 2 1 2
1 1 0 2 2 1
1 1 1 2 2 2
"""

def solve(test):
  N=int(input())
  ans=[0]*N
  box=[list(map(int, input().split())) for _ in range(N)]
  ans=[set() for _ in range(N)]
  tmp=[-1]*(100**3)
  def idx(x,y,z):
    return x*100**2+y*100+z
  for i in range(N):
    x1,y1,z1,x2,y2,z2=box[i]
    for x in range(x1,x2):
      for y in range(y1,y2):
        for z in range(z1,z2):
          tmp[idx(x,y,z)]=i
  for x in range(100):
    for y in range(100):
      for z in range(100):
        if tmp[idx(x,y,z)]==-1: continue
        if x>0 and tmp[idx(x-1,y,z)]!=-1:
          ans[tmp[idx(x,y,z)]].add(tmp[idx(x-1,y,z)])
        if x<99 and tmp[idx(x+1,y,z)]!=-1:
          ans[tmp[idx(x,y,z)]].add(tmp[idx(x+1,y,z)])
        if y>0 and tmp[idx(x,y-1,z)]!=-1:
          ans[tmp[idx(x,y,z)]].add(tmp[idx(x,y-1,z)])
        if y<99 and tmp[idx(x,y+1,z)]!=-1:
          ans[tmp[idx(x,y,z)]].add(tmp[idx(x,y+1,z)])
        if z>0 and tmp[idx(x,y,z-1)]!=-1:
          ans[tmp[idx(x,y,z)]].add(tmp[idx(x,y,z-1)])
        if z<99 and tmp[idx(x,y,z+1)]!=-1:
          ans[tmp[idx(x,y,z)]].add(tmp[idx(x,y,z+1)])
  for i in range(N): ans[i].discard(i)
  if test==0:
    for i in range(N): print(len(ans[i]))
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