from pyparsing import col


def printTable(listofstrings):

    longestlen = len(max(listofstrings,key=len))
    longestidx = 0

    for idx, v in enumerate(listofstrings):
        if longestlen == len(v):
            longestidx = idx

    #print(longestidx)


    for colu in range(0,longestlen+1):
        #print(colu)
        for row in range(len(listofstrings)):
            try: 
                print(listofstrings[row][colu].rjust(10,'*'),end=' ')
            except:
                print('x',end='')
        print()
    # maxl = []

    # for row in range(len(listofstrings)):
    #     maxl.append(max([len(col) for col in listofstrings[row]]))
    
    # print(maxl)
    # for col in range(len(listofstrings[0])):
    #     for row in range(len(listofstrings)):
    #         print(listofstrings[row][col].rjust(maxl[row]),end=' ')

    #     print()


if __name__ == "__main__":
    tableData = [
        ['apples', 'oranges', 'cherries', 'banana'],
        ['Alice', 'Bob', 'Carol', 'David'],
        ['dogs', 'cats', 'moose', 'goose','234']
    ]

    printTable(tableData)
