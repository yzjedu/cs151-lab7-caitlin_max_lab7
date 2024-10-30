def main():
    play = input('Would you like to run this program: Yes/No ').lower()
    while play not in ['yes', 'no']:
        play = input('Would you like to run this program: Yes/No ').lower()
    while play =='yes':
        count = 0
        total_price = 0
        while count < 5:
            #functions stores area of floor five times
                def func_area():
                    width = int(input('enter width: '))
                    length = int(input('enter length: '))
                    area = width * length
                    return area
            #stores all the floor types and how much thy cost five times
                def func_floor_type():
                    floor_type = input('enter floor type: ').lower()
                    while floor_type != 'hardwood' and floor_type != 'carpet' and floor_type != 'tile':
                        floor_type = input('enter floor type: ').lower()
                    if floor_type == 'hardwood':
                        floor_price = 1.39
                    if floor_type == 'carpet':
                        floor_price = 3.99
                    if floor_type == 'tile':
                        floor_price = 4.99
                    return floor_price
            #times the floor type by the floor area to find total 5 times
                def room_price(area, floor_price):
                    room_price = floor_price * area
                    return room_price
                count = count + 1
                total_price = total_price + room_price(func_area(), func_floor_type())
                print(f'the total price is {total_price}')
        play = input('Would you like to run this program again: Yes/No ').lower()
        if play not in ['yes', 'no']:
            play = input('Would you like to run this program: Yes/No ').lower()
        if play == 'no':
            print('Thank you for using this program')
main()















