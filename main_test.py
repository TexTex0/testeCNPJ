from main import validate_cnpj
from gerador_cnpj import generate_cnpj

def testando_cnpj():
    cnpj = generate_cnpj()  # PODE DEIXAR GERAR UM CNPJ AUTOMATICAMENTE OU SUBSTITUIR O GENERATE_CNPJ() POR UM CNPJ DA SUA ESCOLHA, MELHORIAS SEMPRE BEM-VINDAS
    assert validate_cnpj(cnpj) == cnpj
    print('\n' + cnpj)
