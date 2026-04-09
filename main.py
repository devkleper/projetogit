def process_message(message: str) -> None:
    print(f"message:{message}")


def avaliar_mensagem_comando(mensagem: str):
    pass


def main():

    comandos: list[str] = []

    project_name: str = "projetogit"
    print(f"Hello from {project_name}!")

    texto_usuario = " Ola mundo! "
    avaliar_mensagem_comando(texto_usuario)


if __name__ == "__main__":
    main()
