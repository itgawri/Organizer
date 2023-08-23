guests = 19
menu_item = "biryani"
menu_item2 = "pizza"

print("Old menu is: " + menu_item)
print("New menu is: " + menu_item2)

biryani_per_person = 1
biryani_needed = biryani_per_person * guests
biryani_prepared = 20
enough_biryani = biryani_prepared == biryani_needed
guests += 1
biryani_per_guest = biryani_prepared // guests
print(biryani_per_guest)