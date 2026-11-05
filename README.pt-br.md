# GiveMeQr

[English](README.md) | Português (Brasil)

Gerador de QR Codes em Python, executado pelo terminal. Informe um link, visualize o QR Code em ASCII e, se quiser, salve o resultado como imagem.

## Funcionalidades

- Geração de um QR Code ou de vários em sequência.
- Visualização diretamente no terminal.
- Exportação de imagens com fundo branco e QR Code preto.
- Nomes de arquivo com data, hora e número aleatório.
- Opção de abrir a imagem após salvar.
- Verificação de entradas vazias e tratamento de erros ao salvar formatos inválidos.

## Requisitos

- Python 3 e `pip` disponíveis no sistema.
- Dependência declarada em `requirements.txt`: `qrcode[pil]`, com suporte a imagens via Pillow.
- Um visualizador de imagens disponível caso queira usar a opção de abrir o arquivo.

## Instalação e execução

Baixe o projeto pelo GitHub ou clone o repositório. Abra um terminal dentro da pasta que contém `geraqr.py` e `requirements.txt`.

### Windows (PowerShell)

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe geraqr.py
```

Se o comando `py` não estiver disponível, use `python` no primeiro comando.

### Linux e macOS

```bash
python3 -m venv .venv
./.venv/bin/python -m pip install -r requirements.txt
./.venv/bin/python geraqr.py
```

Os comandos usam o Python do ambiente virtual diretamente, sem necessidade de ativá-lo. No Linux, se a criação do ambiente informar que o módulo `venv` não está disponível, instale o pacote correspondente à sua distribuição e tente novamente.

## Como usar

### Gerar um único QR Code

1. Execute o programa.
2. Responda `n` à pergunta `quer gerar mais de um qr em sequência?`.
3. Digite o link desejado.
4. Veja o QR Code no terminal.
5. Responda `s` para salvar como imagem ou `n` para encerrar sem salvar.
6. Se escolher salvar, digite o formato, por exemplo `png`.
7. Após salvar, responda `s` se quiser abrir a imagem.

### Gerar vários QR Codes

1. Execute o programa e responda `s` à primeira pergunta.
2. Digite um link por vez, pressionando Enter após cada um.
3. Digite `fim` para terminar a lista, sem os asteriscos exibidos no prompt.
4. O programa gera os QR Codes na ordem informada e pergunta separadamente se deseja salvar cada um.

### Exemplo de entrada

Para gerar um único QR Code e salvá-lo em PNG, sem abrir a imagem, forneça estas respostas aos prompts, uma por vez:

```text
n
https://example.com
s
png
n
```

## Arquivos gerados

As imagens são salvas na pasta de onde o programa foi executado, que pode ser diferente da pasta do script. O caminho completo é exibido após salvar.

Exemplo de nome:

```text
qr_2026-01-15_14-30-00-123456.png
```

O prompt oferece `PNG`, `JPEG`, `GIF`, `BMP`, `WEBP`, `TIFF` e `ICO`. A gravação depende do suporte do Pillow ao formato e ao modo da imagem; se houver erro, o programa informa a falha. Use `png` como primeira opção.

## Observações

- O programa rejeita entradas vazias, mas não valida se o conteúdo é uma URL nem se o endereço está acessível.
- Também é possível informar um texto em vez de um link.
- A visualização no terminal pode variar conforme a fonte, as cores e o espaço disponível. Se necessário, use a imagem salva.
- A abertura automática da imagem depende do ambiente e do visualizador disponível no sistema.

## Estrutura do projeto

```text
GiveMeQr/
├── geraqr.py         # Programa e interação pelo terminal
├── requirements.txt  # Dependência do projeto
├── README.md         # Documentação em inglês
└── README.pt-br.md   # Documentação em português (Brasil)
```

## Autor

[Leonardo Cargnelutti Mello](https://github.com/LeonardoCargneluttiMello)
