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

# PL----------------------------------------------------------

goscie = 19
element_menu = "biryani"
element_menu2 = "pizza"

print("Stare menu to: " + element_menu)
print("Nowe menu to: " + element_menu2)

biryani_na_osobe = 1
potrzebne_biryani = biryani_na_osobe * goscie
przygotowane_biryani = 20
wystarczajaco_biryani = przygotowane_biryani == potrzebne_biryani
goscie += 1
biryani_na_goscia = przygotowane_biryani // goscie
print(biryani_na_goscia)
