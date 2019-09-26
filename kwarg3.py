def grocery(**kwargs):
    if 'item'and'quantity'and'price' in kwargs:
        print(f"Item :{kwargs['item']}\tQuantity :{kwargs['quantity']}\tPrice :{kwargs['price']}")




grocery(item='soap',quantity='2',price='20.0')
grocery(item='shampoo',quantity='4',price='400.0')
grocery(item='facewash',quantity='5',price='200.0')