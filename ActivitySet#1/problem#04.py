hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter the Rate:")
x = float(rate)
if h <= 40:
  pay = h*x
 	print(pay)
else h > 40:
	print(pay+ (h-40)*1.5*x)