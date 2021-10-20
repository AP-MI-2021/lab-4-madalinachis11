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

def show_parte_intreaga(lst):
    result=get_parte_intreaga()
    print(f'Lista cu partile intregi din lista {lst} este:{result}')

def get_parte_intreaga(lst):
    '''
    Determina lista in care sunt partile intregi ale numerelor din lista.
    :param lst: lista introdusa.
    :return: lista care indeplineste conditia ceruta.
    '''
    for num in lst:
            result.append(int(num))
    return result
def test_get_parte_intreaga():
    assert get_parte_intreaga([1.5, -3.3, 8, 9.8, 3.2]) == [1, -3, 8, 9, 3]
    assert get_parte_intreaga([]) == []
    assert get_parte_intreaga([2.3, 4,19, 20.4]) == [2, 4, 20]


def main():
    lst = []
    while True:
        show_menu()
        optiune = input('Alegeti optiunea:')
        if optiune == '1':
            lst = read_list()
        elif optiune == '2':
            show_parte_intreaga(lst)
        elif optiune == 'x':
            break
        else:
            print('Optiune invalida, reincercati!')

if __name__=='__main__':
    test_get_parte_intreaga()
    main()



