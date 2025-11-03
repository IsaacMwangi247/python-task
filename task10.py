# prods = [[‘omo’,’30kshs’,’300’], [‘milk’,’50kshs’,’200’],[‘bread’,’45kshs’,’359’], [‘coffee’,’5kshs’,’79’]]
prods = [["omo", "30kshs", 300], ["milk", "50kshs", 200],["bread", "45kshs", 359], ["coffee","5kshs", 79]]
print(prods[0][-1])
# total stock 
total_stock = int(prods[0][-1]) + int(prods[1][-1]) + int(prods[2][-1]) + int(prods[3][-1])
print(total_stock)