middle_element = [5,2,-10,-4,4,5]
def middle_element(lst):
  if len(lst) % 2 == 0:
    return (lst[-3] + lst[-4]) / 2
  else:
    i = (round(len(lst) / 2)) - 1
    return lst[i]
print('the middle element is: ')
print(middle_element([5, 2, -10, -4, 4, 5]))