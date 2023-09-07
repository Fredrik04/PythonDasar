#membuat pola yang lebih kompleks

import re
text = "The quick brown fox jumps over the lazy dog"
match = re.search("[Tt]he [a-z]+", text)
if match:
    print(match.group())

#Output: The quick