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
19 18
###......###......
###......###......
###..#...###..#...
..............#...
..................
..................
......###......###
......###......###
......###......###
.###..............
.###......##......
.###..............
............###...
...##.......###...
...##.......###...
.......###........
.......###........
.......###........
........#.........
9 21
###.#...........#.###
###.#...........#.###
###.#...........#.###
....#...........#....
#########...#########
....#...........#....
....#.###...###.#....
....#.###...###.#....
....#.###...###.#....
18 18
######............
######............
######............
######............
######............
######............
..................
..................
..................
..................
..................
..................
............######
............######
............######
............######
............######
............######
"""

def solve(test):
  N,M=map(int,input().split())
  S=[input() for _ in range(N)]
  def judge(i,j):
    if i+8>=N or j+8>=M: return False
    res=True
    for k in range(3):
      for l in range(3):
        if S[i+k][j+l]=='.': res=False
        if S[i+k+6][j+l+6]=='.': res=False
    for k in range(4):
      if S[i+3][j+k]=='#': res=False
      if S[i+k][j+3]=='#': res=False
      if S[i+5+k][j+5]=='#': res=False
      if S[i+5][j+5+k]=='#': res=False
    return res
  for i in range(N):
    for j in range(M):
      if judge(i,j): print(i+1,j+1)

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