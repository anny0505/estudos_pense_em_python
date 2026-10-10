# 1. Em uma instrução print, o que acontece se você omitir um dos parênteses ou ambos?
# Erro: SintaxError: '(' was never closed
# Quando faço essa ação no terminal, interpretador entende como código incompleto e aguarda o término
print("oi"

# 2. Se estiver tentando imprimir uma string, o que acontece se omitir uma das aspas ou ambas?
# Erro: SyntaxError: unterminated string literal (detected at line 6)
# Erro compatível com o que acontece no terminal. Interpretador espera o par que combine com as aspas duplas
# É como se eu não tivesse terminado corretamente o comando
print("oi)

# 3. Você pode usar um sinal de menos para fazer um número negativo como -2. O que acontece se puser um sinal de mais antes de um número? E se escrever assim: 2++2?
# Acontece a soma normalmente.
print(2 ++ 2)

# 4. Na notação matemática, zeros à esquerda são aceitáveis, como em 02. O que acontece se você tentar usar isso no Python?
# Erro: SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
# Esse erro de sintaxe ocorre em razão de reduzir redundância. Historicamente se usava 0 à esquerda para n° da base octal
# Devido a confusão das pessoas que viam o 010 como número 10 e não 8, Python determinou a ilegalidade do 0 à esquerda se
# não houver prefixo o.
print(02)

# 5. O que acontece se você tiver dois valores sem nenhum operador entre eles?
# Erro: SyntaxError: invalid syntax. Perhaps you forgot a comma?
# Interpretador não entende o que fazer com esses números. Espera operador ou separador entre os dois valores.
print (2 2)

# Se não tiver espaço entre eles, imprime o número normalmente.
print(22)

# Erro: SyntaxError: invalid syntax. Perhaps you forgot a comma?
# Não entende a instrução e o que deve ser feito. Espera operador ou separador entre os dois valores.
print(2 "casa")
