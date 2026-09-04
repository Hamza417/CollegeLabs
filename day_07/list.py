items = [10, 20, 30]
print(f"Initial list:       {items}")

# append(x) - Adds single item to the end
items.append(40)
print(f"1. append(40):      {items}")  # [10, 20, 30, 40]

# extend(iterable) - Unpacks and appends iterable
items.extend([50, 60])
print(f"2. extend([50, 60]): {items}")  # [10, 20, 30, 40, 50, 60]

# insert(index, x) - Inserts x at index, shifts right
items.insert(2, 25)
print(f"3. insert(2, 25):   {items}")  # [10, 20, 25, 30, 40, 50, 60]

# count(x) - Returns frequency (read-only)
freq_20 = items.count(20)
print(f"4. count(20):       {freq_20}")  # 1

# index(x) - Returns first index of x (read-only)
idx_30 = items.index(30)
print(f"5. index(30):       {idx_30}")  # 3

# remove(x) - Removes first occurrence of x
items.remove(25)
print(f"6. remove(25):      {items}")  # [10, 20, 30, 40, 50, 60]

# pop([index]) - Removes & returns item (default: last)
popped_last = items.pop()
print(f"7. pop():           popped={popped_last}, remaining={items}")  # 60 removed

popped_first = items.pop(0)
print(f"   pop(0):          popped={popped_first}, remaining={items}")  # 10 removed

# reverse() - Reverses list in-place
items.reverse()
print(f"8. reverse():       {items}")  # [50, 40, 30, 20]

# sort() - Sorts list in-place
items.sort()
print(f"9. sort():          {items}")  # [20, 30, 40, 50]

# copy() - Returns shallow copy
shallow = items.copy()
print(f"10. copy():         {shallow} (is clone: {shallow is not items})")

# clear() - Removes all elements
items.clear()
print(f"11. clear():        {items}")  # []
