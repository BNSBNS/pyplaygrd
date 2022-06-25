import requests
import bs4


def verify(url):
    res1 = requests.get(url)

    try:
        res1.raise_for_status()

# here it get the href, and then the anchor for the links and go through them

        soup = bs4.BeautifulSoup(res1.text, 'html.parser')
        pageLinks = [link.get('href')
                     for link in soup.select('a') if link.get('href')]

        brokenCount = 0
        goodCount = 0

        for link in pageLinks:

            if link.startswith('http'):
                res2 = requests.get(link)
                try:
                    res2.raise_for_status()
                    print('good link, ', link)
                    goodCount += 1

                except Exception as exc:
                    print('broker is ', link)
                    brokenCount += 1

        print('good count = ', goodCount, 'broken count= ', brokenCount)

    except Exception as exc:
        print('there was problem with ', exc)


if __name__ == '__main__':
    verify('https://automatetheboringstuff.com/chapter11')
