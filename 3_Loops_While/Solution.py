numlist = []
invalid_inputs = []

while True:
    user_input = input("Enter a number: ")
    
    if user_input.lower() == 'done':
        break

    try:
        num = int(user_input)
        numlist.append(num)
    except:
        invalid_inputs.append(user_input)
        print("Invalid input")
        continue

if len(numlist) > 0:
    print(f"Maximum is {max(numlist)}")
    print(f"Minimum is {min(numlist)}")
    print(f"Invalid inputs: {invalid_inputs}")
else:
    print("No numbers were entered.")
    print(f"Invalid inputs: {invalid_inputs} ")