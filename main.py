from projeto.engenheiro import Engenheiro
from projeto.nutricionista import Nutricionista
from projeto.endereco import Endereco

# Instancie os objetos.
n1 = Nutricionista(
    nome="Marcelly",
    email = "marcelly28ray@gmail.com",
    crn = "85.6987.64",

    salario=8975.64,

    endereco=Endereco(
        logradouro="Avenida Doutor Couto Maia",
        numero = "54",
        complemento="Ao lado do curso de inglês CCAA"
    )
)
primeiroEngenheiro = Engenheiro()

# determine as caracteristicas do objeto "primeiroEngenheiro"
primeiroEngenheiro.nome = "Marcelo"

primeiroEngenheiro.email = "bunny1goal@gmail.com"
primeiroEngenheiro.crn = "87.8989.00"

primeiroEngenheiro.salario = 875.65

primeiroEngenheiro.endereco.logradouro = "Praça da piranha"
primeiroEngenheiro.endereco.numero = "63"
primeiroEngenheiro.endereco.complemento = "Em frente ao mercado."

primeiroEngenheiro.salario_final()