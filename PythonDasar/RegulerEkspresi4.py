#mencari semua kemunculan pola pada sebuah string

import re
text = "The quick brown fox jumps over the lazy dog"
matches = re.findall("o", text)
print(matches)

#Output: ['o', 'o', 'o', 'o']