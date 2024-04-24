# f = open('text.txt','r') #reading, writing, appending, reading and writing
# print(f.name)
# print(f.read())
# print(f.mode)
# f.close()

# with open('text2.txt', 'w') as f:
        # f.write('nanda')
           
    # f_contents = f.readline()
    # print(f_contents)
#     # f_contents = f.readline()
#     # print(f_contents)

# print(f.closed)

with open('text.txt', 'r') as rf:
    with open('text_copy','w') as wf:
        for line in rf:
            wf.write(line)
        

with open('Testing.png','rb') as rf:
    with open('Testing_copy.png','wb') as wf:
        chunk_size = 50
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) >0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
