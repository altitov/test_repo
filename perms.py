import itertools

def perms():
  ''' prints permutations of 0-5 if sum of elements equals 6 '''
  s = tuple(range(0, 6))
  l = list(itertools.permutations(s, 3))
  for p in l:
    if (sum(p)) == 6):
      print(a)

perms()
