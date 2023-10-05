import os

caminho = r"/home/isabella/Área de trabalho/automação em python/002 - movedor de arquivos/Mover"

lista_arquivos = os.listdir("Mover")

for arquivo in lista_arquivos:
    if ".xlsx" in arquivo:
        if "Jan" in arquivo:
            os.rename(f"Mover/{arquivo}", f"Mover/Jan/{arquivo}")
        if "Fev" in arquivo:
            os.rename(f"Mover/{arquivo}", f"Mover/Fev/{arquivo}")
        if "Mar" in arquivo:
            os.rename(f"Mover/{arquivo}", f"Mover/Mar/{arquivo}")
