def bisect(a, x, lo=0, hi=None):
  if lo < 0:
    raise ValueError('lo must be non-negative')
  if hi is None:
    hi = len(a)
  while lo < hi:
    mid = (lo + hi) // 2
    if a[mid] < x:
      lo = mid + 1
    else:
      hi = mid
  return lo

mylist = [1, 2, 3, 7, 9, 11, 34]
print(bisect(mylist, 3))

from bisect import bisect_left, bisect_right
mylist = [1, 2, 3, 5, 5, 6, 61, 88, 889]
x = 3

print(f"bisect_left: {bisect_left(mylist, x)}") #2
print(f"bisect_right: {bisect_right(mylist, x)}") #61
