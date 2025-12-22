# --- Exercise 1: two-sum ---
print("--- Ex 1 ---")
num1 = 10
num2 = 5
sum_result = num1 + num2
print(f"Sum: {sum_result}")

# --- Exercise 2: reverse-string ---
print("\n--- Ex 2 ---")
text = "Python"
reversed_text = text[::-1]
print(f"Reversed: {reversed_text}")

# --- Exercise 3: string-length ---
print("\n--- Ex 3 ---")
sample_str = "Hello World"
length = len(sample_str)
print(f"Length: {length}")

# --- Exercise 4: concatenate-string ---
print("\n--- Ex 4 ---")
str1 = "Hello"
str2 = "World"
concatenated = str1 + " " + str2
print(f"Concatenated: {concatenated}")

# --- Exercise 5: is-vowel ---
print("\n--- Ex 5 ---")
char = 'a'
is_vowel = char.lower() in 'aeiou'
print(f"Is '{char}' a vowel? {is_vowel}")

# --- Exercise 6: swap-first-last ---
print("\n--- Ex 6 ---")
original = "bridge"
if len(original) > 1:
    modified = original[-1] + original[1:-1] + original[0]
else:
    modified = original
print(f"Swapped: {modified}")

# --- Exercise 7: to-uppercase ---
print("\n--- Ex 7 ---")
lower_str = "hello"
upper_str = lower_str.upper()
print(f"Uppercase: {upper_str}")

# --- Exercise 8: rectangle-area ---
print("\n--- Ex 8 ---")
length = 10
width = 5
area = length * width
print(f"Area: {area}")

# --- Exercise 9: is-even ---
print("\n--- Ex 9 ---")
number = 42
is_even = (number % 2 == 0)
print(f"Is {number} even? {is_even}")

# --- Exercise 10: extract-first-three ---
print("\n--- Ex 10 ---")
long_str = "Programming"
first_three = long_str[:3]
print(f"First three: {first_three}")

# --- Exercise 11: string-interpolation ---
print("\n--- Ex 11 ---")
name = "Alex"
age = 25
message = f"My name is {name} and I am {age} years old."
print(message)

# --- Exercise 12: string-slicing ---
print("\n--- Ex 12 ---")
slice_source = "0123456789"
# Indices 2 to 5 inclusive means strictly [2:6] in Python slicing
sliced = slice_source[2:6] 
print(f"Sliced (2-5): {sliced}")

# --- Exercise 13: type-conversion ---
print("\n--- Ex 13 ---")
num_str = "123"
num_int = int(num_str)
print(f"Converted integer: {num_int}")

# --- Exercise 14: string-repetition ---
print("\n--- Ex 14 ---")
repeat_me = "Ha"
repeated = repeat_me * 3
print(f"Repeated: {repeated}")

# --- Exercise 15: calculate-quotient-remainder ---
print("\n--- Ex 15 ---")
dividend = 17
divisor = 5
quotient = dividend // divisor
remainder = dividend % divisor
print(f"Quotient: {quotient}, Remainder: {remainder}")

# --- Exercise 16: float-division ---
print("\n--- Ex 16 ---")
f_num1 = 10
f_num2 = 4
f_result = f_num1 / f_num2
print(f"Float division: {f_result}")

# --- Exercise 17: string-methods ---
print("\n--- Ex 17 ---")
count_source = "banana"
char_to_count = "a"
count = count_source.count(char_to_count)
print(f"Occurrences of '{char_to_count}': {count}")

# --- Exercise 18: escape-sequences ---
print("\n--- Ex 18 ---")
escaped_str = "She said, \"Hello!\""
print(escaped_str)

# --- Exercise 19: multi-line-string ---
print("\n--- Ex 19 ---")
multiline = """Line one
Line two
Line three"""
print(multiline)

# --- Exercise 20: exponentiation ---
print("\n--- Ex 20 ---")
base = 2
exponent = 3
power_result = base ** exponent
print(f"2 to the power of 3 is: {power_result}")

# 💎 Exercise 21: palindrome (without loops)
print("\n--- Ex 21 ---")
palindrome_word = "racecar"
is_palindrome = (palindrome_word == palindrome_word[::-1])
print(f"Is '{palindrome_word}' a palindrome? {is_palindrome}")

# 💎 Exercise 22: check-anagrams
print("\n--- Ex 22 ---")
word1 = "Listen"
word2 = "Silent"
# Sort characters and compare (ignoring case)
are_anagrams = sorted(word1.lower()) == sorted(word2.lower())
print(f"Are '{word1}' and '{word2}' anagrams? {are_anagrams}")