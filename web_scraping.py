import requests
import bs4


def update_xrates():
    url = requests.get('https://www.x-rates.com/table/?from=EUR&amount=1')
    url.raise_for_status()  # segnala se ci sono errori

    soup = bs4.BeautifulSoup(url.text, 'html.parser')   # ottiene l'html del sito
    changes = open('files\\changes.txt', 'w')  # apro il file su cui scriverò le valute
    changes.write('Euro: 1.000000\n')  # metto la moneta fondamentale euro al primo posto

    i = 1
    name = soup.select('.tablesorter > tbody:nth-child(2) > tr:nth-child('+str(i)+') > td:nth-child(1)')    # parto dal primo
    while name:
        value = soup.select('.tablesorter > tbody:nth-child(2) > tr:nth-child('+str(i)+') > td:nth-child(2) > a:nth-child(1)')
        changes.write(name[0].text + ': ' + value[0].text + '\n')  # appendo
        
        i += 1
        name = soup.select('.tablesorter > tbody:nth-child(2) > tr:nth-child('+str(i)+') > td:nth-child(1)')

    changes.close()     # chiudo il file


def lista_valute():
    names = ['Euro']

    url = requests.get('https://www.x-rates.com/table/?from=EUR&amount=1')
    url.raise_for_status()  # segnala se ci sono errori

    soup = bs4.BeautifulSoup(url.text, 'html.parser')   # ottiene l'html del sito
    
    i = 1
    name = soup.select('.tablesorter > tbody:nth-child(2) > tr:nth-child('+str(i)+') > td:nth-child(1)')
    while name:
        name = str(name[0])
        names.append(name[4:-5])

        i += 1
        name = soup.select('.tablesorter > tbody:nth-child(2) > tr:nth-child('+str(i)+') > td:nth-child(1)')

    return names
