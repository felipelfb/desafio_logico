class Guarani:
    
    def __init__(self, *args, **kwargs):
        self.carteiras = []

    def __str__(self):
        return str(self.carteiras)

    def atualiza_socios(self, lista_socios):
        socio_dict = {}
        for numero, bilhete in lista_socios:
            socio_dict[numero] = bilhete
        for socio in self.carteiras:
            if socio['numero'] in socio_dict:
                socio['ativo'] = True
                socio['bilhete'] = socio_dict[
                    socio['numero']
                    ]
                del socio_dict[socio['numero']]
            else:
                socio['ativo'] = False
        for numero in socio_dict:
            socio = {
                'numero': numero,
                'ativo': True,
                'bilhete': socio_dict[numero]
            }
            self.carteiras.append(socio)
