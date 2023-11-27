def sum_list(lst):
    sum = 0 
    for value in lst:
      sum += value
    return sum


def sum_list_raw(lst):
    sum = 0
    index = 0
    list_len = len(lst)
    while index < list_len:
        sum = sum + lst[index]
        index += 1
    return sum

def multiply_list(lst):
    sum = 1 
    for value in lst:
      sum *= value;
    return sum


def location_of_max(lst):
    loc_of_max = 0;
    for index, value in enumerate(lst):
      if (lst[index] > lst[loc_of_max]):
        loc_of_max = index
    return loc_of_max

def fast_mode(lst):
    loc = location_of_max(lst);  # O(n)
    max_value = lst[loc]
    count = [0] * (max_value + 1)
    print(count)

    for val in lst:
        count[val] += 1

    return location_of_max(count) # !! Be careful  count.length != array.length

def slow_mode(lst):
    max_count = 0
    max_value = lst[0]

    for value_to_count in lst:
      local_count = 0
      for val in lst:
        if (val == value_to_count):
            local_count += 1

        if (local_count > max_count):
            max_count = local_count
            max_value = value_to_count
    return max_value

# print(slow_mode([15, 10, 5, 20, 10, 16]))

def linear_search(findMe, lst):
    for index, value in enumerate(lst):
        if (value == find_me):
            return index
    return -1; # -1 means "NOT FOUND"


def trick1(lst):
    total = 0
    for i in range(0, 10):
      total += lst[i % len(lst)]
    return total 

def trick2(lst):
    total = 0
    for i in range(0, len(lst)):
      if (i % 2 == 0):
        total += location_of_max(lst)
      else:
        total += lst[i]
    return total

def trick3(lst):
    total = 0
    for i in range(0, len(lst)):
      if (i == len(lst) / 2):
        total += location_of_max(lst)
      else:
        total += lst[i]
    return total

print(trick3([2, 4, 6, 8, 10]))



def meet_everybody_v1(people): # List of People objects
    for p1 in people:
      for p2 in people:
        if p1 != p2:
          p1.meet(p2)

def meet_everybody_v2(people):
    for index1 in range(0, len(people)):
     for index2 in range(index1 +1, len(people)):
        people[index1].meet(people[index2]);
