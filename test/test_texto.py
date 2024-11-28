from app.texto import Texto

def test_imprimir():
    assert Texto.imprimir('ola mundo') == 'ola mundo'