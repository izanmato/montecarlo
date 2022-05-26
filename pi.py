import math
import random

def ipi(n):
  dedans=0
  tot=0
  for _ in range(n):
    x = random.uniform(0,1)
    y = random.uniform(0,1)
    if x**2+y**2<=1:
      dedans+=1
    tot+=1
  return 4*dedans/tot
