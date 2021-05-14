shoplist = ['apples', 'mango', 'bananas', 'onions']

print("I have to buy", len(shoplist), "items")

print("Items:", end=' ')
for item in shoplist:
    print(item, end=' ')

print("\nAlso I want to buy little rise.")
shoplist.append("rise")

print("Now my list to buy is:\n\t", shoplist)

print("I need to sort it.")
shoplist.sort()
print("Sortet list is:\n\t", shoplist)

print("First item is", shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print("I bought", olditem)
print("Now my list is:\n\t",shoplist)

