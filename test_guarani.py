import unittest
from guarani import Guarani

class GuaraniTestCase(unittest.TestCase):

    def setUp(self):
        self.clube = Guarani()

    def test_atualiza_socios(self):
        primeiro_mes = [
            (1, 1),
            (2, 2),
            (3, 3)
        ]

        segundo_mes = [
            (1, 4),
            (4, 5),
            (5, 6)
        ]
        
        result_primeiro_mes = [
            {
                'numero': 1,
                'ativo': True,
                'bilhete': 1
            },
            {
                'numero': 2,
                'ativo': True,
                'bilhete': 2
            },
            {
                'numero': 3,
                'ativo': True,
                'bilhete': 3
            }
        ]

        result_segundo_mes = [
            {
                'numero': 1,
                'ativo': True,
                'bilhete': 4
            },
            {
                'numero': 2,
                'ativo': False,
                'bilhete': 2
            },
            {
                'numero': 3,
                'ativo': False,
                'bilhete': 3
            },
            {
                'numero': 4,
                'ativo': True,
                'bilhete': 5
            },
            {
                'numero': 5,
                'ativo': True,
                'bilhete': 6
            }
        ]
        
        self.clube.atualiza_socios(primeiro_mes)
        clube_primeiro_mes = str(self.clube)
        self.assertEqual(clube_primeiro_mes, str(result_primeiro_mes))

        self.clube.atualiza_socios(segundo_mes)
        clube_segundo_mes = str(self.clube)
        self.assertEqual(clube_segundo_mes, str(result_segundo_mes))

if __name__ == '__main__':
    unittest.main()