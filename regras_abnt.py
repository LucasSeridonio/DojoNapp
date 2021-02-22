def formatar_autor(autor):
    autor = autor.lower().split(' ')

    if len(autor) == 1:
        nome = autor[0].strip().upper()
        return nome

    if len(autor) <= 2:
        nome = autor[0].strip().capitalize()
        sobrenome = autor[1].strip().upper()
        return f'{sobrenome}, {nome}'

    if len(autor) <= 3:
        if autor[-1].strip().upper() in excessoes:
            nome = autor[0].strip().capitalize()
            sobrenome = f'{autor[1].strip().upper()} {autor[2].strip().upper()}'
            return f'{sobrenome}, {nome}'
        else:
            sobrenome = autor[2].strip().upper()
            nome = f'{autor[0].strip().capitalize()} {autor[1].strip().capitalize()}'

            for sufixo in minusculas:
                if nome.endswith(sufixo):
                    nome = nome.replace(sufixo, sufixo.lower())

            return f'{sobrenome}, {nome}'


excessoes = ["FILHO", "FILHA", "NETO", "NETA", "SOBRINHO", "SOBRINHA", "JUNIOR"]
minusculas = ["Da", "De", "Do", "Das", "Dos"]

# testes
assert formatar_autor('guimaraes') == 'GUIMARAES'
assert formatar_autor('Guimaraes') == 'GUIMARAES'
assert formatar_autor('gUImArAes') == 'GUIMARAES'
assert formatar_autor('Lucas Seridonio') == 'SERIDONIO, Lucas'
assert formatar_autor('lucas seridonio') == 'SERIDONIO, Lucas'
assert formatar_autor('Joao Silva Neto') == 'SILVA NETO, Joao'
assert formatar_autor('Joao Neto') == 'NETO, Joao'
assert formatar_autor('Joao Quinta Feira') == 'FEIRA, Joao Quinta'
assert formatar_autor('Joao da Silva') == 'SILVA, Joao da'
assert formatar_autor('Maria das Dores') == 'DORES, Maria das'
