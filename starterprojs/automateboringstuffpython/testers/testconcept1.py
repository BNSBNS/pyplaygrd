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

def spam():
    global eggs
    print(eggs)
    eggs='local'

eggs ='global'
spam()