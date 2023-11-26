'''
Input takes all input as string by default

variable_name = input(statement)

print():
    Function to display the output

    print(value/values, sep='', end='\n', file=file, flush=flush)

        sep: separator, separator use to separate the objects when more than one object, default = ''
        end: It gives what to print at the end , default = '\n'
        file: default= sys.stdout
        flush: default=False
                if flush = True , the output will be flushed
                   flush = False, the output will be buffered
'''
import time
# print('the','python','best', sep='**', end='$')
# print('world') #the**python**best$world

for i in range(1,10):
    print(i)
    time.sleep(1)

for i in range(1,10):
    print(i, flush=True)
    time.sleep(1)
