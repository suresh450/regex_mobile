import re
n=input('enter mobile number')
regex=r'[6-9]\d\d\d\d\d\d\d\d\d'
print("findall -- '%s' --'%s' "%(regex,n))
match=re.findall(regex,n)
if match:
	print("valid mobile number:",match)
else:
	print("not a valid mobile number")
