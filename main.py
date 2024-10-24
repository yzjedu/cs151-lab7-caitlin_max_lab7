count = 0
total_price = 0
while count < 5:
    def func_area():
        width = int(input('enter width: '))
        length = int(input('enter length: '))
        area = width * length
        return area

    def func_floor_type():
        floor_type = input('enter floor type: ')
        while floor_type != 'hardwood' and floor_type != 'carpet' and floor_type != 'tile':
            floor_type = input('enter floor type: ').lower()
        if floor_type == 'hardwood':
            floor_price = 1.39
        if floor_type == 'carpet':
            floor_price = 3.99
        if floor_type == 'tile':
            floor_price = 4.99
        return floor_price

    def room_price(area, floor_price):
        room_price = floor_price * area
        return room_price
    count = count + 1
    total_price = total_price + room_price(func_area(), func_floor_type())

print(total_price)













