
def hcf(x, y):
   
	while(y):
		x, y = y, x % y        

	return x

z = hcf(50, 75)
print(z)