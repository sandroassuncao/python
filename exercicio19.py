import random

def gerar_jogada(mao):
  """
  Gera uma jogada aleatória a partir de uma mão de cartas.

  Args:
    Mao: A mão de cartas da IA.

  Returns:
    Uma jogada, que pode ser uma carta, um curinga ou uma combinação.
  """

  jogada = None
  if len(mao) == 0:
    jogada = "bate"
  elif len(mao) == 1:
    jogada = mao[0]
  else:
    jogada = random.choice(mao)
  return jogada

def jogar_buraco(mao, adversario):
  """
  Joga uma partida de buraco contra um adversário.

  Args:
    Mao: A mão de cartas da IA.
    Adversario: A mão de cartas do adversário.

  Returns:
    O resultado da partida, que pode ser "ganhou", "perdeu" ou "empatou".
  """

  buraco = []
  pontos_ia = 0
  pontos_adversario = 0
  while True:
    jogada_ia = gerar_jogada(mao)
    jogada_adversario = gerar_jogada(adversario)

    if jogada_ia == "bate":
      if len(buraco) >= 10:
        pontos_ia += 10
      break
    elif jogada_ia == jogada_adversario:
      buraco.append(jogada_ia)
    elif isinstance(jogada_ia, tuple):
      if isinstance(jogada_adversario, tuple):
        if len(jogada_ia) >= len(jogada_adversario):
          pontos_ia += len(jogada_ia)
          buraco.extend(jogada_ia)
        else:
          pontos_adversario += len(jogada_adversario)
          buraco.extend(jogada_adversario)
      else:
        pontos_ia += len(jogada_ia)
        buraco.extend(jogada_ia)
    else:
      if isinstance(jogada_adversario, tuple):
        pontos_adversario += len(jogada_adversario)
        buraco.extend(jogada_adversario)
      else:
        pontos_ia += 1
        buraco.append(jogada_ia)

  if pontos_ia > pontos_adversario:
    return "ganhou"
  elif pontos_ia < pontos_adversario:
    return "perdeu"
  else:
    return "empatou"


# Exemplo de uso

mao_ia = [10, 5, 4, 3, 2]
mao_adversario = [9, 8, 7, 6, 5]

resultado = jogar_buraco(mao_ia, mao_adversario)

print(resultado)
