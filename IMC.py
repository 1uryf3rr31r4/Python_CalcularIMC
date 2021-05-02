import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        layout = [
            [sg.Text('Peso'), sg.Input()],
            [sg.Text('Altura'), sg.Input()],
            [sg.Button('Calcuclar')]
        ]

        janela = sg.Window('Calculadora de IMC').layout(layout)

        self.button, self.values = janela.read()

    def Iniciar(self):
        peso = float(self.values[0])
        altura = float(self.values[1])

        imc = peso / (altura * altura)

        if imc < 18:
                result = 'Consideradas pessoas de baixo peso'

        if imc > 18 and imc < 24:
                result = 'Para mulheres e entre 18-25 kg/m2 para homens - consideradas IMC de pessoas normais'

        if imc > 25 and imc < 30:
                result = 'Consideradas pessoas com sobrepeso'

        if imc > 30 and imc < 35:
                result = 'Pessoas obesas'

        if imc > 35 and imc < 40:
                result = 'Pessoas com obesidade moderada'

        if imc > 40:
                result = 'Pessoas com obesidade grave'

        if imc > 50:
                result = 'Pessoas com obesidade gravíssima'

        layoutFim = [
            [sg.Text('Resultado')],
            [sg.Text(int(imc)), sg.Text(result)]
        ]
        janela2 = sg.Window('Calculadora de IMC').layout(layoutFim)

        self.values = janela2.read()

tela = TelaPython()
tela.Iniciar()