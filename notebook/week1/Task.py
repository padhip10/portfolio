# --- TASK: First Code Execution ---
print("the program has executed")

# --- TASK: Alternative Messages ---
print("This is the second message")
print("Python programming is interesting")
print("I am completing my FOCP assignment")

# --- TASK: Using Command History ---
# (Simulating recalling a previous command)
print("This is the second message")

# --- TASK: Getting Help ---
# Note: Interactive help() is commented out because it blocks script execution.
# help()
# help(print)
# help(input)
print("Help command tasks completed (viewed manually).")

# --- TASK: Entering Basic Expressions ---
print("45 + 20 =", 45 + 20)

# --- TASK: Common Operators ---
print("10 + 20 - 15 =", 10 + 20 - 15)
print("10 * 5 =", 10 * 5)
print("100 / 33 =", 100 / 33)       # Standard Division
print("100 // 33 =", 100 // 33)     # Floor Division
print("10 ** 2 =", 10 ** 2)         # Exponentiation
print("10 % 3 =", 10 % 3)           # Modulus

# --- TASK: Operator Precedence (Part 1) ---
print("10 + 5 * 2 =", 10 + 5 * 2)
print("10 - 5 * 10 + 5 =", 10 - 5 * 10 + 5)
print("5 * 10 ** 2 =", 5 * 10 ** 2)

# --- TASK: Operator Precedence (Part 2 - Parentheses) ---
print("(10 + 5) * 2 =", (10 + 5) * 2)
print("10 - 5 * (10 + 5) =", 10 - 5 * (10 + 5))
print("(5 * 10) ** 2 =", (5 * 10) ** 2)

# --- TASK: Nested Parentheses ---
print("12 + (5 * 2 + 3) =", 12 + (5 * 2 + 3))
print("12 + (5 * (2 + 3)) =", 12 + (5 * (2 + 3)))

# --- TASK: Handling Errors ---
# 1. Syntax Error Task: "10 +"
# This line is commented out because a Syntax Error prevents the file from running.
# 10 +

# 2. Runtime Error Task: Division by Zero
# Wrapped in try-except so the script continues running for you.
try:
    print("Ten divided by zero is", 10/0)
except ZeroDivisionError as e:
    print("Error encountered:", e)

# --- TASK: Key Terminology Definitions ---
print("\n--- Key Terminology Definitions ---")
print("Source code: Human-readable code written by the programmer.")
print("Machine code: Binary code (0s and 1s) executed by the CPU.")
print("Interpreter: Translates and runs code line-by-line (e.g., Python).")
print("Compiler: Translates all code into an executable file before running.")
print("Executable: A file ready to run on an OS (e.g., .exe).")
print("Expressions: Combinations of values and operators that evaluate to a result.")
print("Operators: Symbols that perform operations (+, -, *, /).")
print("Operands: The values/variables the operator acts on.")
print("Syntax Errors: Grammar mistakes preventing the program from starting.")
print("Logical Errors: Mistakes in logic causing wrong results or crashes.")

# --- TASK: Quitting ---
print("\nEnd of assignment tasks.")
quit()