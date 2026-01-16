def copy_file(command: str) -> None:
    # Divide a string em partes: ['cp', 'origem', 'destino']
    parts = command.split()

    # Verifica se o comando é válido e possui os argumentos necessários
    if len(parts) != 3 or parts[0] != "cp":
        return

    file_in_name = parts[1]
    file_out_name = parts[2]

    # Regra: Não fazer nada se o nome do arquivo for o mesmo
    if file_in_name == file_out_name:
        return

    # Utiliza dois gerenciadores de contexto simultaneamente
    with open(file_in_name, "r") as file_in, \
            open(file_out_name, "w") as file_out:
        file_out.write(file_in.read())
