first = 1
second = 0


for i in range(1,46):

    current = first + second

    print(f"N = {i} -> {current}")
    
    second = first
    first = current
