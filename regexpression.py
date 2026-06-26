# Regular Expressions In python:-----------------------------------


# findall--- searches the string and returns all the matches in a list
# search--- searches the string and returns the first match as a match object
#split--- splits the string based on the pattern and returns a list of substrings
#sub----- replaces the matches with a specified string
#finditer---- returns an iterator yielding match objects for all matches in the string
"""
import re 

# 1. Sample text to analyze
text = "Contact us at support@example.com or sales@example.org today."

# 2. Define a regex pattern for emails
# \w+ matches letters/digits, @ matches literal '@', \w+ matches domain, \.[a-z]+ matches .com/.org
email_pattern = r"\w+@\w+\.[a-z]+"

# 3. Find ALL matches in the text
emails = re.findall(email_pattern, text)
print("Extracted Emails:", emails)

# 4. Search for the FIRST occurrence and get its position
match_obj = re.search(email_pattern, text)
if match_obj:
    print(f"First email found: '{match_obj.group()}' at position {match_obj.span()}")

# 5. Replace all emails with masked text
masked_text = re.sub(email_pattern, "[MASKED_EMAIL]", text)
print("Masked Text:", masked_text)

"""
# Given a string with a lot of indian phone numbers starting from +91
"""import re

patt = re.compile(r"(\+91[\-\s]?)?[0]?(91)?[789]\d{9}")
mystr = {"91-9876543210", "+91 98765 43210", "09876543210", "9876543210", "+919876543210"}
matches = patt.finditer(mystr)
for match in matches:
    print(match)"""

#findall() function---

"""import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
"""
#search() function---
"""
import re
txt = "The rain in Spain"
x = re.search("\s", txt)
print("The first white-space character is located in position:", x.start())
x.start()"""

#split() function---

import re
txt = "the rain in spain"
x=re.split("\s", txt)
print(x)

# sub() function---

import re
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)