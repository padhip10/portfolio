# ==========================================
# FOCP Lab Worksheet - Week 2
# FINAL CHECKED SOLUTION
# ==========================================

print("--- SECTION: WORKING WITH VARIABLES ---")

# TASK: Try inputting code and examine results
total = 100
print("The total is", total)

# TASK: Expression evaluation
total = total + 99
print("The total is now", total)

# TASK: Augmented assignment equivalent
total = 100  # Resetting for demonstration
total += 99
print("The total (using +=) is now", total)

# TASK: Replace assignment expressions with augmented assignment
# 1. total = total - 1
total -= 1
print("The total is", total)

# 2. total = total * 4
total *= 4
print("The total is", total)

# 3. total = total / 2
total /= 2
print("The total is", total)

# TASK: Extend code to create 'average' variable
total = 98.2
count = 5
average = total / count
print("The average is", average)


print("\n--- SECTION: DATA-TYPES ---")

# Examples from text (Dynamic Typing)
total = 10
print("Type of total (int):", type(total))
total = 10.5
print("Type of total (float):", type(total))
total = "10.5"
print("Type of total (string):", type(total))

# TASK: Use type() function on specific values
print("Type of False:", type(False))
print("Type of 1000:", type(1000))
print("Type of 100.111:", type(100.111))
print("Type of 'Hello':", type("Hello"))
print("Type of True:", type(True))
print("Type of 100 / 5:", type(100 / 5))
print("Type of 100 // 5:", type(100 // 5))

# Example: Addition vs Concatenation
print("10 + 10 result:", 10 + 10)
print("'10' + '10' result:", "10" + "10")

# TASK: What is the * operator doing to the string?
print("'ABC' * 10 result:", "ABC" * 10)


print("\n--- SECTION: CALLING BUILT-IN FUNCTIONS ---")

# TASK: Print name, address, contact, and length of name
my_name = "Student Name"
print("Name:", my_name)
print("Address: Leeds Beckett University")
print("Contact details: student@example.com")
print("Length of my name:", len(my_name))

# TASK: Input age (Demonstrating the error then the fix)
# The worksheet asks "Does this program work?". It fails without int().
# We implement the FIX as requested in the next paragraph of the worksheet.
print("\n[Input Required] Calculating Age...")
age_str = input("Enter your age: ")
age = int(age_str)  # The fix using int()
print("in one year your age will be", age + 1)

# TASK: Input two numeric values and display product
print("\n[Input Required] Calculating Product...")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("The product is", num1 * num2)


print("\n--- SECTION: SINGLE, DOUBLE AND TRIPLE QUOTES ---")

# TASK: Use double quotes for the assignment
comment = "I would have 'thought' you knew better!"
print(comment)

# TASK: Print text with special escape characters
# Required output: This text includes characters such as '\' '"' and "'",
print("This text includes characters such as '\\' '\"' and \"'\",")

# TASK: Print text with tabs and newlines
print("\tThis is a new line that starts with a tab")
print("\t\tThis new line starts with two tabs")

# TASK: Print the "Backslash Wall"
print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
print("Hello there!")
print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")

# TASK: Triple quoted string (Multi-line)
print("""This text spans three lines,
and includes both single ('),
and double quotes (").""")


print("\n--- SECTION: INDEXING AND SLICING ---")
surname = "Palin"

# TASK: Access 3rd letter (Index 2)
print("3rd letter:", surname[2])

# TASK: Access 10th letter (Index 9) - Error Handling
try:
    print(surname[9])
except IndexError as e:
    print("Error accessing 10th letter (Index 9):", e)

# TASK: Access second from last letter (Index -2)
print("Second from last letter:", surname[-2])

# Example: Slice [1:4]
print("Slice [1:4]:", surname[1:4])

# TASK: Slice all except first character
print("All except first:", surname[1:])

# TASK: Slice all except last character
print("All except last:", surname[:-1])


print("\n--- SECTION: INTRODUCING LISTS ---")

# Required List for testing
names = ["Terry", "John", "Michael", "Eric", "Terry", "Graham"]
primes = [2, 3, 5, 7, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

# TASK: Slice first four prime numbers
print("First four primes:", primes[0:4])

# Examples of List Mutation from text
names[0] = "Terry, G."
names[0:0] = ["Tim", "Bill", "Graeme"]
names.append("Brian")
names += ["Jacob"]
print("List after text examples:", names)

# TASK: Insert two new names just before the final name
# Reset list to clean state for this specific task
names = ["Terry", "John", "Michael", "Eric", "Terry", "Graham"]
names[-1:-1] = ["Tim", "Bill"]
print("List after inserting before final name:", names)

# Extra Check from text: "Try concatenating a string directly to a list"
try:
    print("Attempting to concatenate string to list...")
    test_list = [1, 2] + "string"
except TypeError as e:
    print("Error concatenating string to list:", e)

# TASK: List Multiplication
nums = [1, 2, 3] * 5
print("Nums list * 5:", nums)


print("\n--- SECTION: KEY TERMINOLOGY ---")
print("Assignment: Allocating a value to a variable name (e.g., x = 5).")
print("Data-type: The category of a value (e.g., int, str) defining its rules.")
print("Argument: A value provided to a function when calling it.")
print("Indexing: retrieving a single item from a sequence using its position.")
print("Slicing: retrieving a subset/range of items from a sequence.")
print("Mutable: An object that can be modified after creation (List).")
print("Immutable: An object that cannot be modified after creation (String).")

print("\n--- End of Assignment ---")