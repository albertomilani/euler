
def triangolare(n):
  return n*(n+1)/2

def fattori(n):

  k = 2
  k_max = int(n/2)
  fattori = [1]
  while k < k_max:
    if (n % k) == 0:
      fattori.append(k)
    k += 1
  fattori.append(n)
  return fattori

def trova():

  n = 2
  n_fattori = fattori(triangolare(n))
  while len(n_fattori) < 500:
    t = triangolare(n)
    n_fattori = fattori(t)
    print t, len(n_fattori)
    n += 1
  
  return t


print trova()

