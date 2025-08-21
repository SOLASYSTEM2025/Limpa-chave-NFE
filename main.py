def limpar_chave(chave_com_espacos):
  
    return chave_com_espacos.replace(" ", "").replace("\r", "").replace("\n", "")

def main():
    print("Cole a chave NFe com espaços (ou digite 'sair' para encerrar):\n")
    while True:
        entrada = input("Chave: ").strip()
        if entrada.lower() == "sair":
            break
        chave_limpa = limpar_chave(entrada)
        print(f"Chave sem espaços: {chave_limpa}\n")

if __name__ == "__main__":
    main()
