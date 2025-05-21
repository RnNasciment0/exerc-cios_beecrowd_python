frangoDisponivel, bifeDisponivel, massaDisponivel = map(int, input().split())
frangoPedido, bifePedido, massaPedido = map(int, input().split())
faltou = 0
if frangoDisponivel < frangoPedido:
    faltou -= frangoDisponivel - frangoPedido
if bifeDisponivel < bifePedido:
    faltou -= bifeDisponivel - bifePedido
if massaPedido > massaDisponivel:
    faltou -= massaDisponivel - massaPedido
print(faltou)
