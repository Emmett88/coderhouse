
def main():
    nomes = input("Coloque o nome de cada pessoa separando por vírgula, mano: ")

    lista_nomes = nomes.split(',')

    lista_nomes = [nome.strip() for nome in lista_nomes]

    print("A lista tá assim, ó", lista_nomes)

if __name__ == "__main__":
    main()
