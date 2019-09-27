with open('rose-blue-flower-rose-blooms-67636.jpeg', 'rb') as f:
    pix = f.read()
with open('new.jpeg', 'wb') as f:
    f.write(pix)