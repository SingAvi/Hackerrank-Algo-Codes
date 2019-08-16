string = "Avinash is a good boy avi"
text = "avi"

results = 0
sub_len = len(text)
for i in range(len(string)):
    if string[i:i+sub_len].lower() == text:
        results += 1
print (results)


s = string.lower().count(text)
print(s)

