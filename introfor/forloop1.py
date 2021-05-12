#!/usr/bin/env python3

# create the list called vendors

vendors = ["cisco", "juniper", "big_ip", "f5", "arista"]

# create a second list of strings
approved_vendors = ["cisco", "juniper", "big_ip"]


# loop across the list vendors

for x in vendors:    # newline, print current vendor, and end without newline
    print("\nThe vendor is: " + x, end="")
    if x not in approved_vendors: # if x does not appear within the list approved_vendors
        print(" - NOT AN Approved VENDOR!", end="")
print("\nOur loop has ended")
