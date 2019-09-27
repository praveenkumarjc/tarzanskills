with open("test.txt","r")as file:
    with open("new.txt","w")as file2:
        for line in file:
            file2.write(line)