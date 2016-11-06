import itertools

def perms():
  s = tuple(range(0, 6))
  l = list(itertools.permutations(s, 3))
  for p in l:
    if (sum(p)) == 6):
      print(a)

perms()
