## Capítulo 1 - A Jornada do Programa
Neste capítulo, aprendi sobre como um cientista da computação deve pensar e suas habilidades cruciais, além de conceitos inicais relacionados à programação e Python. O livro tem como objetivo ensinar a pensar como um cientista da computação.

**Algumas descobertas**
* Resolução de Problemas: Habilidade principal em que se aprende a arte de formular problemas, elaborar soluções criativas e conseguir expressar essa solução de formar clara.
* Programar é uma habilidade útil, mas serve, sobretudo, para exercitar a capacidade de Resolução de Problemas.
* Python é uma linguagem interpretada: um interpretador vai "traduzir" o código escrito na linguagem de alto nível para uma linguagem de baixo nível que o computador entende (0 e 1).
* Linguagens naturais servem para classificar os idiomas falados. Caractéristicas: redundância, dependente do contexto, cheia de metáforas
* Linguagens formais são usadas para aplicações específicas. Linguagem de programação é usada para denotar tarefas computacionais. São claras, sem redundância e independem da interpretação de fatores externos.

### O que é um programa?
**Programa:** conjunto de instruções que descrevem o passo a passo que o computador deve seguir para realizar um objetivo ou tarefa
**Instrução:** é um comando unitário que o computador executa

Qualquer programa de computador, por mais complicado que seja pode ser "quebrado" em pequenas partes e simplificado de tal forma que encontramos as seguintes instruções:  
**entrada** --> instruções que recebem dados, seja do teclado, de arquivos, ou de outros dispositivos  
**saída** --> instruções que podem exibir algo na tela para o usuário, que devolvem um texto, um arquivo ou envio de uma mensagem pela rede  
**processamento (matemática)** --> operações que ocorrem com os dados de entrada, transformando-os em dados diferentes  
**condicional** --> blocos de código que só são executados quando determinada condição é satisfeita  
**repetição** --> instruções que se repetem continuamente em um laço enquanto a condição de parada não é satisfeita (automatiza tarefas repetitivas)  

### O primeiro programa
``print("Hello, World")`` ==> instrução que imprime a mensagem **Hello, World** na tela  
print() é uma função. Reconhecemos uma função por causa dos parênteses (mais aprofundado no capítulo 2)

### Operadores Aritméticos
* soma (+) ==> 2+2 = 4
* subtração (-) ==> 2-5 = -3
* multiplicação (*) ==> 2\*5 = 10
* potenciação (**) ==> 5\**2 = 25
* divisão (/) ==> 10/2 = 5.0

### Valores e tipos
Valor é um dos principais recursos que o programa precisa para trabalhar. 42 e "olá" são valores.  
O valor pode ser classificado como sendo pertencente a um desses 4 tipos primitivos:
* str --> String. São uma sequência de letras. Podem ser escritas com aspas simples ou duplas.
* int --> usado para designar números inteiros
* float --> se classifica os números fracionários, também chamados decimais
* bool --> valores booleanos de True ou False.

### Debugging
Arte de encontrar e solucionar erros (bugs) encontrados nos algoritmos de programação. Habilidade bastante útil no mercado atualmente.

---

### Exercícios do Capítulo 1
**Exercício 1.1**  
É uma boa ideia ler este livro em frente a um computador para testar os exemplos durante a leitura.  
Sempre que estiver testando um novo recurso, você deve tentar fazer erros. Por exemplo, no programa “Hello, World!”, o que acontece se omitir uma das aspas? E se omitir ambas? E se você soletrar a instrução print de forma errada?  
Este tipo de experimento ajuda a lembrar o que foi lido; também ajuda quando você estiver programando, porque assim conhecerá o significado das mensagens de erro. É melhor fazer erros agora e de propósito que depois e acidentalmente.  
1. Em uma instrução print, o que acontece se você omitir um dos parênteses ou ambos?  
2. Se estiver tentando imprimir uma string, o que acontece se omitir uma das aspas ou ambas?  
3. Você pode usar um sinal de menos para fazer um número negativo como -2. O que acontece se puser um sinal de mais antes de um número? E se escrever assim: 2++2?  
4. Na notação matemática, zeros à esquerda são aceitáveis, como em 02. O que acontece se você tentar usar isso no Python?  
5. O que acontece se você tiver dois valores sem nenhum operador entre eles?  
**Respostas em:** [print_erros.py](./print_erros.py)

**Exercício 1.2**  
Inicialize o interpretador do Python e use-o como uma calculadora.  
1. Quantos segundos há em 42 minutos e 42 segundos?  
2. Quantas milhas há em 10 quilômetros? Dica: uma milha equivale a 1,61 quilômetro.  
3. Se você correr 10 quilômetros em 42 minutos e 42 segundos, qual é o seu passo médio (tempo por milha em minutos e segundos)? Qual é a sua velocidade média em milhas por hora?  
---
