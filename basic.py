def funcao_1(cadastro):
    print("Função 1 {nome}".format(**cadastro))

def funcao_2(cadastro):
    print("Função 2 {nome} {Sobrenome}".format(**cadastro))

if __name__ == '__main__':
    dicionario = {
        "Funcao1":funcao_1,
        "Funcao2":funcao_2
    }
    cadastro = {
        "nome":"Homer"
    }
    dicionario['Funcao1'](cadastro)
    cadastro["Sobrenome"] = "Simpson"
    dicionario['Funcao2'](cadastro)
