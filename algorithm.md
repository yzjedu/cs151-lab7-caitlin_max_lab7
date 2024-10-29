# Algorithm Document
#### PLEASE! PLEASE! PLEASE! THINK before you code...
* purpose: call the whole program
* name: main
* parameter: none
* return: the program
* algorithm:
  1. count = 0
  2. total price = 0
  3. while count < 5:
  4. call func_area, func-floor_type, and room_price


* purpose: calculates area of room 
* name: func_area
* parameter: none
* return: area
* algorithm:
  1. set width equal to user input
  2. set length equal to user input
  3. set area equal to width x length
  4. return area

* purpose: establishes floor type and price
* name: func_floor_type
* parameter: none
* return: floor price
* algorithm:
  1.  set floor type equal to user input and convert to lower
  2. while floor type is not equal to hardwood, tile, and carpet
     1. set floor type equal to user input and convert to lower
  3. if floor type is equal to hardwood
     1. floor price is equal to 1.39
  4. otherwise if floor type is equal to carpet
     1. floor price is equal to 3.99
  5. otherwise if floor price is equal to tile
     1. floor price is equal to 4.99
  6. return floor price

* purpose: sets room price
* name: room_price
* parameter: area, floor price
* return: room price
* algorithm:
  1. set room price equal to floor price x area
  2. return room price
  3. count += 1
  4. total price is equal to total price + room price(func_area, func_floor_type)

5. print total price

