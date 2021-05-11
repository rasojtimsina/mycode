#!/usr/bin/env python3

round = 0
self_driving =' '
battery_power = ' '


#while round<3 and  self_driving != 'yes' and battery_power != 'electric':
while round<3 and  self_driving not in ['yes', 'no'] and battery_power not in ['electric', 'gasoline']:
    round +=1
    print('Lets find out what car you want to drive:')

    self_driving = input('Do you like sef-driving car? Yes/No\n =>').lower()
    battery_power = input('Do you prefer electric or gasoline?\n =>').lower()
    if self_driving == 'yes' and battery_power == 'electric':
        print('Your preferred car choice is Tesla. Make sure you have $80k in your bank account')
    elif self_driving == 'no' and battery_power == 'gasoline':
        print('Congratulation there are tons of choices out there as per your budget.')
    elif self_driving == 'no' and battery_power == 'electric':
        print('There are few good hybrids out there')
    elif self_driving == 'yes' and battery_power == 'gasoline':
        print("Ain't no such thing made yet.")
    elif round ==3:
        print('Sorry, you missed your future vehicle choice.')
    else:
        print('Please enter valid selection')

