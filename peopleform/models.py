
'''
    Módulo para criação dos modelos das tabelas do banco de dados
    
    
    author: Janison Serra
    email: j.janilson12@gmail.com
'''

from django.db import models


class Person(models.Model):
    '''
        Classe para criação da tabela que terá os dados das pessoas cadasdtradas no banco de dados.

        Parâmetros
        ----------
        
        full_name : string
            Nome completo da pessoa.
        mother_name : string
            Nome da mãe da pessoa.
        cpf : string
            Número de CPF da pessoas.
        adress : string
            Endereço da pessoa.
        phone : string
            Número de telefone da pessoa.
    '''
    # Os campus com blank e null pode ser preenchido com string vazia ou ser nulo.
    # os outros são obrigatórios serem preenchidos.
    full_name = models.CharField(max_length=255, verbose_name='Nome Completo', help_text='Insira o nome completo.') 
    mother_name = models.CharField(max_length=255, verbose_name='Nome da Mãe Completo', help_text='Insira o nome da sua mãe completo.')
    cpf = models.CharField(max_length=11, unique=True, blank=True, null=True,verbose_name='Número de CPF', help_text='Insira somente número CPF.') 
    adress = models.CharField(max_length=512, default='', blank=True, null=True, verbose_name='Endereço', help_text='Insira o endereço seguido de uma referência que auxilie a encontrar sua localidade.')
    phone = models.CharField(max_length=11, default='', blank=True, null=True, verbose_name='Telefone', help_text='Insira número de telefone com o DDD. (Ex.: 91983243576)')

    def __str__(self):
        return self.full_name # Ao ler o objeto como string ele irá mostrar o full_name.
