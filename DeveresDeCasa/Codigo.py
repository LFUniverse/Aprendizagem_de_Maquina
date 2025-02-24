import pandas as pd
import os

# Obtendo o caminho da pasta Downloads do usuário e o nome do arquivo
caminho_downloads = os.path.join(os.path.expanduser("~"), "Downloads", "MeuCSV.csv")

# Verificar se o arquivo existe na pasta Downloads
if not os.path.exists(caminho_downloads):
    print(f"Arquivo não encontrado na pasta Downloads: {caminho_downloads}")
else:
    try:
        # Ler o arquivo CSV
        df = pd.read_csv(caminho_downloads)

        # Solicitar ao usuário o número do registro desejado
        n = int(input(f"Digite o número do registro (0 a {len(df)-1}): "))
        if n < 0 or n >= len(df):
            print("Número de registro inválido.")
        else:
            # Converter as datas para o formato brasileiro (DD/MM/AAAA)
            data_nascimento = pd.to_datetime(df.loc[n, "Data de Nascimento"]).strftime("%d/%m/%Y")
            dia_cadastro = pd.to_datetime(df.loc[n, "Dia do Cadastro"]).strftime("%d/%m/%Y")
            hora_cadastro = df.loc[n, "Hora de Cadastro"]

            # Criar a saída concatenada
            registro_formatado = f"{df.loc[n, 'Nome']}, {data_nascimento}, {dia_cadastro}, {hora_cadastro}"
            print("Registro:", registro_formatado)
    
    except ValueError:
        print("Por favor, digite um número válido.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
