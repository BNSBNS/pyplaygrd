import re
import requests,os,bs4

url = 'http://xkcd.com/'
os.makedirs('/home/mn/pythonprojs/pyplaygrd/starterprojs/automateboringstuffpython/practiceprojects/xkcd',exist_ok=True)

while not url.endswith('#'):
    print('downloading ... %s ...' %url)

    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)

    #find url
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('cnt find img')

    else:
        comicUrl = 'http' + comicElem[0].get('src')

    #download
    print('downloading image %s ' %(comicUrl))
    res = requests.get(comicUrl)
    res.raise_for_status()
    #save img

    #get prev butn



print('done')
