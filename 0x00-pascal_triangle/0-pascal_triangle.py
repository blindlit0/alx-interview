#!/usr/bin/python3

def pascal_triangle(n):
    '''
    func: pascal_triangle
        function that 
        returns a list of lists of integers
        representing the Pascals triangle of n
    args:
        <int: n> : number of rows (> 0)
    return:
        <list <of list>>
    '''

    if type(n) is not int and n < 0:
        return ([])
    line = []
    for i in range(n):
        line.append([])
        line[i].append(1)
        if (i > 0):
            for j in range(1, i):
                line[i].append(line[i - 1][j - 1] + line[i - 1][j])
            line[i].append(1)

    return (line)
