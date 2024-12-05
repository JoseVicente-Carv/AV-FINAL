from dataclasses import dataclass
from projeto.funcionario import Funcionario

@dataclass
class Engenheiro(Funcionario):
    crea: str

    def salario_final(self):
        return