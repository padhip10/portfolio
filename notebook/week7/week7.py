import math

print("===== INTRODUCING SETS =====")

names = {"John", "Eric", "Terry", "Michael", "Graham", "Terry"}
print("Names set:", names)

names_constructor = set(["John", "Eric", "Terry", "Michael", "Graham", "Terry"])
print("Names using constructor:", names_constructor)

hex_letters = set("abcdef")
print("Hex letters:", hex_letters)

empty_set = set()
print("Empty set:", empty_set)


print("\n===== SET COMPREHENSIONS =====")

sentence = "this is a sentence containing some letters"

unique_letters = {x for x in sentence}
print("Unique letters (with spaces):", unique_letters)

unique_letters_no_space = {x for x in sentence if x != " "}
print("Unique letters (no spaces):", unique_letters_no_space)


print("\n===== SET MEMBERSHIP TEST =====")

name = "Alex"
if name not in names:
    print(name, "is NOT listed in the set of known names")


print("\n===== SET OPERATIONS (METHODS) =====")

staff = {"Pete", "Kelly", "Jon", "Paul", "Sally", "Sue"}
directors = {"Kelly", "Rupert", "Cyril", "Jon"}

staff = staff.union({"Mark", "Ringo"})
print("Union:", staff)

staff_directors = staff.intersection(directors)
print("Intersection:", staff_directors)

external = directors.difference(staff)
print("Difference:", external)

staff_or_external = directors.symmetric_difference(staff)
print("Symmetric Difference:", staff_or_external)


print("\n===== SET MUTATOR METHOD =====")

vowels = set({"a", "e", "i"})
vowels.update({"o", "u"})
print("Updated vowels:", vowels)


print("\n===== SET COMPARISONS (METHODS) =====")

managers = {"Kelly", "Jon", "Paul", "Sally", "Sue"}

if managers.issubset(staff):
    print("All managers are staff members")

if staff.issuperset(managers):
    print("Staff is a superset of managers")


print("\n===== IMMUTABLE SET (FROZENSET) =====")

suits = frozenset({"heart", "club", "spade", "diamond"})
print("Frozenset suits:", suits)

print({"club", "diamond"}.issubset(suits))


print("\n===== INTRODUCING DICTIONARIES =====")

stock = {"apple": 10, "banana": 15, "orange": 11}
print("Initial stock:", stock)

stock["kiwi"] = 10
print("After adding kiwi:", stock)

print("Banana stock level:", stock["banana"])


print("\n===== DICTIONARY COMPREHENSION =====")

roots = {n: math.sqrt(n) for n in range(1, 26)}
print("Roots dictionary:", roots)


print("\n===== DICTIONARY METHODS =====")

removed_item = stock.popitem()
print("Removed item:", removed_item)
print("Stock after popitem:", stock)


print("\n===== ITERATING OVER DICTIONARIES =====")

print("Stock keys:")
for item in stock:
    print(item)

print("\nStock values:")
for level in stock.values():
    print(level)

print("\nStock items:")
for item, level in stock.items():
    print(item, "has a stock level of", level)


print("\n===== ITERATING OVER ROOTS DICTIONARY =====")

for num, sqrt in roots.items():
    print(f"The square root of {num} is {sqrt}")


print("\n===== END OF WEEK 7 LAB =====")
