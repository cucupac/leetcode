from collections import Counter

s = "bat"
t = "tab"


if Counter(s) == Counter(t):
    print(True)
else:
    print(False)
