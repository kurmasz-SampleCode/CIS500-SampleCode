def sum_list_raw(lst):
    sum = 0
    index = 0
    list_len = len(lst)
    while index < list_len:
        sum = sum + lst[index]
        index += 1
    return sum

def sum_list(lst):
    sum = 0 
    for value in lst:
      sum += value;
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
    total = 0;
    for i in range(0, 10):
      total += lst[i % 10]
    return total 
