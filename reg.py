import re
with open("t.txt", "r") as F:
    find_all = re.findall(r"\b\w*z...z\w*\b", F.read())
print(find_all)

