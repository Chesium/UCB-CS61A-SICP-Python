def twice(f):
  def result(*args):
    f(*args)
    f(*args)
  return result

@twice
def printn5(n):
  print('5'*n)

