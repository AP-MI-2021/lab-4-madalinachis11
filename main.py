def show_menu():
    print('1. Citire lista de float-uri.')
    print('2. Afișarea părții întregi a tuturor numerelor din listă.')
    print('3. Afisare numerele care aparțin unui interval deschis citit de la tastatură.')
    print('4. Afișarea tuturor numerelor a căror parte întreagă este divizor al părții fracționare.')
    print('5. Afișarea listei obținute din lista inițială în care numerele sunt înlocuite cu un string format din cuvinte care le descriu caracter cu caracter.')
    print('x. Exit')


def read_list():
    '''
    Functia de citire a listei.
    :return: lista introdusa.
    '''
    floats_as_str = input('Dati o lista de float-uri separate prin spatiu:')
    floats_as_list_of_str = floats_as_str.split(' ')
    floats = []
    for float_str in floats_as_list_of_str:
        floats.append(float(float_str))
    return floats
def show_cuvant_cheie(lst)
def transforma_in_cuvinte(numar):
    numar_in_cuvinte = ""
    while numae !=0:
        cifra=numar%10
        numar_in_cuvinte=cuvant_cifra + numar_in_cuvinte
        numar = int(numae/10)
    return numar_in_cuvinte

def transforma(lst):
    result= []
    for elem in lst:
        result.append(numar_in_cuvinte)
    return result

def cuvant_cifra(cifra):
    if cifra == 1:
        return "unu"
    if cifra == 2:
        return "doi":
    if cifra == 3:
        return "trei"
    if cifra == 4:
        return "patru"
    if cifra == 5:
        return "cinci"
    if cifra == 6:
        return "sase"
    if cifra == 7:
        return "sapte"
    if cifra == 8:
        return "opt"
    if cifra == 9:
        return "noua"

def show_parte_intreaga(lst):
    result=get_parte_intreaga(lst)
    print(f'Lista cu partile intregi din lista {lst} este:{result}')

def get_parte_intreaga(lst):
    '''
    Determina lista in care sunt partile intregi ale numerelor din lista.
    :param lst: lista introdusa.
    :return: lista care indeplineste conditia ceruta.
    '''
    result = []
    for num in lst:
            result.append(int(num))
    return result
def show_interval_deschis():
    start=int(input('Dati marginea din stanga a intervalului:'))
    stop=int(input('Dati marginea din dreapta a intervalului:'))
    result=get_interval_deschis(lst, start, stop)
    print(f'Lista din intervalul deschis este: {result}')

def get_interval_deschis(lst, start, stop):
    '''
    Determina toate numerelre dintr-un interval deschis introdus de la tastatura.
    :param lst: lista data.
    :return: lista care indeplineste cerinta.
    '''
    lista=[]
    for num in range(start+1,stop):
        lista.append(num)
    return lista


#def test_get_parte_intreaga():
    #assert get_parte_intreaga([1.5, -3.3, 8, 9.8, 3.2]) == [1, -3, 8, 9, 3]
    #assert get_parte_intreaga([]) == []
    #assert get_parte_intreaga([2.3, 4,19, 20.4]) == [2, 4, 20]



def main():
    lst = []
    while True:
        show_menu()
        optiune = input('Alegeti optiunea:')
        if optiune == '1':
            lst = read_list()
        elif optiune == '2':
            show_parte_intreaga(lst)
        elif optiune == '3':
            show_interval_deschis(lst, start, stop)
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida, reincercati!')

if __name__=='__main__':
    #test_get_parte_intreaga()
    main()



