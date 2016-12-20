ip_numbers = [i for i in range(256)]
ip = input().split(".")
try:
	ip = list(map(int, ip))
	if (len(ip) == 4):
		if (ip[0] in ip_numbers and ip[1] in ip_numbers and ip[2] in ip_numbers and ip[3] in ip_numbers):
			print("YES")
		else:
			print("NO")
	else:
		print("NO")
except:
	print("NO")
