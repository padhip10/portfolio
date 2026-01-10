
import math

print("\n--- TASK 1: Square roots ---")
squares = [4, 9, 16, 25]
for value in squares:
    print(math.sqrt(value))

print("\n--- TASK 2: append next 3 squares ---")
squares.append(36)
squares.append(49)
squares.append(64)
squares.append(81)
print(squares)

print("\n--- TASK 3: extend() next squares (121,144,169) ---")
squares.extend([121, 144, 169])
print(squares)

print("\n--- TASK 4: insert 2 at beginning ---")
squares.insert(0, 2)
print(squares)


print("\n--- TASK 5: remove 49 ---")
squares.remove(49)
print(squares)


print("\n--- TASK 6: remove 3 (will error) ---")
try:
    squares.remove(3)
except Exception as e:
    print("Error:", e)

print("\n--- TASK 7: list with duplicates remove first 2 ---")
nums = [1, 2, 3, 1, 2]
nums.remove(2)
print(nums)

print("\n--- TASK 8: pop() last element ---")
popped = squares.pop()
print("Popped:", popped)
print("List now:", squares)


print("\n--- TASK 9: pop() first element ---")
popped_first = squares.pop(0)
print("Popped:", popped_first)
print("List now:", squares)


print("\n--- TASK 10: reverse() ---")
squares.reverse()
print(squares)

print("\n--- TASK 11: index of 'blue' ---")
colors = ["red", "green", "yellow", "blue", "red", "purple"]
print(colors.index("blue"))

print("\n--- TASK 12: copy() test ---")
copy_colors = colors.copy()
copy_colors.remove("purple")
print("Original:", colors)
print("Copy:", copy_colors)


print("\n--- LIST COMPREHENSIONS ---")
print("TASK: cubes 2–20")
cubes = [x**3 for x in range(2, 21)]
print(cubes)

print("\n--- CONDITION FOR some_users ---")
some_users = ["admin1", "superuser", "michael123", "tim", "anna22"]
short_names = [u for u in some_users if len(u) < 8]
print("Condition: usernames with length < 8")
print(short_names)

print("\n--- TUPLE TASKS ---")
address = ("12B", "Main Street", "AB12 3CD")
print("Address tuple:", address)

print("\nSingle element tuple test:")
single_tuple = ("hello",)
not_tuple = ("hello")
print(type(single_tuple), "(tuple)")
print(type(not_tuple), "(string)")

print("Unpacking address:")
a, b, c = address
print(a, b, c)

print("\nPrint tuple using * unpacking:")
print(*address)
print(address)

print("\n--- SORTING TASKS ---")
names = ["sam", "anna", "Sophie", "Eric"]

print("Default sort:", sorted(names))
print("Case-insensitive sort:", sorted(names, key=str.lower))

print("\nALL TASKS COMPLETE!")
