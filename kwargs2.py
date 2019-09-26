def myfunc(**kwargs):
    if 'first'and'mid'and'last' in kwargs:
        print(f"{kwargs['first']},{kwargs['mid']},{kwargs['last']}")

myfunc(first='praveen',mid='kumar',last='b')