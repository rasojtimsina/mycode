#!/usr/bin/env python3

ipchk = input("Apply an IP address: ") # this line now prompts the user for input

# a provided string will test true
if ipchk == "192.168.70.1":
   print("Looks like the IP address of the Gateway was set: " + ipchk) # indented under if
elif ipchk:     # if any data is provided, this will test true
    print("Looks like the IP address was set: " + ipchk)
else:       #if data is not provided.
    print("You did not provide the input")
