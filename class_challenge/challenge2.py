#!/usr/bin/env python3
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

for animals1 in farms[0]["agriculture"]:
    print(animals1)

# input to chose the farm!
print("""
0. NE Farm
1. W Farm
2. SE Farm""")

choice = int(input("Choose a farm by its number!"))

for animals1 in farms[choice]["agriculture"]:
    print(animals1)

# choose animals only. Similar to above

veggies = ["carrots", "celery"]
print("""
0. NE Farm
1. W Farm 
2. SE Farm""")

choice = int(input("Choose a farm by its number!"))

for animals1 in farms[choice]["agriculture"]:
    if animals1 not in veggies:
        print(animals1)
