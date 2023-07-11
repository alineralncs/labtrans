from models.Results import Results
from models.BaseModel import db
from models.Videos import Videos
from models.Rodovias import Rodovias

def display_menu():
    print("Menu:")
    print("1. Criar tabelas")
    print("2. Popular tabela results com dados do csv")
    print("3. Exportar dados csv")
    print("4. Consultar Incidência por KM")
    print("5. Ver videos")
    print("6. Ver rodovias")
    print("7. Ver infos")
    print("8. Encerrar o programa")

def option1():
    print("Você selecionou a Opção 1 - Criar tabelas")
    db.create_tables([Results, Videos, Rodovias])


def option2():
    print("Você selecionou a Opção 2 - Popular tabela results com dados do csv")
    Results.delete_results()
    Results.insert_data()


def option3():
    print("Você selecionou a Opção 3 - Exportar dados csv ")
    Results.export_csv()

def option4():
    print("Você selecionou a Opção 4 - Consultar Incidência por KM ")
    item = input("Qual item você quer verificar a incidência: ")
    km_maior_incidencia, incidencia, rodovia = Results.find_incidence(item)
    print(f"O quilômetro com maior incidência de {item} é na rodovia {rodovia} e no km: {km_maior_incidencia}, com {incidencia} ocorrências.")
def option5():
    print("Você selecionou a Opção 5 - Ver vídeos e seus kms ")
    Videos.delete_videos()
    Videos.create_videos()
    Videos.show_videos()

def option6():
    print("Você selecionou a Opção 6 - Ver rodovias e seus kms ")
    Rodovias.delete_highways()
    Rodovias.create_highway()
    Rodovias.show_highways()

def option7():
    print("Você selecionou a Opção 7 - Ver infos ")
    Results.get_highway_info()

def main():
    while True:
        display_menu()
        choice = input("Digite sua escolha (1-8): ")

        if choice == "1":
            option1()
        elif choice == "2":
            option2()
        elif choice == "3":
            option3()
        elif choice == "4":
            option4()
        elif choice == "5":
            option5()
        elif choice == "6":
            option6()
        elif choice == "7":
            option7()
        elif choice == "8":
            print("Encerrando o programa...")
            break
        else:
            print("Escolha inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()





