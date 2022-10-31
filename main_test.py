from main import validate_cnpj
from gerador_cnpj import generate_cnpj

def testando_cnpj():
    cnpj = generate_cnpj()
    assert validate_cnpj(cnpj) == cnpj
    print('\n' + cnpj)
