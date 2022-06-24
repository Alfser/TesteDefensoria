'''
    Módulo que receberá os comportamentos que serão adicionados as vizualizações no html.

    author : Janilson Serra
    email : j.janilson12@gmail.com
'''

from django.urls import reverse_lazy
from django.views import generic

from peopleform.models import Person
class PersonList(generic.ListView):
    '''
        Classe que irá auxiliar na listagem dos dados cadastrados na tabela person do banco de dados.

        Obs: A classe ListView por padão irá procurar o html person_list.html na pasta templates.
    '''
    model = Person # Define o modelo que será listado
    queryset = Person.objects.all() # Obtem os dados que serão listados.


class PersonCreate(generic.CreateView):
    '''
        Classe que irá auxiliar no cadastro das pessoas.

        Obs: A classe CreateView por padão irá procurar o html person_form.html na pasta templates.
    '''

    model = Person # Modelo que definirá os dados que serão recebidos no formulário de cadastro.
    fields = '__all__'
    #o atributo success_url receberá a rota a qual ele irá retonar após a operação for concluida.
    success_url = reverse_lazy('peopleform:list') # # reverse_laze pega a url atravez do nameespace e do nome da rota.


class PersonUpdate(generic.UpdateView):
    '''
        Classe que irá auxiliar na adição dos dados das pessoas cadastradas.

        Obs: A classe UpdateView por padão irá procurar também o html person_form.html na pasta templates.
    '''

    model = Person # Modelo que definirá os dados que poderão ser alterados no formulário.
    fields = '__all__'
     #o atributo success_url receberá a rota a qual ele irá retonar após a operação for concluida. 
    success_url = reverse_lazy('peopleform:list') # reverse_laze pega a url atravez do nameespace e do nome da rota.

class PersonDetails(generic.DetailView):
    '''
        Classe que irá auxiliar na visualização dos dados da pessoa cadastrada.

        Obs: A classe DetailView por padão irá procurar também o html person_detail.html na pasta templates.
    '''

    queryset = Person.objects.all() # Receber os dados que serão exibidos na view. 

class PersonDelete(generic.DeleteView):
    '''
        Classe que irá auxiliar na deleção dos dados das pessoas cadastradas.

        Obs: A classe DeleteView por padão irá procurar também o html person_confirm_delete.html na pasta templates.
    '''
    queryset = Person.objects.all() # Receber o object para consultar do dados que será deletado. 
    success_url = reverse_lazy('peopleform:list') # reverse_laze pega a url atravez do nameespace e do nome da rota.
