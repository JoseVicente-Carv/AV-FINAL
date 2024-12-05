from abc import ABC, abstractmethod
from dataclasses import dataclass
from projeto.endereco import Endereco

@dataclass
class Funcionario(ABC):
    nome : str
    email : str
    salario: float 
    endereco : Endereco

    @abstractmethod
    def salario_final(self):
        print("\tExibindo dados do funcionário {nome}:\n")

        print("E-mail: {email}")
        print("Endereço:")
        print("\tLogradouro: {Endereco.logradouro}")
        print("\tNúmero: {endereco.numero}")
        print("\tComplemento: {endereco.complemento}")
        
        print("Salário do funcionário: {salario}")
        pass