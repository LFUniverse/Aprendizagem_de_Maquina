def obter_frase():
    """Solicita ao usuário uma frase e garante que a entrada não esteja vazia."""
    while True:
        frase = input("Digite uma frase: ").strip()  # Remove espaços extras
        if frase:
            return frase  # Retorna a frase válida
        print("Entrada inválida! A frase não pode estar vazia.")


def analisar_frase(frase):
    """Realiza a análise da frase fornecida."""
    num_caracteres = len(frase)  # Conta o total de caracteres (incluindo espaços)
    palavras = frase.split()  # Divide a frase em palavras com base nos espaços
    num_palavras = len(palavras)  # Conta o número total de palavras
    maior_palavra = max(palavras, key=len) if palavras else ""  # Encontra a maior palavra
    
    return num_caracteres, num_palavras, maior_palavra, palavras


def manipular_frase(frase, palavras):
    """Realiza manipulações na frase, como inversão e alteração de caixa."""
    frase_invertida_caracteres = frase[::-1]  # Inverte a frase por caracteres
    frase_invertida_palavras = " ".join(reversed(palavras))  # Inverte a ordem das palavras
    frase_maiuscula = frase.upper()  # Converte a frase para maiúsculas
    frase_minuscula = frase.lower()  # Converte a frase para minúsculas
    tupla_palavras = tuple(palavras)  # Cria uma tupla com as palavras
    
    return (
        frase_invertida_caracteres,
        frase_invertida_palavras,
        frase_maiuscula,
        frase_minuscula,
        tupla_palavras
    )


def exibir_resultados(num_caracteres, num_palavras, maior_palavra, 
                      frase_invertida_caracteres, frase_invertida_palavras, 
                      frase_maiuscula, frase_minuscula, tupla_palavras):
    """Exibe os resultados formatados."""
    print("\nResultados da Análise:")
    print(f"Número total de caracteres: {num_caracteres}")
    print(f"Número total de palavras: {num_palavras}")
    print(f"Maior palavra: {maior_palavra}")
    print(f"Frase invertida (por caracteres): {frase_invertida_caracteres}")
    print(f"Frase invertida (por palavras): {frase_invertida_palavras}")
    print(f"Frase em maiúsculas: {frase_maiuscula}")
    print(f"Frase em minúsculas: {frase_minuscula}")
    print(f"Tupla de palavras: {tupla_palavras}")


def main():
    """Função principal para executar o programa."""
    frase = obter_frase()  # Solicita a frase ao usuário
    num_caracteres, num_palavras, maior_palavra, palavras = analisar_frase(frase)  # Realiza a análise
    resultados = manipular_frase(frase, palavras)  # Manipula a frase
    exibir_resultados(num_caracteres, num_palavras, maior_palavra, *resultados)  # Exibe os resultados


if __name__ == "__main__":
    main()  # Executa o programa
