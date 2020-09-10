def find_pairs_with_given_difference(arr, k):
  sol = []
  for y in arr:
    for x in arr:
      if x == y + k:
        sol.append([x,y])
  return sol

def find_pairs_with_given_difference(arr, k):
  if k == 0:
    return []
  
  hashes = {}
  answer = []
  
  for x in arr:
    hashes[x-k] = x
    
  for y in arr:
    if y in hashes.keys():
      answer.append([hashes[y], y])
      
  return answer
  
