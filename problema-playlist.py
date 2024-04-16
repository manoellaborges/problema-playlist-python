class Programa:
    def __init__(self, nome, ano):
        '''função definindo os atributos da classe Programa
        
        Parâmetros:
        - str nome: nome do programa (atributo privado)
        - ano: ano de lançamento do programa
        - duracao - tempo de duracao do programa
        
        '''
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        '''função para poder acessar atributo likes, que é privado'''
        return self._likes

    def dar_like(self):
        '''função para contar a quantidade de likes'''
        self._likes += 1

    @property
    def nome(self):
        '''função para poder acessar atributo nome, que é privado'''
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        '''função que acessa um atributo privado para deixar as primeiras letras de cada nome como maiúscula'''
        self._nome = novo_nome.title()

    def __str__(self):
        '''Função que define representação textual do meu objeto'''
        return f'{self._nome} - {self.ano} - {self._likes} likes'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} min - {self.likes} likes'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self.likes} likes'

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        '''Essa função está repassando um item para a minha lista de programas interno'''
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas
    
    def __len__(self):
        '''Função que retorna o tamanho da lista'''
        return len(self._programas)

filme01 = Filme('vingadores - guerra infinita', 2018, 160)
filme01.dar_like()
filme02 = Filme('Barbie', 2023, 180)
filme02.dar_like()
filme02.dar_like()
filme02.dar_like()
filme02.dar_like()
serie01 = Serie('atlanta', 2018, 2)
serie01.dar_like()
serie01.dar_like()
serie02 = Serie('riverdale', 2016, 5)
serie02.dar_like()
serie02.dar_like()
serie02.dar_like()

filmes_e_series = [filme01, serie01, filme02, serie02]
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

print(f'Tamanho do playlst: {len(playlist_fim_de_semana)}')

print(playlist_fim_de_semana[0])

len(playlist_fim_de_semana)

for programa in playlist_fim_de_semana:
    print(programa)

