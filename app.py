from pizzapi import *

print("Hello, we need some information")
f = input("First Name: ")
l = input("Last Name: ")
e = input("Email Address: ")
p = input("Phone Number: ")
s = input("State Code [Example: CO, CA, WA, DC, etc]: ")
c = input("City: ")
z = input("Zip Code: ")
a = input("Street Address: ")

addr = Address(a, c, s, z)
cust = Customer(f, l, e, p)
store = addr.closest_store()
order = Order(store, cust, addr)

print("\n\nNow time to get your menu!")
menu = store.get_menu()

ordr_true = False
while(ordr_true == False):
    srch = input("search items: ")
    menu.search(Name=srch)
    add = input("Add item [example: 20BCOKE]:")
    order.add_item(add)
    isdone = input("you done? [y/n]")
    if (isdone == 'y' or isdone == 'Y'):
        ordr_true = True
        continue
    else:
        ordr_true = False

print("Time for credit card information!")
cc1 = input("Your card number [the 16 numbers on the front of your card]: ")
cc2 = input("Expiration Date [example 1121 instead of 11/21]: ")
cc3 = input("Your card CCV [the 3/4 numbers on the back]: ")

card = PaymentObject(cc1, cc2, cc3, z)
order.place(card)