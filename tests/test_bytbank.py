from codigo.bytebank import Funcionario

class TestClass:
    def test_quando_idade_recebe_31_03_200_deve_retornar_22(self):
        #Given (contexto)
        entrada = '13/03/2000'
        esperado = 23

        #When (como)
        funcionario_teste = Funcionario('Funcionario Teste', entrada, 1111)
        resultado = funcionario_teste.idade()

        #Then (desfecho)
        assert resultado == esperado
