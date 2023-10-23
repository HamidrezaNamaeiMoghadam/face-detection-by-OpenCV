import random
hads=int(input("adad bde: "))

num=random.randint(1, 100)
c=0
while hads!=num:
    if hads < num:
        print("mal man bozorgtare")
    else:
        print("mal man kotahtare")
    hads=int(input("haha ridi,dobare hads bzn: "))
    c+=1
print("wowww to khafani ",c ,"hads")
