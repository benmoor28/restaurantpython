from array import array

def enque(a, b, c, d):
    try:
        int(a)
        int(b)
        int(c)
        int(d)
    except:
        return "\nAn error occured, a number was not entered"
    orders.append[[a,b,c,d]]
    return i + " " + "order added successfully"

def deque():
    x = orders.pop(0)
    return x

def view_que():
    orderlist = ""
    if len(orders) == 0:
        return "No orders are in the que."
    else:
        for i in range(len(orders)):
            orderlist += " " + str(i) + ") " + orders[i] + " "
        return orderlist

def resource_allo():
    r = {}
    r1 = {}
    r2 = {}
    r3 = {}

    for i in range(len(orders)):
        r.update({"c" + i: orders[i][0]})
    
    batch = []

    batch_numbers = list(r)

    y = 0

    # review batch number thing
    
    for i in range(len(batch_numbers)):
        y += batch_numbers[i]
        if y > 12:
            cooker.append(batch)
            batch = []
            break
        else:
            batch.append("c"+i)
        

orders = []
orderlist = ""
cooker = []



while True:
    try:
        option = input("""

Select an option:

1) Enque an order
2) Deque order
3) View que

>""")
        if option == "1":
            chicken = input("How much e-chicken was ordered? ")
            burger = input("How much c-burger was ordered? ")
            chips = input("How much la-fries was ordered? ")
            eggy = input("How much eggy-bread was ordered? ")
            print(enque(chicken, burger, chips, eggy))
        elif option == "2":
            confirm = input("The order: " + orders[0] + "will be removed. Continue? Y/N ")
            if confirm.lower() == "y":
                deque()
            elif confirm.lower() == "n":
                print("Order will stay first in the que.")
            else:
                print("Erronous option was recieved, order will not be cancelled.")
        elif option == "3":
            print(view_que())
        else:
            print("\nNot a valid option. Please use either 1 or 2.")
    except Exception as e:
        print("\nAn error has occured: " + e)
