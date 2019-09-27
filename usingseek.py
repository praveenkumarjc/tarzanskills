with open("test2.txt","r")as file:
    print(file.read(5))
    file.seek(0)
    print(file.readline(5))