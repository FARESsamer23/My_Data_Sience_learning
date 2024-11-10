#pythex.org
#regulare expressions =>  quantifiers
"""
Basic Syntax:

.  Matches any character except a newline.
^  Matches the start of a string.
$  Matches the end of a string.
*  Matches zero or more repetitions of the preceding element.
+  Matches one or more repetitions of the preceding element.
?  Matches zero or one repetition of the preceding element (makes it optional).
{n}  Matches exactly n repetitions of the preceding element.
{n, m}  Matches between n and m repetitions.
[^a-z] => any non a-z ta3ni not

Character Classes:

\d  Matches any digit (equivalent to [0-9]).
\D  Matches any non-digit.
\w  Matches any alphanumeric character (letters, digits, underscore).
\W  Matches any non-alphanumeric character.
\s  Matches any whitespace (spaces, tabs, newlines).
\S  Matches any non-whitespace character.
Grouping and Alternation:

(abc)  Groups characters as a single unit. You can refer to the matched group later.
|  Alternation, or "or" (e.g., cat|dog matches either "cat" or "dog").
Anchors:

\b Word boundary.
\B  Non-word boundary.
\. bah yahsebha fan
\ escapeing  el fayda t3o bah ya3taber symbol dakhel fe regulaire expre
"""
# Basic match:

import re
pattern = r"\d{3}-\d{2}-\d{4}"  # Pattern for matching SSN format
text = "My number is 123-45-6789."
match = re.search(pattern, text)
if match:
    print("Match found:", match.group())

#Find all occurrences:


text = "Call me at 123-456-7890 or 987-654-3210."
phone_numbers = re.findall(r"\d{3}-\d{3}-\d{4}", text)
print("Phone numbers found:", phone_numbers[0])

#Replace text: replace fox with dog 
text = "The quick brown fox."
new_text = re.sub(r"fox", "dog", text)
print(new_text)  # Output: "The quick brown dog."

#Split by pattern:
text = "apple, banana,    cherry"
fruits = re.split(r",\s*", text)
print(fruits)  # Output: ['apple', 'banana', 'cherry']
