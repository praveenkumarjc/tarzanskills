with open('rose-blue-flower-rose-blooms-67636.jpeg', 'rb') as fr:
    with open('new1.jpeg', 'wb') as fw:
        chunk_size=4096
        rf_chunk=fr.read(chunk_size)
        while len(rf_chunk)>0:
            fw.write(rf_chunk)
            rf_chunk=fr.read(chunk_size)