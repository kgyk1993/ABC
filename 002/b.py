import re

W = raw_input().strip()
print re.sub(r"[aeiou]", "", W)
