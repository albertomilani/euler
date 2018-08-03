
def is_inc (L):
  L = map(int, str(n))
  return all(x <= y for x, y in zip(L, L[1:]))

def is_dec (L):
  L = map(int, str(n))
  return all(x >= y for x, y in zip(L, L[1:]))

def is_bounce(L):
  return (not is_inc(L) and not is_dec(L))



n = 1
run = True
bounce = 0
not_bounce = 0
while run:
  if is_bounce(map(int, str(n))):
    bounce += 1
  else:
    not_bounce += 1
  ratio = float(bounce)/float(n)*100
  print n, ratio
  if ratio == 99:
    run = False
  n += 1

