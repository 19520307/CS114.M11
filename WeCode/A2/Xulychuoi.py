s = input()

na = "aoyeui"

s = s.lower()

result = ""
for i in range(0,len(s)):
    if(na.find(s[i]) == -1):
        result = result + "." + s[i]

print(result)
