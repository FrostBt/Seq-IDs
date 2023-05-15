sequences = [] # lista vazia para armazenar as sequências
while True:
    dna_seq = input("Insira uma sequência de DNA: ")
    dna_id = input("Insira um ID para a sequência: ")
    dna_desc = input("Insira uma breve descrição para a sequência (opcional): ")
    # adiciona a sequência, o ID e a descrição ao dicionário e, em seguida, à lista
    sequences.append({"ID": dna_id, "Sequência": dna_seq, "Descrição": dna_desc})
    cont = input("Deseja inserir mais alguma sequência? (S/N): ")
    if cont.upper() == "N":
        break
for seq in sequences:
    if not seq["ID"]: # verifica se o ID está em branco
        raise ValueError("O ID não pode estar em branco")
    if set(seq["Sequência"]) - set("ATCG"): # verifica se a sequência possui letras inválidas
        raise ValueError("A sequência de DNA deve conter apenas as letras 'A', 'T', 'C' e 'G'")
for seq in sequences:
    count_a = seq["Sequência"].count("A")
    count_t = seq["Sequência"].count("T")
    count_c = seq["Sequência"].count("C")
    count_g = seq["Sequência"].count("G")
    seq["Contagem"] = {"A": count_a, "T": count_t, "C": count_c, "G": count_g}
with open("sequences.fasta", "w") as fasta_file:
    for seq in sequences:
        header = f">{seq['ID']}|{seq['Descrição']}|A:{seq['Contagem']['A']}|T:{seq['Contagem']['T']}|C:{seq['Contagem']['C']}|G:{seq['Contagem']['G']}"
        fasta_file.write(f"{header}\n{seq['Sequência']}\n")