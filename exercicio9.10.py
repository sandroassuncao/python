altura = float(input('altura da parede: '))
largura = float(input('largura da parede: '))
area = altura * largura
print('Sua parede tem a dimensão de {} x {} e sua area é {} m².'.format (altura, largura, area))
tinta = area / 2
print('Para pintar essa parede, você precisará de {} l de tinta.'.format(tinta))