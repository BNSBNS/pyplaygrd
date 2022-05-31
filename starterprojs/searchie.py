def SearchieCh(strParam) -> None:

    #return first non repeating char
    char_order = []
    counts = {}

    for c in strParam:
        if c in counts:
            counts[c] += 1
            print('counts[c] = {} '.format(counts[c]))
            # print('char_order[c] = {}'.format(char_order[c]))
        else:
            counts[c] = 1
            char_order.append(c)

        print(char_order[c])
    for c in char_order:
        if counts[c] == 1:
            return c


def Seachie1(strParam) -> None:
    while strParam != "":
        print('strParam = {}'.format(strParam))
        slen0 = len(strParam)
        ch = strParam[0]
        print('ch = {}'.format(ch))
        strParam = strParam.replace(ch, "")
        slen1 = len(strParam)
        if slen1 == slen0-1:
            # previous implemention had break here instead of return, break resulted in returning "none" after printing
            # break
            print('slen1 = {}'.format(slen1))
            print('slen0 = {}'.format(slen0))
            return ch
        else:
            print('else if')
    else:
        print('whhile else')


# print(SearchieCh('aassdd'))

print(Seachie1('aasdesasdad'))


