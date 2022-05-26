import math
import random

def isin(n):
  dedans=0
  tot=0
  for _ in range(n):
    x=random.uniform(0,math.pi)
    y=random.uniform(0,1)
    if y<=math.sin(x):
      dedans+=1
    tot+=1
  print(math.pi*dedans/tot)
