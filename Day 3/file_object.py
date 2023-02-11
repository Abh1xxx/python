file=open ("file.txt","r+")
if file:
    print("The file open successfully")
    file.write("print('HELLO ABHIRAM file write successfully')")
    print(file.closed)
    print(file.mode)
    print(file.name)
abhi=open("abhi.c","a")
if abhi:
    print("Opened successfully")
    abhi.write('printf("HELLO world");')
    abhi.close()

