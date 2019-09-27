with open("test2.txt","r")as file:
    size=10
    content=file.read(size)
    while len(content)>0:
        print(content,end="**")
        content = file.read(size)
