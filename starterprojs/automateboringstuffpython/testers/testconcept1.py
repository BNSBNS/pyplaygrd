# def spam():
#     eggs=99
#     bacon()
#     print(eggs)

# def bacon():
#     ham=101
#     eggs=0

# spam()

# def spam():
#     global eggs
#     eggs ='spam'

# eggs ='global'
# spam()
# print(eggs)

# def spam():
#     global eggs
#     print(eggs)
#     eggs='local'

# eggs ='global'
# spam()

# catName = []
# while True:
#     print('enter name of cat' + str(len(catName) + 1) + ('or enter nth to stop '))
#     name = input()
#     if name == '':
#         break
        # this part is the key, list = list + [indexval to add in]
#     catName = catName + [name]

# print('cat names are ', catName)

# print('')

# for name in catName:
#     print( '   ' + name)

# sup = ['234','435,',12312]

# for i, s in enumerate(sup):
#     print('i = ', i, 's = ', s)


# def checkval(val, li) -> None:
#     if val in li:
#         print('asd')



# li = ['asd',34]
# checkval('asd',li)
# print(type(checkval('asd',li)))

# birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

# while True:
#     print('enter a name: (blank to quit)')
#     name = input()
#     if name == '':
#         break;

#     if name in birthdays:
#         print(birthdays[name] + ' is the birthday of ' + name)
#     else:
#         print('do not have birthday info for ' + name)
#         print('what is their bday?')
#         bday = input()
#         birthdays[name] = bday
#         print('bday database updated')

# count = 0
# for i in range(5):
#     count+=1
#     print(count)


# def printPicnic(itemsDict, leftWidth, rightWidth):
#     print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
#     for k, v in itemsDict.items():
#         print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

# picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
# printPicnic(picnicItems, 12, 5)
# printPicnic(picnicItems, 20, 6)

# import re
# pnr = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# a = pnr.search('my num is 112-333-4242')
# print('num = '+ a.group())


import logging
logging.basicConfig(level=logging.DEBUG,format=' %(asctime)s -%(levelname)s - %(message)s')

logging.debug('some debug details')
logging.info('logging working')
logging.warning('warning')
logging.error('error')
logging.critical('critical')