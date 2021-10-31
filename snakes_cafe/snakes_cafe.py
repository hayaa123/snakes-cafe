menue={
    "Appetizers":["Wings","Cookies","Spring Rolls","Entrees"],
    "Entrees":["Salmon","Steak","Meat Tornado","A Literal Garden"],
    "Desserts":["Ice Cream","Cake","Pie"],
    "Drinks":["Coffee","Tea","Unicorn Tears"]
}
custom_order = []

def munue_printer():
    print("**************************************")
    print("**    Welcome to the Snakes Cafe!   **")
    print("**    Please see our menu below.    **")
    print("**")
    print('** To quit at any time, type "quit" **')
    print("**************************************")
    for type in menue.keys() : 
        print("")
        print (type)
        print("----------")
        for item in menue[type]:
            print(item)

def order (custom_order):
    
    print("**************************************")
    print("** What would you like to order? **")
    print("**************************************")
    orders = []
    for i in menue.values():
        orders+= i

    current_order = ""

    while current_order != "Quit":
        current_order = input(">").capitalize()
        if current_order in orders:
            custom_order.append(current_order)
            print(f"{custom_order.count(current_order)} order of {current_order} have been added to your meal")
        elif current_order =="Quit":
            print("exiting the program ...")
        else :
            print("sorry we dont have this dish in the menue")


def print_order (custom_order):
    print("")
    print("______________________")
    print("your order : ")
    print("")
    for item in set(custom_order):
        print(f"{custom_order.count(item)} order of {item} ")
    print()
    print("______________________")

if __name__ == "__main__":
    munue_printer()
    order(custom_order)
    print_order(custom_order)