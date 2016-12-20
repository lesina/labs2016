balance = 0
parenthesses = input()
for paren in parenthesses:
    if paren == '(':
        balance += 1
    else:
        balance -= 1
    if balance < 0:
        break
if balance == 0:
    print("YES")
else:
    print("NO")
