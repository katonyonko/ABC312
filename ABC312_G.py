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
5
1 2
2 3
2 4
1 5
6
1 2
2 3
3 4
4 5
5 6
12
1 6
3 4
10 4
5 9
3 1
2 3
7 2
2 12
1 5
6 8
4 11
"""

def dfs(G,r=0):
    used=[False]*len(G)
    parent=[-1]*len(G)
    st=[]
    st.append(r)
    while st:
        x=st.pop()
        if used[x]==True:
            continue
        used[x]=True
        for v in G[x]:
            if v==parent[x]:
                continue
            parent[v]=x
            st.append(v)
    return parent

def EulerTour(G, s):
    depth=[-1]*len(G)
    depth[s]=0
    done = [0]*len(G)
    Q = [~s, s] # 根をスタックに追加
    parent=[-1]*len(G)
    ET = []
    left,right=[-1]*len(G),[-1]*len(G)
    while Q:
        i = Q.pop()
        if i >= 0: # 行きがけの処理
            done[i] = 1
            ET.append(i)
            for a in G[i][::-1]:
                if done[a]: continue
                depth[a]=depth[i]+1
                parent[a]=i
                Q.append(~a) # 帰りがけの処理をスタックに追加
                Q.append(a) # 行きがけの処理をスタックに追加
        else: # 帰りがけの処理
            ET.append(i)
    for i in range(len(G)*2):
      if ET[i]>=0 and left[ET[i]]==-1: left[ET[i]]=i
      if ET[~i]<0 and right[~ET[~i]]==-1: right[~ET[~i]]=len(G)*2-i-1
    return ET, left, right, depth, parent #(right-left+1)//2がその頂点を含む部分木の大きさ

def solve(test):
  N=int(input())
  G=[[] for _ in range(N)]
  for _ in range(N-1):
    a,b=map(int,input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
  ET, left, right, depth, parent=EulerTour(G,0)
  size=[(right[i]-left[i]+1)//2 for i in range(len(G))]
  ans=N*(N-1)*(N-2)//6
  for i in range(N):
    now,acc=0,0
    for v in G[i]:
      if v==parent[i]:
        now=N-size[i]
      else:
        now=size[v]
      ans-=now*acc
      acc+=now
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