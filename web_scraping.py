import requests
import bs4


def update_xrates():
    url = requests.get('https://www.x-rates.com/table/?from=EUR&amount=1')
    url.raise_for_status()  # segnala se ci sono errori

    soup = bs4.BeautifulSoup(url.text, 'html.parser')   # ottiene l'html del sito
    changes = open('files\\changes.txt', 'w')  # apro il file su cui scriverò le valute
    changes.write('Euro: 1.000000\n')  # metto la moneta fondamentale euro al primo posto

    for i in range(1, 54):
        name = soup.select('.tablesorter > tbody:nth-child(2) > tr:nth-child('+str(i)+') > td:nth-child(1)')
        value = soup.select('.tablesorter > tbody:nth-child(2) > tr:nth-child('+str(i)+') > td:nth-child(2) > a:nth-child(1)')
        changes.write(name[0].text + ': ' + value[0].text + '\n')  # appendo

    changes.close()     # chiudo il file


def lista_valute():
    names = ['Euro']

    url = requests.get('https://www.x-rates.com/table/?from=EUR&amount=1')
    url.raise_for_status()  # segnala se ci sono errori

    soup = bs4.BeautifulSoup(url.text, 'html.parser')   # ottiene l'html del sito
    for i in range(1, 54):
        name = soup.select('.tablesorter > tbody:nth-child(2) > tr:nth-child('+str(i)+') > td:nth-child(1)')
        name = str(name[0])
        names.append(name[4:-5])

    return names
