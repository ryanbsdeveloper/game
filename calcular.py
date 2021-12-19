from random import randint
from time import sleep
from typing import Union


class Calcular:

    def __init__(self: object, dificuldade: int, /) -> None:
        self.__dificuldade: int = dificuldade
        self.__valor1: int = self._gerar_valor
        self.__valor2: int = self._gerar_valor
        self.__operacao: int = randint(1, 3)  # 1 = somar, 2 = diminuir, 3 = multiplicar
        self.__resultado: int = self._gerar_resultado

    @property
    def dificuldade(self: object) -> int:
        return self.__dificuldade

    @property
    def valor1(self: object) -> int:
        return self.__valor1

    @property
    def valor2(self: object) -> int:
        return self.__valor2

    @property
    def operacao(self: object) -> int:
        return self.__operacao

    @property
    def resultado(self: object) -> int:
        return self.__resultado

    def __str__(self: object) -> str:
        op: str = ''
        if self.operacao == 1:
            op = 'Somar'
        elif self.operacao == 2:
            op = 'Diminuir'
        elif self.operacao == 3:
            op = 'Multiplicar'
        else:
            op = 'Operação desconhecida'
        return f'Valor 1: {self.valor1} \nValor 2: {self.valor2} \nDificuldade: {self.dificuldade} \nOperação: {op}'

    @property
    def _gerar_valor(self: object) -> Union[str, int]:
        if self.dificuldade == 1:
            return randint(0, 10)
        elif self.dificuldade == 2:
            return randint(0, 100)
        elif self.dificuldade == 3:
            return randint(0, 1000)
        elif self.dificuldade == 4:
            return randint(0, 10000)
        elif self.dificuldade == 5:
            return randint(0, 100000)
        else:
            sleep(2)
            exit('Operação não existente!')

    @property
    def _gerar_resultado(self: object) -> int:
        if self.operacao == 1:  # somar
            return self.valor1 + self.valor2
        elif self.operacao == 2:  # diminuir
            return self.valor1 - self.valor2
        elif self.operacao == 3:  # multiplicar
            return self.valor1 * self.valor2

    @property
    def _op_simbolo(self: object) -> str:
        if self.operacao == 1:
            return '+'
        elif self.operacao == 2:
            return '-'
        else:
            return '*'

    def checar_resultado(self: object, resposta: int) -> bool:
        certo: bool = False
        if self.resultado == resposta:
            print()
            sleep(1)
            print('\033[32mResposta correta\033[m!')
            print()
            certo = True
        else:
            print()
            sleep(2)
            print('\033[31mResposta errada\033[m!')
            print()
        sleep(1)
        print(f'{self.valor1} {self._op_simbolo} {self.valor2} = {self.resultado}')
        sleep(1)
        print()
        return certo

    def mostra_operacao(self: object) -> None:
        print(f'{self.valor1} {self._op_simbolo} {self.valor2} = ?')
        print()
