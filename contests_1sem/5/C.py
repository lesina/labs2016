time, day = input().split(" ")
time = time.split(":")
if day[0] == "p":
	if time[0] == "12":
		print(int(time[0]), ":", time[1], sep = "")
	else:
		print(int(time[0])+12, ":", time[1], sep = "")
else:
	if time[0] == "12":
		print("0", int(time[0])-12, ":", time[1], sep = "")
	elif (len(time[0]) == 1):
		print("0", int(time[0]), ":", time[1], sep = "")
	else:
		print(int(time[0]), ":", time[1], sep = "")

