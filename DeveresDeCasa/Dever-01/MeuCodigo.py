import pandas as pd

def format_date(date_str, current_format, desired_format):
    return pd.to_datetime(date_str, format=current_format).strftime(desired_format)

def read_csv_and_print_record():
    # Lendo o arquivo CSV
    df = pd.read_csv('MeuCSV.csv', sep=';')
    
    # Ajustando os formatos das datas
    df['Data de Nascimento'] = df['Data de Nascimento'].apply(lambda x: format_date(x, '%m/%d/%Y', '%d/%m/%Y'))
    df['Dia do Cadastro'] = df['Dia do Cadastro'].apply(lambda x: format_date(x, '%d/%m/%Y', '%d/%m/%Y'))
    
    # Solicitando ao usuário o número do registro
    registro = int(input("Digite o número do registro que deseja visualizar: "))
    
    if 1 <= registro <= len(df):
        linha = df.iloc[registro - 1]
        print(f"Registro {registro}: Nome: {linha['Nome']}; Data de nascimento: {linha['Data de Nascimento']}; Data de cadastro: {linha['Dia do Cadastro']} às {linha['Hora de Cadastro']} horas")
    else:
        print("Número de registro inválido.")

if __name__ == "__main__":
    read_csv_and_print_record()
