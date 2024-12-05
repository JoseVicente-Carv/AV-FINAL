from dataclasses import dataclass
from projeto.funcionario import Funcionario

@dataclass
class Nutricionista(Funcionario):
    crn : str
    
    def salario_final(self):
        return