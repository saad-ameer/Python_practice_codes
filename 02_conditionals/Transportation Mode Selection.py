# Choose a mode of transportation based on the distance(eg. <3km: Walk), 3-15km: Bike, >15km: Car).

distance = int(input("Give a distance in km:"))

if distance <3:
    transport = "Walk"
elif distance <=15:
    transport = "Bike"
else:
    transport ="Car"

print(f"The mode of transport for you is {transport}.")
