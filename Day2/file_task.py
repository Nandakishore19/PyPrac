def read_file():
    with open('task.txt','r') as rf:
        rf_content = rf.read()
        if len(rf_content) == 0:
            print("No notes found")
        print(rf_content)


def write_file(str):
    with open('task.txt','w') as wf:
        wf.write(str)


def append_files(str):
    with open('task.txt', 'a') as af:
        af.write(str)

while(True):
    print("Enter your choice:\n 1. Read notes from the file\n 2. Write a new note to the file\n 3. Append a note to the existing file\n 4. Exit the application")
    inp = int(input())
    if inp==1:
        read_file()
    elif inp ==2:
        string = input("Enter the text\n")
        write_file(string)
    elif inp==3 :
        string = input("Enter the text you want to append\n")
        append_files(string)
    elif inp==4:
        break
    else:
        print("Incorrect input")