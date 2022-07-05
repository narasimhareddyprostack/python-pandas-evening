prices = [599,99,499,1999,4999,5999,799]
new_Prices = list(filter(lambda x:x<1000, prices))


print(prices)
print(new_Prices)