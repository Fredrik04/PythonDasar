#Mencocokan pola pada sebuah string
import re

text = "The quick brown fox jumps over the lazy dog"
match = re.search("fox",text)
if match:
    print("Match found!")
else:
    print("Match not found")
#Output: Match Found

