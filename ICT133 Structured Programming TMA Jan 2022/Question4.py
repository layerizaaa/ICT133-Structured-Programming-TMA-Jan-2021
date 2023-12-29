#Create Menu Dictionary
def getMenu():
    menu = {}
    for line in open('menu.txt', 'r'):
        item_code, description, price = line.split(',')
        menu[item_code] = [description, float(price)]
    return menu


#Display Option Menu
def getOption():
    return int(input('''
ABC Briyani
1. Place order
2. Update order
3. Serve order
0. Exit 
Enter option: '''))


#Q4a Place order function
def placeOrder(menu, order_number):
    print('''
Menu
B1 - Chicken Briyani $5.00
B2 - Mutton Briyani $5.50
B3 - Fish Briyani $6.00''')
    order_list = []
    while True:
        order_input = input('Enter item code and quantity (Press <Enter> key to end): ').capitalize()
        if order_input == '': 
            break
        order = order_input.split()
        if order[0] not in menu.keys():
            print('Invalid Item Code! Try again.')
        order_list.append(order)   
    return order_list   


#Stores orders in a dictionary
def storeOrder(orders, order_list, order_number):
    orders[order_number] = order_list
    return orders


#Display Summary of Order
def summaryOrder(menu, orders, order_number):
    print(f'\n***Order number {order_number}***')
    Total_price = 0
    order_list = orders[order_number]
    for item_code, quantity in order_list:
        if item_code in menu.keys():
            cost = menu[item_code][1] * float(quantity)
            print(f'''{item_code} {menu[item_code][0]} x {quantity} = ${cost:.2f}''')
            Total_price += cost 
    print(f'Total price ${Total_price:.2f}')   
    return order_list


#Select order to update
def selectOrder(menu, orders):
    order_key = ''
    if orders == {}:
        print('\nNo orders')
    else:
        while True:
            order_key = int(input('\nEnter order number: '))
            if order_key not in orders.keys():
                print('\nOrder not found!')
            else:
                order_list = summaryOrder(menu, orders, order_key)
                orders = updateOrder(menu, orders, order_key, order_list)
                break
    return orders


#Q4b Update order function
def updateOrder(menu, orders, order_key, order_list):
    for eachOrder in order_list[:]:
        update = input(f'\n{eachOrder[0]} {menu[eachOrder[0]][0]} x {eachOrder[1]}, enter new qty or <Enter> for no change: ')
        if update == '0':
            print(f'{eachOrder[0]} {menu[eachOrder[0]][0]} removed.')
            order_list.remove(eachOrder) 
        elif update == '':
            print(f'{eachOrder[0]} {menu[eachOrder[0]][0]} no change.')
        else:
            eachOrder[1] = int(update)
    if order_list == []:
        print(f'\nOrder {order_key} cancelled.')
        orders.pop(order_key)
    else: 
        print(f'\nOrder {order_key} update:')
        summaryOrder(menu, orders, order_key)
    return orders  


#Q4c Serve order
def serveOrder(menu, orders):
    if orders == {}:
        print('\nNo orders')
    else:
        ready_order = int(input('\nEnter order number that is ready: '))
        summaryOrder(menu, orders, ready_order)
        orders.pop(ready_order)
        input('\nPress <Enter> when order is collected: ')
    return orders
            

#Main Function   
def main():
    order_number = 1
    orders = {}
    while True:
        option = getOption()
        menu = getMenu()

        if option == 1:
            order_list = placeOrder(menu, order_number)
            orders = storeOrder(orders, order_list, order_number)
            summaryOrder(menu, orders, order_number)
            order_number += 1 
        
        elif option == 2:
            orders = selectOrder(menu, orders)
        
        elif option == 3:
            orders = serveOrder(menu, orders)
            print(orders)
        elif option == 0:
            break
        
        else:
            print('Invalid menu choice')

main()

 