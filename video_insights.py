from models.Results import Results

def display_menu():
    print("Menu:")
    print("1. Ver insights")
    print("2. Inserir dados do csv na tabela")
    print("3. Exportar dados csv")
    print("4. Consultar Incidência por KM")

def option1():
    print("Você selecionou a Opção 1 - Ver insights")
    Results.get_highway_info()

def option2():
    print("Você selecionou a Opção 2 - Inserir dados do csv na tabela")
    Results.insert_data()

def option3():
    print("Você selecionou a Opção 3 - Exportar dados csv ")
    Results.export_csv()

def option4():
    print("Você selecionou a Opção 4 - Consultar Incidência por KM ")
    item = input("Qual item você quer verificar a incidência: ")
    km_maior_incidencia, incidencia = Results.encontrar_maior_incidencia(item)
    print(f"O quilômetro com maior incidência de {item} é: {km_maior_incidencia}, com {incidencia} ocorrências.")

def main():
    while True:
        display_menu()
        choice = input("Digite sua escolha (1-5): ")

        if choice == "1":
            option1()
        elif choice == "2":
            option2()
        elif choice == "3":
            option3()
        elif choice == "4":
            option4()
        elif choice == "5":
            print("Encerrando o programa...")
            break
        else:
            print("Escolha inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()



