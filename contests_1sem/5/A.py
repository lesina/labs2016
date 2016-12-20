x = 0
y = 0
text = input().split(" ")
while (text[0] != "Treasure!"):
	if text[0] == "South":
		y -= int(text[1])
	elif text[0] == "North":
		y += int(text[1])
	elif text[0] == "East":
		x += int(text[1])
	elif text[0] == "West":
		x -= int(text[1])
	text = input().split(" ")
print(x, y)
