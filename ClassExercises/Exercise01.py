x = [int(x) for x in input("Enter 10 values: ").split()]
print("Number of list is: ", x)

def calculate_average(x):
    sum = 0
    for num in x:
        sum += num
    return sum/len(x)

avg = calculate_average(x)
print(f"The average is: {avg} ")
