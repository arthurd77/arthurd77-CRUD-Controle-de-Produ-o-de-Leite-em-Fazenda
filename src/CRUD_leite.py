import mysql.connector
import datetime
from tabulate import tabulate


class Crud:
    host = "localhost"
    usuario = "root"
    senha = "root"
    banco = "bubalinocultura"
    mydb = mysql.connector

    def Conectar(self):
        try:
            self.mydb = self.mydb.connect(
                host=self.host,
                user=self.usuario,
                password=self.senha,
                database=self.banco
            )

            return True

        except BaseException as e:
            if (str(e) == "1049 (42000): Unknown database 'bubalinocultura'"):
                print("o Banco de dados 'bubalinocultura' não foi criado!")
                return False

    def Desconectar(self):
        if self.mydb.is_connected():
            print("DESCONECTANDO...")
            self.mydb.close()

    def ShowLote(self):
        cursor = self.mydb.cursor()

        sql = f"SELECT * from lote WHERE ocupacao = %s"

        values = ("leite",)
        cursor.execute(sql, values)

        resultado = cursor.fetchall()

        dados = [
            ["CODIGO LOTE", "OCUPACAO", "METROS QUADRADOS", "QUANTIDADE BUBALINOS"]
        ]
        estilo = "fancy_grid"
        tabela_formatada = tabulate(dados, headers="firstrow", tablefmt=estilo)
        for linha in resultado:
            dados.append(list(linha))

        formato = tabulate(dados, headers="firstrow", tablefmt=estilo)
        print(formato)

    def ShowBubalino(self):
        cursor = self.mydb.cursor()

        sql = f"select c.* from bubalino c, lote l where c.lote_cod_lote = l.cod_lote and l.ocupacao = 'leite' and c.status='vivo';"

        cursor.execute(sql)

        resultado = cursor.fetchall()

        dados = [
            ["CODIGO_ANIMAL", "DATA_NASCIMENTO", "STATUS_VACINACAO", "PESO_NASCIMENTO", "RACA_COD_RACA",
             "LOTE_COD_LOTE", "STATUS"]
        ]
        estilo = "fancy_grid"
        for linha in resultado:
            dados.append(list(linha))

        formato = tabulate(dados, headers="firstrow", tablefmt=estilo)
        print(formato)

    def Create(self):
        try:
            cursor = self.mydb.cursor()
            now = datetime.datetime.now()

            dataHora = now.strftime("%Y-%m-%d")
            opcao_qualidade = int(input("Qual é a qualidade do leite ?\n1-boa\n2-Inconsumível\n"))
            qualidade_leite = ''
            match (opcao_qualidade):
                case 1:
                    qualidade_leite = "boa"
                case 2:
                    qualidade_leite = "inconsumível"

            quantidade_litros = float(input("Qual foi a quantidade de litros coletada ?\n"))
            print("LISTA LOTES")
            self.ShowLote()
            lote_cod_lote = int(input("Qual é o código do lote? \n"))
            print("LISTA BUBALINOS")
            self.ShowBubalino()
            bubalino = int(input("Qual é o código do bubalino? \n"))
            sql = "INSERT INTO producao_leite (data_coletada, qualidade_do_leite, quantidade_litros, lote_cod_lote, bubalino_codigo_animal) values (%s, %s, %s, %s, %s)"
            values = (dataHora, qualidade_leite, quantidade_litros, lote_cod_lote, bubalino)
            cursor.execute(sql, values)
            self.mydb.commit()

            print(cursor.rowcount, "TUPLAS ADICIONADAS\n")

        except BaseException as erro:
            print(erro)

    def Read(self):
        cursor = self.mydb.cursor()
        sql = "SELECT * FROM producao_leite"
        cursor.execute(sql)
        resultado = cursor.fetchall()

        if (len(resultado) == 0):
            print("Não há produções registradas")
        dados = [
            ["ID", "DATA", "QUALIDADE DO LEITE", "QUANTIDADE LITROS", "LOTE", "ANIMAL"]
        ]
        estilo = "fancy_grid"
        tabela_formatada = tabulate(dados, headers="firstrow", tablefmt=estilo)
        for linha in resultado:
            dados.append(list(linha))

        formato = tabulate(dados, headers="firstrow", tablefmt=estilo)
        print(formato)

    def ReadLitros(self):
        cursor = self.mydb.cursor()
        quantidade = int(input("QUAL A QUANTIDADE DE LITROS?\n"))
        sql = f"SELECT * from producao_leite WHERE quantidade_litros >= {quantidade}"
        values = (quantidade,)
        cursor.execute(sql)

        print(f"MOSTRANDO AS PRODUÇÕES ONDE A QUANTIDADE DE LITROS FOI MAIOR OU IGUAL A {quantidade} litros")

        resultado = cursor.fetchall()

        if (len(resultado) == 0):
            print("AINDA NÃO EXISTEM PRODUÇÕES COM A QUANTIDADE ESCOLHIDA")
        dados = [
            ["ID", "DATA", "QUALIDADE DO LEITE", "QUANTIDADE LITROS", "LOTE", "ANIMAL"]
        ]
        estilo = "fancy_grid"
        tabela_formatada = tabulate(dados, headers="firstrow", tablefmt=estilo)

        for linha in resultado:
            dados.append(list(linha))

        formato = tabulate(dados, headers="firstrow", tablefmt=estilo)
        print(formato)

    def ReadData(self):
        mycursor = self.mydb.cursor()
        dia = input("qual dia?")
        mes = input("Qual mês?")
        ano = input("Qual ano?")
        data = f"{ano}-{mes}-{dia}"
        sql = f"SELECT * from producao_leite WHERE data_coletada = %s"
        valor = (data,)
        mycursor.execute(sql, valor)

        resultado = mycursor.fetchall()
        dados = [
            ["ID", "DATA", "QUALIDADE DO LEITE", "QUANTIDADE LITROS", "LOTE", "ANIMAL"]
        ]
        estilo = "fancy_grid"
        for linha in resultado:
            dados.append(list(linha))

        formato = tabulate(dados, headers="firstrow", tablefmt=estilo)
        print(formato)

    def Update(self):
        try:
            mycursor = self.mydb.cursor()
            print("\nLISTA BUBALINOS:")
            self.Read()
            codigo = int(input("QUAL CODIGO DA PRODUCAO VOCÊ DESEJA MODIFICAR ?\n"))

            opcao_qualidade = int(input("Qual é a qualidade do leite ?\n1-boa\n2-Inconsumível\n"))
            qualidade_leite = ''
            match (opcao_qualidade):
                case 1:
                    qualidade_leite = "boa"
                case 2:
                    qualidade_leite = "inconsumível"
            quantidade_litros = float(input("Qual foi a quantidade de litros coletada ? \n"))
            print("LISTA LOTES")
            self.ShowLote()
            lote_cod_lote = int(input("Qual é o código do lote? \n"))
            print("LISTA BUBALINOS")
            self.ShowBubalino()
            bubalino = int(input("Qual é o código do bubalino? \n"))

            self.ShowBubalino()

            sql = "UPDATE producao_leite SET qualidade_do_leite = %s, quantidade_litros = %s, lote_cod_lote = %s, bubalino_codigo_animal = %s where codigo = %s"
            values = (qualidade_leite, quantidade_litros, lote_cod_lote, bubalino, codigo)

            mycursor.execute(sql, values)

            self.mydb.commit()

            print(mycursor.rowcount, "TUPLAS ATUALIZADAS \n")
        except BaseException as erro:
            print(erro)

    def Delete(self):
        mycursor = self.mydb.cursor()

        codigo = int(input("QUAL O CODIGO DA PRODUCAO DE LEITE QUE VOCÊ DESEJA EXCLUIR \n"))
        sql = "DELETE FROM producao_leite where codigo= %s"

        mycursor.execute(sql, (codigo,))

        self.mydb.commit()

        print(mycursor.rowcount, "TUPLAS EXCLUIDAS \n")


mainCrud = Crud()

if (mainCrud.Conectar()):

    while (True):
        codigo_escolhido = int(input("\nO QUE VOCE DESEJA?\n"
                                     "1-ADICIONAR UMA PRODUCÃO DE LEITE\n"
                                     "2-LISTAR TODAS AS PRODUÇÕES DE LEITE\n"
                                     "3-LISTAR POR QUANTIDADE DE LITROS\n"
                                     "4-LISTAR POR DATA\n"
                                     "5-ATUALIZAR UMA PRODUCAO DE LEITE\n"
                                     "6-DELETAR UMA PRODUCAO DE LEITE\n"
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
