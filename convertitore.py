def invio(value_from, dalla_valuta, alla_valuta):
    try:

        change = open('files\\changes.txt', 'r')
        change_list = change.readlines()
        dalla_valuta_value = 0
        alla_valuta_value = 0
        for c in change_list:
            if c[0:len(dalla_valuta)] == dalla_valuta:
                dalla_valuta_value = c[(len(dalla_valuta) + 2):-3]
            if c[0:len(alla_valuta)] == alla_valuta:
                alla_valuta_value = c[(len(alla_valuta) + 2):-3]

        res = (float(value_from) * float(alla_valuta_value) / float(dalla_valuta_value))
        return res

    except ValueError:   # segnala errore se non viene inserito un numero
        return 'Prova inserendo un valore numerico.'
