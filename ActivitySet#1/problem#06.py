def computepay(h,r):
  if h < 40:
    pay = (h*r)
  else:
    pay = (40-h) * 1.5 * r + (40*r)
  return pay 

hrs=float(input("Enter hrs : "))

rate=float(input("Enter rate :"))


pay = computepay(hrs,rate)
print(pay)
  
    

