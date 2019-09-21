from src.leilao.dominio import Usuario, Lance, Leilao, Avaliador

gui = Usuario("Gui")
yuri = Usuario("Yuri")

lance_do_gui = Lance(gui, 200.0)
lance_do_yuri = Lance(yuri, 100.0)

leilao = Leilao("Celular")

leilao.lances.append(lance_do_yuri)
leilao.lances.append(lance_do_gui)

for lance in leilao.lances:
    print(f"O usuário {lance.usuario.nome} deu um lance de {lance.valor}")

avaliador = Avaliador()
avaliador.avalia(leilao)

print(f'Maior lance: {avaliador.maior_lance}')
print(f'Menor lance: {avaliador.menor_lance}')