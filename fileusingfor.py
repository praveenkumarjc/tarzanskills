with open("test2.txt","r")as file:
    content=file.readlines()
    for lines in content:
        print(lines,end=' ')