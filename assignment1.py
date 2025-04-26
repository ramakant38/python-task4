
try:
    with open('sample.txt','r') as file1:
        readFile = file1.read()
        print(readFile)
except FileNotFoundError:
    print("The file \'sample.txt\' was not found")