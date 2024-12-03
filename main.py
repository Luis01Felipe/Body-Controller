import comandos.left_joystick as left_joystick
import comandos.l3 as l3
import comandos.right_joystick as right_joystick
import comandos.r3 as r3
import comandos.botao_a as botao_a
import comandos.botao_x as botao_x
import comandos.botao_y as botao_y
import comandos.menu as menu
import comandos.lb as lb
import comandos.rb as rb
import comandos.lt as lt
import comandos.rt as rt

from utils.reconhecimento_voz import reconhecer_comando
from utils.rastreamento_movimentos import capturar_movimentos


def main():
    while True:
        # Capturar comando de voz
        comando_voz = reconhecer_comando()

        # Executar ações baseadas em voz
        if comando_voz == "corra":
            l3.ativar()
        elif comando_voz == "deslize":
            r3.ativar()
        elif comando_voz == "carrega":
            botao_x.ativar()
        elif comando_voz == "ferramenta":
            botao_y.ativar()
        elif comando_voz == "inventário":
            menu.abrir()
        elif comando_voz == "anterior":
            lb.ativar()
        elif comando_voz == "próxima":
            rb.ativar()
        elif comando_voz == "bam":
            rt.ativar()

        # Capturar movimentos
        movimentos = capturar_movimentos()
        left_joystick.movimentar(movimentos["cabeca"])
        right_joystick.movimentar(movimentos["mao_direita"])
        botao_a.checar_movimento_queixo(movimentos["queixo"])
        lt.checar_gesto_arma(movimentos["mao_direita"])


if __name__ == "__main__":
    main()
