from codigo.bytebank import Funcionario
import pytest
from pytest import mark


class TestClass:
    def test_quando_idade_recebe_31_03_200_deve_retornar_22(self):
        # Given (contexto)
        entrada = '13/03/2000'
        esperado = 23

        # When (como)
        funcionario_teste = Funcionario('Funcionario Teste', entrada, 1111)
        resultado = funcionario_teste.idade()

        # Then (desfecho)
        assert resultado == esperado

    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retorna_Carvalho(self):
        # Given (contexto)
        entrada = 'Lucas Carvalho'
        esperado = 'Carvalho'

        # When (como)
        lucas = Funcionario(entrada, '13/03/2000', 1111)
        resultado = lucas.sobrenome()

        # Then (desfecho)
        assert resultado == esperado

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        # Given
        entrada = 100000
        entrada_nome = 'Paulo Bragança'
        esperado = 90000

        # when
        funcionario_teste = Funcionario(entrada_nome, '11/11/2000', entrada)
        funcionario_teste.decrescimo_salario()
        resultado = funcionario_teste.salario

        # Then
        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        # Given
        entrada = 1000
        esperado = 100

        # When
        funcionario_teste = Funcionario('entrada nome', '11/11/2000', entrada)
        resultado = funcionario_teste.calcular_bonus()

        # Then
        assert esperado == resultado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_100000000_deve_retorna_exception(self):
        with pytest.raises(Exception):
            entrada = 100000000

            funcionario_teste = Funcionario('entrada nome', '11/11/2000', entrada)
            resultado = funcionario_teste.calcular_bonus()

            assert resultado

    # def test_retorno_str(self):
    #     # Given
    #     nome, data_nascimento, salario = 'Teste', '12/03/2000', 1000
    #     esperado = 'Funcionario(Teste, 12/03/2000, 1000)'

    #     # When
    #     funcionario_teste = Funcionario(nome, data_nascimento, salario)
    #     resultado = funcionario_teste.__str__()

    #     # Then
    #     assert resultado == esperado
