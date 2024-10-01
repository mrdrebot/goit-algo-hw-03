import random

def get_numbers_ticket(min, max, quantity):
 random_numbers_list = []
 total_random_quantity = 0
 
 if min < 0 or max > 1000:
  return result
  
 random_numbers_set = set()
 
 while total_random_quantity < quantity:
  random_number = random.randint(min, max + 1) #max + 1, add max number in the range of random numbers
  random_numbers_set.add(random_number)
  total_random_quantity = len(list(random_numbers_set))
  
 random_numbers_list = list(random_numbers_set)
 random_numbers_list.sort()
 return random_numbers_list
  
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)