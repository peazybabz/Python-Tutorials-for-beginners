import sys

print('\nNumber of parameters', len(sys.argv), 'parameters')
print('\nParametersList', sys.argv)#to run the code from the shell you must import this 'sys.argv'

def tuples(x): #def tuples is the name of the class we are working in
    result = x
    for k in range(x-1, 1, -1):
        result = result * k
        return result
    print('\n', sys.argv(1),'!=', tuples(int(sys.argv(1)))) # we call the tuple here again