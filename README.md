# 🧮 Calculadora Inteligente em Python

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Concluído-green)
![Licença](https://img.shields.io/badge/Licença-MIT-orange)

## 📋 Sobre o Projeto

Calculadora desenvolvida em Python durante meus estudos de lógica de programação. O projeto vai além de uma calculadora comum, oferecendo 11 funcionalidades diferentes e tratamento de erros para garantir uma boa experiência do usuário.

## 🚀 Funcionalidades

| Opção | Função | Descrição |
|-------|--------|-----------|
| [ 1 ] | Média Escolar | Calcula a média de várias notas |
| [ 2 ] | Soma | Soma múltiplos números |
| [ 3 ] | Subtração | Subtrai múltiplos números |
| [ 4 ] | Multiplicação | Multiplica múltiplos números |
| [ 5 ] | Divisão | Divide múltiplos números com validação |
| [ 6 ] | Radiciação | Calcula raiz quadrada |
| [ 7 ] | Potência | Eleva um número a um expoente |
| [ 8 ] | Fatoração | Calcula o fatorial de um número |
| [ 9 ] | Seno | Calcula o seno de um ângulo |
| [ 10 ] | Cosseno | Calcula o cosseno de um ângulo |
| [ 11 ] | Finalizar | Encerra o programa |

## 🛠️ Tecnologias Utilizadas

- Python 3
- Biblioteca `math` (operações matemáticas)
- Biblioteca `time` (controle de fluxo)

## 🎯 O que eu aprendi

- ✅ Estruturas de repetição (`while`, `for`)
- ✅ Condicionais (`if/elif/else`)
- ✅ Manipulação de variáveis e tipos
- ✅ Tratamento de erros básico
- ✅ Importação e uso de módulos
- ✅ Validação de entrada do usuário
- ✅ Organização de código limpo

## 🔍 Destaques do Código

### Tratamento de erro na divisão
```python
'''if cont <= 1 and numero == 0:
    while True:
        print('erro!!!!')
        numero = float(input('digite o numero novamente: '))
        if numero != 0:
            break'''

Impede divisão por zero solicitando um novo número

📦 Como executar
Certifique-se de ter o Python instalado

Clone este repositório:

git clone https://github.com/GabrielRSJ/Calculadora_inteligente-v1.git

cd Calculadora_inteligente-v1

python calculadora.py

💡 Exemplo de Uso

-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    [  1 ] media escolar
    [  2 ] soma
    [  3 ] subtração
    [  4 ] mutiplicação
    [  5 ] divisão
    [  6 ] radiciação/raiz quadrada
    [  7 ] potencia
    [  8 ] fatoração
    [  9 ] seno
    [ 10 ] cosseno
    [ 11 ] finalizar
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
digite sua opcao: 8
Digite o numero que você quer fatorar: 5
5 x 4 x 3 x 2 x 1 = 120

🔮 Próximas Melhorias (To-Do)
Adicionar validação para raiz de número negativo

Adicionar validação para fatorial de número negativo

Implementar histórico das últimas operações

Criar opção para limpar a tela

Salvar operações em arquivo .txt

Refatorar código usando funções

📫 Contato
[![GitHub](https://img.shields.io/badge/-GitHub-000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/GabrielRSJ)
