from calcular import Calcular
from time import sleep


def main() -> None:
    pontos: int = 0
    jogar(pontos)


print('=' * 40)
print('JOGUINHO'.center(40))
print('=' * 40)
print()


def jogar(pontos: int) -> None:
    while True:   
        dificuldade: int = input('Informe o nivel de dificuldade desejado [1, 2, 3, 4 ou 5]: ')
        if dificuldade.isnumeric():
            dificuldade = int(dificuldade)
            break

    print()

    calc: Calcular = Calcular(dificuldade)

    print('Informe o resultado para a seguinte operação: ')
    sleep(1.5)
    calc.mostra_operacao()

    while True:
        resultado: int = (input('Resultado: '))
        if resultado.isnumeric():
            resultado = int(resultado)
            break

    if calc.checar_resultado(resultado):
        pontos += 1
        if pontos > 0:
            print(f'Você tem \033[32m{pontos}\033[m ponto(s).')
            print()

    continuar = ' '

    while True:
        continuar: str = str(input('Deseja continuar no jogo? '))[0].upper()
        print()

        if continuar == 'S':
            jogar(pontos)
        elif continuar == 'N':
            if pontos > 0:
                print(f'Você finalizou com \033[32m{pontos}\033[m ponto(s).')
                sleep(1)
                print()
                print('Até a próxima!')
                exit()
            else:
                print(f'Você finalizou com \033[31m{pontos}\033[m ponto(s).')
                sleep(1)
                print()
                print('Até a próxima!')
            exit()
        else:
            sleep(1.5)
            print('apenas sim ou não.')
            print()


if __name__ == '__main__':
    main()

