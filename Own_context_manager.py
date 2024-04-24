from contextlib import contextmanager
# class Openfile:
#     def __init__(self,filename,mode) -> None:
#         self.filename = filename
#         self.mode = mode
#     def __enter__(self):
#         self.file = open(self.filename,self.mode)
#         return self.file
#     def __exit__(self,exc_type,exc_val,traceback):
#         self.file.close()


# with Openfile('task.txt', 'w') as f:
#     f.write('Testing')


# print(f.closed)
@contextmanager
def open_file(file,mode):
    try:
        f = open(file,mode=mode)
        yield 
    except:
        print("Type Error")
    finally:
        f.close()

with open_file('task.txt','w') as f:
    f.write('Nanda Kishoreeeee Gorenka')

print(f.closed)