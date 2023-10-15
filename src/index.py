import CRUD_leite

mainCrud = CRUD_leite.mainCrud()

if not mainCrud.Conectar():
    print("OKAY")

else:
    while (True):
        codigo_escolhido = int(input("\nO QUE VOCE DESEJA?\n"
                                     "1-ADICIONAR UMA PRODUCÃO DE LEITE\n"
                                     "2-LISTAR TODAS AS PRODUÇÕES DE LEITE\n"
                                     "3-LISTAR POR QUANTIDADE DE LITROS\n"
                                     "4-LISTAR AS PRODUÇÕES POR DATA\n"
                                     "5-ATUALIZAR UMA PRODUCÃO DE LEITE\n"
                                     "6-DELETAR UMA PRODUCÃO DE LEITE\n"
                                     "7-Sair\n"))

        match codigo_escolhido:
            case 1:
                mainCrud.Create()

            case 2:
                mainCrud.Read()

            case 3:
                mainCrud.ReadLitros()

            case 4:
                mainCrud.ReadData()

            case 5:
                mainCrud.Update()

            case 6:
                mainCrud.Delete()

            case 7:
                mainCrud.Desconectar()
                break

            case _:
                print("COMANDO INVALIDO, ESCOLHA UMA DAS OPÇÕES")
