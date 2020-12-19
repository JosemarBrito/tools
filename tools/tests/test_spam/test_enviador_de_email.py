import pytest

from tools.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador= Enviador()
    assert enviador is not None

@pytest.mark.parametrize(
    'destinatario',
    ['josemarbritosantos@gmail.com', 'estudos.josemarbrito@gmail.com']
                         )
def test_remetente(destinatario):
    enviador = Enviador()

    resultado=enviador.enviar(
        destinatario,
        'brito.souza@hotmail.com',
        'Curso Python Pro',
        'Aula de Pytools Python Pro'
    )
    assert destinatario in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'estudos.josemarbrito']
                         )
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'brito.souza@hotmail.com',
            'Curso Python Pro',
            'Aula de Pytools Python Pro'
    )

