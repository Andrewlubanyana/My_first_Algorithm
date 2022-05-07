def binary_algo(list, target):
  first = 0
  last = len(list) - 1
  
  while first <= last
    midpoint = len(first + last) // 2
  if [midpoint] == target:
    return midpoint
  elif list [midpoint] < target:
    first = midpoint + 1
  else:
    last = midpoint - 1
    
    def verify(index):
 if index is not None:
    print ("Target found at index: ", index)
 else: 
    print("Target not found in list")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
results = binary_algo (numbers, 12)
verify(results)
