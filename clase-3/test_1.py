from calculadora import sumar, restar, multiplicar, dividir
import pytest

# ----- FIXTURES -----
@pytest.fixture
def numeros_enteros():
    """Prepara dos enteros comunes."""
    return 20, 5

@pytest.fixture
def numeros_decimales():
    """Prepara dos números decimales para pruebas de precisión."""
    return 0.1, 0.2

# ----- TESTS CON FIXTURES -----
def test_dividir_enteros(numeros_enteros):
    """Test que usa la fixture de números enteros para probar la división."""
    a, b = numeros_enteros
    assert dividir(a, b) == 4

def test_multiplicar_enteros(numeros_enteros):
    """Test que usa la fixture de números enteros para probar la multiplicación."""
    a, b = numeros_enteros
    assert multiplicar(a, b) == 100

def test_sumar_decimales(numeros_decimales):
    """Test que usa la fixture de números enteros para probar la multiplicación."""
    a, b = numeros_decimales
    assert sumar(a, b) == 1.0

@pytest.mark.parametrize(
    "a, b, esperado",
    [
        (5, 5, 10),           
        (5, 7, 40),        
    ]
)
def test_sumar_varios(a, b, esperado):
    """Test parametrizado que prueba la funcion de sumar"""
    assert sumar(a, b) == esperado

@pytest.mark.parametrize(
    "a,b,esperado", 
    [
        (10, 5, 5),        
        (-5, -4, -10),        
    ]
)
def test_restar_varios(a, b, esperado):
    """Test parametrizado que prueba la función restar con diversos valores."""
    assert restar(a, b) == esperado

@pytest.mark.exception
def test_dividir_por_cero():
    with pytest.raises(ValueError):
        dividir(1, 0)

def test_dividir():
    assert dividir(1, 0) == 1

@pytest.mark.parametrize(
    "a, b, esperado",
    [
        (5, 5, 10),           
        (5, 7, 40),        
    ]
)
def test_sumar_varios(a, b, esperado):
    """Test parametrizado que prueba la funcion de sumar"""
    assert sumar(a, b) == esperado

# ----- TESTS CON ETIQUETAS (MARKS) -----
@pytest.mark.smoke
@pytest.mark.parametrize(
    "a, b, esperado",
    [
        (1, 2, 3),
        (-5, 10, 5),
        (0, 0, 0)
    ]
)
def test_suma(a, b, esperado):
    assert a + b == esperado
    assert a + b == esperado
