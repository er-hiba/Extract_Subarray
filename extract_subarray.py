def subarray (List, X, Y):
    subarray = []
    for i in range (X, Y):
        subarray.append(List[i])
    return subarray

# Main program

while True :
    List = []
    for i in range (10):
        N = int(input("Enter an integer to add to the list: "))
        List.append(N)
    X = int(input("Enter the starting index: "))
    Y = int(input("Enter the ending index (excluded): "))
    print("The subarray is:", subarray(List, X, Y))
    answer = input("Do you want to enter a new list (Enter 'Yes' or 'No'): ")
    if answer == "No" :
        break
    
        
