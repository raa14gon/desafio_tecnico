# Atividade 1

def fibonacci_sequencia(n):
    sequencia = [0,1] 
    
    while sequencia[-1] < n:
        prox_valor = sequencia[-1] + sequencia[-2]
        sequencia.append(prox_valor)
    
    return sequencia
    

def esta_na_sequencia(n):
    sequencia = fibonacci_sequencia(n)

    if n in sequencia:
        return f"O número {n} pertence a sequência de Fibonacci"
    else:
        return f"O número {n} não pertence a sequência de Fibonacci"


valor = int(input("Informe um valor "))
resultado = esta_na_sequencia(valor)
print(resultado)

# Atividade 2

def verificar_letra_a(string):
    quantidade_a = string.count("a")
    quantidade_A = string.count("A")
    
    total = quantidade_a + quantidade_A
    
    if total > 0:
        return f"A letra 'a' ou 'A' ocorre {total} vezes na string"
    else:
        return f"A letra 'a' ou 'A' não foi encontrada na string"
    
    
usuario_string = input("Digite uma Palavra")
resultado = verificar_letra_a(usuario_string)
print(resultado)

# Atividade 3

indice = 12 
soma = 0 
k = 1 

while k < indice: 
    k = k + 1
    soma = soma + k
    
print(soma)


# Atividade 4 


def complete_sequences():
    
# Sequência a)
    seq_a = [1, 3, 5, 7]
    next_a = seq_a[-1] + 2  # A sequência é de números ímpares, incrementando de 2
    print(f'Sequência a): {seq_a} -> {next_a}')
    
    # Sequência b)
    seq_b = [2, 4, 8, 16, 32, 64]
    next_b = seq_b[-1] * 2  # A sequência é de números que dobram a cada passo
    print(f'Sequência b): {seq_b} -> {next_b}')
    
    # Sequência c)
    seq_c = [0, 1, 4, 9, 16, 25, 36]
    next_c = (len(seq_c))**2  # A sequência é de quadrados de números inteiros
    print(f'Sequência c): {seq_c} -> {next_c}')
    
    # Sequência d)
    seq_d = [4, 16, 36, 64]
    next_d = (len(seq_d) + 2)**2  # A sequência é de quadrados de números inteiros (2, 4, 6, 8...)
    print(f'Sequência d): {seq_d} -> {next_d}')
    
    # Sequência e)
    seq_e = [1, 1, 2, 3, 5, 8]
    next_e = seq_e[-1] + seq_e[-2]  # A sequência é a sequência de Fibonacci
    print(f'Sequência e): {seq_e} -> {next_e}')
    
    # Sequência f)
    seq_f = [2, 10, 12, 16, 17, 18, 19]
    next_f = seq_f[-1] + 1  # Parece que a sequência aumenta normalmente após 19
    print(f'Sequência f): {seq_f} -> {next_f}')

complete_sequences()

# Atividade 5 



