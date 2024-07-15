from Ingreso import Ingresso
from Vip import Vip

plebeu = Ingresso(200, "Economico")

plebeu.MostrarSetor()
plebeu.AlterarPreco(300)

rico = Vip(400, "Privilegiado", True, True, True)

rico.camarote()
rico.PegarBebida()