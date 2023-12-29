#Input of citizenship status
def citizenship_status():
    citizenship = ""
    print('Please enter your citizenship status \n SG = Singaporean \n PR = Permanent Resident \n FR = Foreigner')
    while True:
        citizenship = input('\nCitizenship status (SG, PR, FR) : ').upper()
        if citizenship not in ['SG', 'PR', 'FR']:
            print('\nInvalid citizenship! Please enter a valid Citizenship status.')
        else:
            break
    return citizenship

#Input of current number of properties owned
def current_properties():
    number_of_properties = ""
    while True:
        number_of_properties = int(input('\nEnter number of properties currently owned: '))
        if number_of_properties < 0:
            print('\nNumber of property cannot be negative.')
        else:
            break
    return number_of_properties

#Input price of property
def property_price():
    price_of_property = ""
    while True:
        price_of_property = float(input('\nEnter price of property to purchase ($): ').replace(',',''))
        if price_of_property <= 0:
            print('\nPlease input a valid price.')
        else:
            break
    return price_of_property

#Calculation for BSD and ABSD
def calcBSD(price_of_property):
    import math
        #Calculation for BSD
    if price_of_property <= 180000:
        BSD = price_of_property * 0.01
    elif price_of_property <= 360000:
        BSD = 180000 * 0.01 + math.ceil(price_of_property - 180000) * 0.02
    elif price_of_property <= 1000000:
        BSD = 180000 * 0.01 + 180000 * 0.02 + math.ceil(price_of_property - 360000) *0.03
    else:
        BSD = 180000 * 0.01 + 180000 * 0.02 + 640000 *0.03 + math.ceil(price_of_property- 1000000) * 0.04
    return BSD

    #Calculation for ABSD
def calcABSD(citizenship, number_of_properties, price_of_property):
    if number_of_properties == 0:
        if citizenship == 'PR':
            ABSD = price_of_property * 0.05
        elif citizenship == 'FR':
            ABSD = price_of_property * 0.30
        else:
            ABSD = 0
    elif number_of_properties == 1:
        if citizenship == 'PR':
            ABSD = price_of_property * 0.25
        elif citizenship == 'FR':
            ABSD = price_of_property * 0.30
        else:
            ABSD = price_of_property * 0.17
    else:
        if citizenship == 'PR' or citizenship == 'FR':
            ABSD = price_of_property * 0.30
        else:
            ABSD = price_of_property * 0.25
    return ABSD


#Display all user inputs and result
def main():
    citizenship = citizenship_status()
    citizenship = citizenship.replace('SG','Singaporean')
    citizenship = citizenship.replace('PR', 'Permanent Resident')
    citizenship = citizenship.replace('FR', 'Foreigner')

    price_of_property = property_price()
    number_of_properties = current_properties()
    BSD = calcBSD(price_of_property)
    ABSD = calcABSD(citizenship, number_of_properties, price_of_property)

    print(f'\nProperty price: ${float(price_of_property):,.2f} \
        \nCitizenship: {citizenship} \
        \nNumber of properties currently owned: {number_of_properties}')
    print(f'\nBSD : ${BSD:,.2f}')
    if ABSD == 0:
        print('ABSD: Not applicable')
    else:
        print(f'ABSD: ${ABSD:,.2f}')   

main()


