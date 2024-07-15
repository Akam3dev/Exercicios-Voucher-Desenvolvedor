from Pessoa import Pessoa
from Aluno import Aluno
from Professor import Professor

generica = Pessoa(54,"Hagamenon Gonçalves", 36)
generica.GetDados()

joao = Aluno(73,"João Almeida", 17, [6,5,7,8,4,6])
joao.estudar()
joao.media()

thiago = Professor(213, "Thiago Almeida", 25, "TODAS", 40, 12000)
thiago.lecionar()
thiago.GetDados()