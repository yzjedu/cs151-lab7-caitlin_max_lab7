# Algorithm Document
#### PLEASE! PLEASE! PLEASE! THINK before you code...
* purpose: call the whole program
* name: main
* parameter: none
* return: the program
* algorithm:
  1. set play equal to user input of either yes or no
  2. while play is not yes or no
     1. set play equal to user input of either yes or no
  3. while play is equal to yes
     1. set count equal to zero
  4. set total price equal to zero
  5. while count is less than 5
     1. call func_area
     2. call func_floor_type
     3. call room_price
     4. set count equal to count plus 1
     5. set total price equal to total price plus room price
     6. print total price
  6. set play equal to user input of either yes or no
  7. while play is not equal to yes or no
     1. set play equal to user input of either yes or no
  8. if play is equal to no
     1. print thank you for using this program


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


