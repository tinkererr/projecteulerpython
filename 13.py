with open('numbers.txt', 'r') as file: # numbers.txt contains the numbers on separate lines
    print(str(sum([int(x) for x in file.readlines()]))[:10])
