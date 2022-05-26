import math
import random

def icos(n):
  dedans=0
  tot=0
  for _ in range(n):
    x = random.uniform(0,math.pi/2)
    y = random.uniform(0,1)
    if y<math.cos(x):
      dedans+=1
    tot+=1
  return math.pi/2*dedans/tot
