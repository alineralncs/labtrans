from models.Results import Results
from models.Results import db
from models.Video import Video
from models.Highways import Highway
import subprocess
import sys
def display_menu():
    print("Menu:")
    print("1. Criar tabelas")
    print("2. Popular tabela results com dados do csv")
    print("3. Exportar dados csv")
    print("4. Consultar Incidência por KM")
    print("5. Ver videos")
    print("6. Ver rodovias")
    print("7. Encerrar o programa")

def option1():
    print("Você selecionou a Opção 1 - Criar tabelas")
 
    Results.create_table()
    db.create_tables([Video, Highway])


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
    km_maior_incidencia, incidencia, highway = Results.encontrar_maior_incidencia(item)
    print(f"O quilômetro com maior incidência de {item} é na rodovia {highway} e no km: {km_maior_incidencia}, com {incidencia} ocorrências.")
def option5():
    print("Você selecionou a Opção 5 - Ver vídeos e seus kms ")
    Video.delete_videos()
    Video.create_videos()
    Video.show_videos()

def option6():
    print("Você selecionou a Opção 6 - Ver rodovias e seus kms ")
    Highway.delete_highways()
    Highway.create_highway()
    Highway.show_highways()

def main():
    while True:
        display_menu()
        choice = input("Digite sua escolha (1-7): ")

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
            print("Encerrando o programa...")
            break
        else:
            print("Escolha inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()


# option1_selected = False
# option2_selected = False
# option3_selected = False
# option4_selected = False

# def option1():
#     global option1_selected
#     if not option1_selected:
#         print("Você selecionou a Opção 1 - Criar tabelas")
#         Results.create_table()
#         option1_selected = True
#     else:
#         print("Opção 1 já foi selecionada anteriormente.")

# def option2():
#     global option2_selected
#     if not option2_selected:
#         print("Você selecionou a Opção 2 - Inserir dados do csv na tabela")
#         Results.insert_data()
#         option2_selected = True
#     else:
#         print("Opção 2 já foi selecionada anteriormente.")

# def option3():
#     global option3_selected
#     if not option3_selected:
#         print("Você selecionou a Opção 3 - Exportar dados csv")
#         Results.export_csv()
#         option3_selected = True
#     else:
#         print("Opção 3 já foi selecionada anteriormente.")

# def option4():
#     global option4_selected
#     if not option4_selected:
#         print("Você selecionou a Opção 4 - Consultar Incidência por KM")
#         item = input("Qual item você quer verificar a incidência: ")
#         km_maior_incidencia, incidencia = Results.encontrar_maior_incidencia(item)
#         print(f"O quilômetro com maior incidência de {item} é: {km_maior_incidencia}, com {incidencia} ocorrências.")
#         option4_selected = True
#     else:
#         print("Opção 4 já foi selecionada anteriormente.")



