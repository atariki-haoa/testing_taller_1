from unittest.mock import patch
import unittest
from model.usuarios import Usuario 
from model.imc import IMC

class FakeUser(): 
    def create():
        usuario = Usuario()
        usuario.usuario_id = 10
        usuario.email = "asd@asd.com"
        usuario.rut = "1-9"
        usuario.nombre = "Pedro"
        usuario.primer_apellido = "Perez"
        usuario.segundo_apellido = "Pereira"
        usuario.genero = "Masculino"
        usuario.fecha_nacimiento = "01-01-1990"
        usuario.atleta = False        
        usuario.contraseña = "asd1"
        return usuario
class TestValidations(unittest.TestCase):

    def validarCorreo(self):
        self.email = 'correosincorrectoformato'
        self.assertEqual(Usuario.validarCorreo(self), False)

    def validarEstadoNutricional(self):
        imcs = [10, 20, 30, 40]
        for imc in imcs:
            self.imc = imc
            IMC.mostrarEstadoNutricional(self, 1)
    
    def validarCalcularPassword(self):
        self.email = 'asd@1234.cl'
        self.rut = '1234-1'
        self.assertEqual(Usuario.calcularContraseña(self), 'asd1234')
     
    @patch('builtins.input', lambda *args: '10')
    def validarImcVerdadero(self):
        usuario = FakeUser.create()
        self.mostrarEstadoNutricional = IMC.mostrarEstadoNutricional
        self.assertEqual(IMC.calcularIMC(self, usuario), True)
            
    @patch('builtins.input', lambda *args: '-10')
    def validarImcFalso(self):
        usuario = FakeUser.create()
        self.mostrarEstadoNutricional = IMC.mostrarEstadoNutricional
        self.assertEqual(IMC.calcularIMC(self, usuario), False)

    def validarRegistroUsuario(self):
        usuario = FakeUser.create() 
        self.calcularContraseña = Usuario.calcularContraseña
        self.saveData = Usuario.saveData
        self.assertEqual(Usuario.registrarPersona(self, usuario), True)
    
    def allTest(self):
        self.validarCalcularPassword()
        self.validarCorreo()
        self.validarEstadoNutricional()
        self.validarImcVerdadero()
        self.validarImcFalso()
        self.validarRegistroUsuario()

if __name__ == '__main__':
    unittest.main(verbosity=2)
