from models.Results import Results

def display_menu():
    print("Menu:")
    print("1. Ver insights")
    print("2. Inserir dados do csv na tabela")
    print("3. Exportar dados csv")
    print("4. Sair")

def option1():
    print("Você selecionou a Opção 1 - Ver insights")
    Results.get_highway_info()

def option2():
    print("Você selecionou a Opção 2 - Inserir dados do csv na tabela")
    Results.insert_data()

def option3():
    print("Você selecionou a Opção 2 - Exportar dados csv ")
    Results.export_csv()

def main():
    while True:
        display_menu()
        choice = input("Digite sua escolha (1-4): ")

        if choice == "1":
            option1()
        elif choice == "2":
            option2()
        elif choice == "3":
            option3()
        elif choice == "4":
            print("Encerrando o programa...")
            break
        else:
            print("Escolha inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()



