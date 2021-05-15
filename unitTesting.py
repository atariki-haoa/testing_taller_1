import unittest
from model.usuarios import Usuario 

class TestValidations(unittest.TestCase):

    def emailValidation(self):
        self.email = 'correosincorrectoformato'
        self.assertEqual(Usuario.validarCorreo(self), False)
    
    def rutValidation(self):
        self.rut = '12-9'
        self.assertEqual(Usuario.validarRut(self), False)
        self.rut = '12-39'
        self.assertEqual(Usuario.validarRut(self), False)
        self.rut = '129'
        self.assertEqual(Usuario.validarRut(self), False)
        self.rut = '1-9'
        self.assertEqual(Usuario.validarRut(self), True)


if __name__ == '__main__':
    unittest.main(verbosity=2)
