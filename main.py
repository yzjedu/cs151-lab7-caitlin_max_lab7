# Programmers:  Caitlin Burns and Max Rice
# Course:  CS151, Professor Zee
# Due Date: 10/30/2024
# Lab Assignment: 7
# Problem Statement: This code allows a user to find the price of flooring in a house from different flooring types
# Data In: length, width, flooring type, run again
# Data Out: total price
# Credits: this code is basen on the guidelines given in the read me file


# Purpose:  runs main program
# Parameters: none
# Return: none
def main():
    print('This code allows user to find the price of flooring in a house with five rooms based on flooring type.')
    play = input('Would you like to run this program: Yes/No ').lower()
    while play not in ['yes', 'no']:
        play = input('Would you like to run this program: Yes/No ').lower()
    while play =='yes':
        count = 0
        total_price = 0
        while count < 5:
            #functions stores area of floor five times
            # Purpose:  finds the area of a room
            # Parameters: none
            # Return: area
                def func_area():
                    width = int(input('enter width: '))
                    length = int(input('enter length: '))
                    area = width * length
                    return area
            #stores all the floor types and how much thy cost five times
            # Purpose:  sets floor price from floor type
            # Parameters: none
            # Return: floor price
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
            # Purpose:  finds room price
            # Parameters: area and floor price
            # Return: room price
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















