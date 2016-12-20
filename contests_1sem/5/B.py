def Capitalize(S):
	res = S.split(" ")[0]
	res = res[0].upper() + res[1:].lower()
	for word in S.split(" ")[1:]:
		res += " " + word[0].upper() + word[1:].lower()
	return res

a = input()
print(Capitalize(a))
