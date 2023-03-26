from codigo.bytebank import Funcionario

def teste_idade():
    funcionario_teste = Funcionario('Funcionario Teste','13/04/2000', 1111)
    print(f'Teste = {funcionario_teste.idade()}')

    funcionario_teste = Funcionario('Funcionario Teste','13/04/1999', 1111)
    print(f'Teste = {funcionario_teste.idade()}')

    funcionario_teste = Funcionario('Funcionario Teste','13/04/1945', 1111)
    print(f'Teste = {funcionario_teste.idade()}')
teste_idade()