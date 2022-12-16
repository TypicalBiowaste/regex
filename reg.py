import re
with open("t.txt", "r") as F:
    find_all = re.findall(r"\b\w*z...z\w*\b", F.read())
print(find_all)

echo "# regex" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/TypicalBiowaste/regex.git
git push -u origin main