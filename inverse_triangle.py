#author__uy_thea
#date_october_3_2024
#section_bscpe_2-2


#get the height
def get_height():
    while True:
        try:
            height = int(input(">>> "))
        except:
            print("Invalid Input")
            continue
        else:
            return height

print("Enter the height of the triangle: ")
height = get_height()


#create the inverse triangle layout
for i in range(height):
    for j in range(i, height):
        print("*", end = " ")
    print()