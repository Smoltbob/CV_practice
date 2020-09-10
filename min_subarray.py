def find_grants_cap(grantsArray, newBudget):
  low_cut = 0
  high_cut = max(grantsArray)
  cut = lambda value, array: [min(value, x) for x in array]
  pred = 0
  possible_budget = float('inf')
  while possible_budget != newBudget:
    cut_value = (low_cut + high_cut)/2

    print(cut_value)
    possible_budget = sum(cut(cut_value, grantsArray))

    if possible_budget > newBudget:
      high_cut = cut_value
    else:
      low_cut = cut_value
    
  return round(cut_value,2)
