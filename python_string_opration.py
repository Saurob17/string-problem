
'''
Here’s a structured index for your code snippets with numbering, allowing you to easily reference each section. Each entry includes the section number and a brief description of what the code does.

### Index of String Operations in Python

1. **String Creation and Basic Operations**
   - Create a string and access characters.
   - Slice strings.

2. **String Length**
   - Calculate the length of a string.

3. **String Concatenation**
   - Concatenate multiple strings.

4. **String Repetition**
   - Repeat a string multiple times.

5. **String Methods**
   - (a) Changing Case
   - (b) Searching for substrings
   - (c) Counting occurrences
   - (d) f-Strings
   - (e) Replace substrings

6. **String Splitting and Joining**
   - (a) Splitting strings
   - (b) Joining strings

7. **String Trimming (Removing Whitespaces)**
   - Remove leading and trailing whitespaces.

8. **String Checking Methods**
   - Check if strings are alphabetical, digits, or alphanumeric.

9. **String Formatting**
   - (a) Old-style formatting using `%`
   - (b) `format()` method
   - (c) f-Strings

10. **Reversing a String**
    - (a) Using slicing
    - (b) Using the `reversed()` function
    - (c) Using a loop
    - (d) Using recursion

11. **String Comparison**
    - Compare two strings lexicographically.

12. **Escape Characters**
    - Use escape characters in strings.

13. **Multiline Strings**
    - Create and print multiline strings.

14. **Sorting Words Lexicographically**
    - Sort words in a string and print as a single string.

15. **Sorting Words by Length**
    - Sort words by length and print as a string.

16. **Sorting in Reverse Order by Length**
    - Sort words by length in reverse order.

17. **Case-Insensitive and Length Sorting Together**
    - Sort words by length and lexicographically (case-insensitively).

18. **Adding Characters in a Specific Range**
    - Remove characters between specified indices.

19. **Removing Characters from a Specific Range**
    - Remove characters from specified indices.

20. **Replacing Characters in a Specific Range**
    - Replace characters in a specified range with a new string.

---

'''
#1. String Creation and Basic Operations

# Create a string
'''
my_string = "Hello, World!"

# Access characters
print(my_string[0])  # H
print(my_string[-1])  # !

# Slice strings
print(my_string[0:5])  # Hello
print(my_string[7:])  # World!

'''

#2. String Length
'''

# Length of string
length = len(my_string)
print(length)  # 13

'''
#3. String Concatenation
'''
# String concatenation
greeting = "Hello"
name = "Alice"
message = greeting + ", " + name + "!"
print(message)  # Hello, Alice!

'''
#4. String Repetition
'''
# Repeat string
repeat_string = "Hi! " * 3
print(repeat_string)  # Hi! Hi! Hi! 

'''
#5. String Methods

#(a) Changing Case
'''
my_string = "Hello, World!"
print(my_string.upper())  # HELLO, WORLD! #all letter upper case
print(my_string.lower())  # hello, world! #all letter lower case

print(my_string.capitalize())  # Hello, world! #just first latter capital
print(my_string.title())  # Hello, World! # eanh word first latter capital

'''
#(b) Searching
'''
print(my_string.find("World"))  # 7 (index where 'World' starts)
print(my_string.find("Python"))  # -1 (not found)
{
substring_position = my_string.find("Python")
if substring_position != -1:
    print("Substring found at index:", substring_position)
else:
    print("Substring not found.")
}

print(my_string.index("World"))  # 7 (raises ValueError if not found) #it's gavin error value
{
try:
    substring_position = my_string.index("Python")
    print("Substring found at index:", substring_position)
except ValueError:
    print("Substring not found.")

}

'''
#(c) Counting
'''
my_string="lssdjls how how how"
print(my_string.count("how"))  # 3 (counts occurrences of 'how')

'''

#(c) f-Strings (Python 3.6+)
'''
name = "Alice"
age = 30
message = f"Hello, {name}. You are {age} years old."
print(message)  # Hello, Alice. You are 30 years old.

'''
#(d) Replace
'''
my_string = "Hello, World! World"
new_string = my_string.replace("World", "Python")
print(new_string)  # Output: Hello, Python! python
'''


#6. String Splitting and Joining

#(a) Splitting
'''
my_string = "Hello, World! sdlsdjlsdk , nsdkjls kkkd"
words = my_string.split(", ")
print(words)  # ['Hello', 'World!']

'''
'''
import re
my_string="lsdk skd kdjfls sld , dfjlsk, sdk"
words = re.split(r',\s*', my_string)  # This splits at a comma followed by 0 or more spaces
#The split(", ") method divides the string at the comma followed by a space, and the resulting parts are stored in the list words.
print(words)
'''
#b) Joining
'''
my_string = "Hello, World! sdlsdjlsdk , nsdkjls kkkd"
words = my_string.split(", ")
joined_string = "-".join(words)
print(joined_string)  # Hello-World!
'''
#7. String Trimming (Removing Whitespaces)
'''
whitespace_string = "  Hello, World!  "
print(whitespace_string.strip())  # "Hello, World!" (removes leading and trailing whitespaces)
print(whitespace_string.lstrip())  # "Hello, World!  " (removes leading whitespaces)
print(whitespace_string.rstrip())  # "  Hello, World!" (removes trailing whitespaces)
'''

