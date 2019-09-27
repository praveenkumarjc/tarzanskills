with open("test2.txt","r")as file:
    print(file.read(5))
    print(file.read(5))
    print(file.readline(5))
    print(file.readlines(5))