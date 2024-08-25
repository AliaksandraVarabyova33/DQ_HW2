from random import randint, choice
from string import ascii_lowercase

# creating empty dicts
final_dict, tmp_dict = {}, {}

# creating list of dicts according to condition in the task (I limited number of pairs in one dict by 5 for testing purpose)
rand_list = [{choice(ascii_lowercase): randint(0, 100) for i in range(5)} for j in range(randint(2, 10))]

print(rand_list)

# creating var to get the index of dict
count = 0

# transforming from list of dicts into dict of dicts.
for dictionary in rand_list:
  count += 1
  for k, v in dictionary.items():
    #adding dict of values from different original dicts (keys) and dict indexes these values come from (values)  as a value
    tmp_dict.setdefault(k, {}).setdefault(v, count)

# selectin only the biggest value
for k, v in tmp_dict.items():
  #if in value more than one pair
  if len(v) > 1:
    #formatting key by adding "_" and getting dict index from max value, adding value as max key from the pairs
    final_dict[k + "_"+str(v.get(max(v)))] = max(v)
  #if it's only one pair than get the key from this pair
  else: final_dict[k] = next(iter(v.keys()))

print(final_dict)