#8. String Checking Methods
'''
my_string = "Hello World"
print(my_string.isalpha())  # False (not all characters are alphabets due to spaces and punctuation)
print("Hello".isalpha())  # True

print(my_string.isdigit())  # False (not all characters are digits)
print("12345".isdigit())  # True

print(my_string.isalnum())  # False (not all characters are alphanumeric) (alpha numaric meance number and digit)
print("Hello123".isalnum())  # True

'''
#9. String Formatting

#(a) Old-style formatting using %
'''
age = 25
message = "I am %d years old" % age
print(message)  # I am 25 years old

'''
#(b) format() Method
'''
message = "Hello, {}. You are {} years old.".format("Alice", 30)
print(message)  # Hello, Alice. You are 30 years old.
'''
#(c) f-Strings (Python 3.6+)
'''
name = "Alice"
age = 30
message = f"Hello, {name}. You are {age} years old."
print(message)  # Hello, Alice. You are 30 years old.
'''
#10. Reversing a String 
#a. Using Slicing
'''
my_string = "Hello World"
reversed_string = my_string[::-1]
print(reversed_string)  # !dlroW ,olleH
'''

#b. Using the reversed() Function
'''
my_string = "Hello, World!"
reversed_string = ''.join(reversed(my_string))
print(reversed_string)  # Output: !dlroW ,olleH
'''

##c. Using a Loop
'''
my_string = "Hello, World!"
reversed_string = ""
for char in my_string:
    reversed_string = char + reversed_string  # prepend the character
print(reversed_string)  # Output: !dlroW ,olleH
'''
#d. Using Recursion
'''
def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])
my_string = "Hello, World!"
reversed_string = reverse_string(my_string)
print(reversed_string)  # Output: !dlroW ,olleH
'''

#11. String Comparison
'''
string1 = "apple"
string2 = "banana"
print(string1 == string2)  # False
print(string1 < string2)  # True (compares lexicographically)
'''
# 12. Escape Characters
'''
escape_string = "He said, \"Python is fun!\""
print(escape_string)  # He said, "Python is fun!"

'''
#13. Multiline Strings
'''
multi_line_string = """This is
a multiline
string."""
print(multi_line_string)
# This is
# a multiline
# string.

'''
#14string word sort laxiagrafically and print as a string
'''
sentence = "apple orange banana grape"
words = sentence.split()  # Split the sentence into words
sorted_words = sorted(words)  # Sort the list of words lexicographically
print(words) #asa list ['apple', 'orange', 'banana', 'grape'] 
sorted_sentence = ' '.join(sorted_words)  # Join the sorted words back into a single string
print(sorted_sentence)  # Output: 'apple banana grape orange'

'''
#15Sorting Words by Length and Printing as a String
'''
sentence = "apple orange banana grape kiwi"
words = sentence.split()  # Split the sentence into words
sorted_words = sorted(words, key=len)  # Sort words by length
sorted_sentence = ' '.join(sorted_words)  # Join the sorted words back into a single string
print(sorted_sentence)  # Output: 'kiwi apple grape orange banana'
'''
#16Sorting in Reverse Order by Length:
'''
sentence = "apple orange banana grape kiwi"
words = sentence.split()
sorted_words = sorted(words, key=len, reverse=True)  # Sort by length in reverse order
sorted_sentence = ' '.join(sorted_words)

print(sorted_sentence)  # Output: 'banana orange apple grape kiwi'
'''
#17Case-Insensitive and Length Sorting Together:
#This will first sort the words by their length,
# and if two words have the same length, it will then sort them lexicographically (case-insensitively).
'''
sentence = "Banana apple Orange grape kiwi"
words = sentence.split()
sorted_words = sorted(words, key=lambda x: (len(x), x.lower()))  # Sort by length, then alphabetically
sorted_sentence = ' '.join(sorted_words)

print(sorted_sentence)  # Output: 'kiwi apple grape Banana Orange'
'''
#18 Adding Characters in a Specific Range
'''
my_string = "Hello Beautiful World"
start_index = 6
end_index = 15

'''
# Remove characters between start_index and end_index

#192. Removing Characters from a Specific Range
'''
my_string = "Hello Beautiful World"
start_index = 6
end_index = 15
new_string = my_string[:start_index] + my_string[end_index:]

print(new_string)  # Output: "Hello World"
'''
#. Replacing Characters in a Specific Range
'''
my_string = "Hello Beautiful World"
start_index = 6
end_index = 15
replacement = "Wonderful"

# Replace characters between start_index and end_index with 'replacement'
new_string = my_string[:start_index] + replacement + my_string[end_index:]

print(new_string)  # Output: "Hello Wonderful World"

'''

