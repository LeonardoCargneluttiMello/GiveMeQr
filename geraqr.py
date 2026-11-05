from pathlib import Path
from datetime import datetime
import random
import qrcode

def gera_qr(link):
    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)

    terminal(qr)
    opcao = input(f"quer salvar {link} como imagem?[s/n]\n").lower()

    if opcao == "s":
        formato = input("digite o formato(PNG, JPEG, GIF, BMP, WEBP, TIFF, ICO)\n").lower()
        para_imagem(qr, formato)
    return qr


def pede_link(mensagem):
    while True:
        texto = input(mensagem).strip()
        if not texto:
            print("O link está vazio!")
            continue
        return texto


def para_imagem(qr, formato):
    img = qr.make_image(fill_color="black", back_color="white")
    data = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    numero = random.randint(99999, 9999999)
    nome = f"qr_{data}-{numero}.{formato.lower()}"

    try:
        img.save(nome)

    except (ValueError, OSError):
        print(f"\nNão consegui salvar como '{formato}'.")
        print("Formatos que costumam funcionar: PNG, JPEG, GIF, BMP, WEBP, TIFF.")

    else:
        caminho = Path(nome).resolve()
        print(f"salvo em {caminho}\n")
        opc = input("quer abrir essa imagem?[s/n]\n")

        if opc == "s":
            img.show()


def terminal(qr):
    qr.print_ascii(invert=True)


def main():
    print("github: https://github.com/LeonardoCargneluttiMello\n")
    ops = input("quer gerar mais de um qr em sequência?[s/n]\n").lower()

    if ops == "n":
        link = pede_link("GERADOR DE QR CODE\nDIGITE SEU LINK:\n")
        gera_qr(link)

    else:
        links = []
        while True:
            add = pede_link("DIGITE UM LINK (ou *fim* para terminar):\n")

            if add.lower() == "fim":
                break
            links.append(add)
        for link in links:
            gera_qr(link)

            
if __name__ == "__main__":
       main()