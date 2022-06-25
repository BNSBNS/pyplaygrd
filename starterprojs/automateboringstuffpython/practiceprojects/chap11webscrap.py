import re
import webbrowser, sys, pyperclip, requests, bs4


# cli and paste
# if len(sys.argv) > 1:
#     address = ' '.join(sys.argv[1:])
# else:
#     address = pyperclip.paste()

# webbrowser.open('http://www.google.com/maps/place/'+address)



# resquest
# res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

# print(type(res))

# print(res.status_code == requests.codes.ok)

# len(res.text)

# print(res.text[:250])


# bs4
# res = requests.get('http://nostarch.com')
# print(res.raise_for_status)
# nostarchsoup = bs4.BeautifulSoup(res.text)
# print(type(nostarchsoup))

# examfile = open('../testers/example.html')
# examSoup = bs4.BeautifulSoup(examfile)
# print(type(examSoup))

# div = examSoup.select('div')
# print(div)

import logging

logging.basicConfig(level=logging.DEBUG,format=' %(asctime)s -%(levelname)s - %(message)s')
logging.debug('html')
print('googling...')

res = requests.get('http://google.com/search?q=' + ''.join(sys.argv[1:]))

res.raise_for_status()

# get top search result
soup = bs4.BeautifulSoup(res.text)

# open browser for each tab
linkElems = soup.select('.yuRUBF a')
numOpen = min(5,len(linkElems))
print(linkElems)
logging.info('aft nu opem')
for i in range(numOpen):
    
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
    logging.info('in for loop')

