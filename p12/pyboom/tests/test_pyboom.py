# Pruebas de Pyboom.
import pytest

from pyboom import pyboom


def test_atacar_rotruvia(capfd):

    print(pyboom.atacar())
    out, err = capfd.readouterr()
    assert "Rotruvia Central" in out


@pytest.mark.xfail
def test_no_atacar_tierra_salvaje(capfd):

    print(pyboom.atacar())
    out, err = capfd.readouterr()
    assert "Norte" in out
