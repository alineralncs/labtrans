from models.Results import Results
from models.BaseModel import db
from models.Videos import Videos
from models.Rodovias import Rodovias
from models.ViewResults import ViewResults

from prettytable import PrettyTable


def display_menu():
    print("Menu:")
    print("1. Criar tabelas ")
    print("2. Popular tabelas - Results, Videos e Rodovias")
    print("3. Exportar dados csv")
    print("4. Ver resultado do agrupamento das rodovias")
    print("5. Consultar Incidência por KM")
    print("6. Ver videos")
    print("7. Ver rodovias")
    print("8. Encerrar o programa")

def option1():
    print("Você selecionou a Opção 1 - Criar tabelas")
    db.create_tables([Results, Videos, Rodovias, ViewResults])

def option2():
    print("Você selecionou a Opção 2 - Popular tabelas - Results, Videos e Rodovias")
    Results.delete_results()
    Results.insert_data()
    Videos.delete_videos()
    Videos.create_videos()
    Rodovias.delete_highways()
    Rodovias.create_highway()

def option3():
    print("Você selecionou a Opção 3 - Exportar dados csv ")
    Results.export_csv()

def option4():
    print("Você selecionou a Opção 6 - Ver resultado do agrupamento das rodovias ")

    results = ViewResults.get_highway_info()
    def display_results(results):
        table = PrettyTable()
        table.field_names = ["Rodovia", "Km", "Buraco", "Remendo", "Trinca", "Placa", "Drenagem"]

        for row in results:
            table.add_row([row["highway"], row["km"], row["buraco"], row["remendo"], row["trinca"], row["placa"], row["drenagem"]])

        print(table)
    display_results(results)

def option5():
    print("Você selecionou a Opção 4 - Consultar Incidência por KM ")
    item = input("Qual item você quer verificar a incidência: ")
    km_maior_incidencia, incidencia, rodovia = Results.find_incidence(item)
    print(f"O quilômetro com maior incidência de {item} é na rodovia {rodovia} e no km: {km_maior_incidencia}, com {incidencia} ocorrências.")
    
def option6():
    print("Você selecionou a Opção 5 - Ver vídeos e seus kms ")

    Videos.show_videos()

def option7():
    print("Você selecionou a Opção 6 - Ver rodovias e seus kms ")
    Rodovias.show_highways()

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





