
def trova():
  f = open ( 'grid.dat' , 'r')
  mat = [ map(int,line.split()) for line in f ]
  print mat

trova()

