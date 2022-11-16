#1 
def hello():
    print("Howdy user")

#2
def pack(eggs, milk, lettuce):
    return [eggs, milk, lettuce]

#3
def eat_lunch(my_list):
    if len(my_list) == 0:
        print("My lunchbox is empty!")
    else:
        for x in range(len(my_list)):
            if x == 0:
                print(f"First I eat {my_list[0]}")
            else:
                print(f"Next I eat {my_list[x]}")


hello()
print(pack("eggs","milk","lettuce"))
eat_lunch([])
eat_lunch(["sandwich"])
eat_lunch(["peanut buttercup","banana","blueberries","yogurt"])
