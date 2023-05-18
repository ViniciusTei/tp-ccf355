# Documentação

Documentação das principais classes usadas no sistemas, responsáveis pela execução das regras de negócio e fazer a comunicação entre cliente e servidor.

# Client

##  Documentação para a classe API

####  Descrição
A classe `API` é uma classe em Python que fornece métodos para fazer requisições HTTP a um servidor utilizando os métodos GET e POST. Internamente, utiliza um socket para estabelecer uma conexão com o servidor e enviar/receber dados.

####  Construtor
#####  `__init__(self, sock=None)`
O método construtor inicializa uma instância da classe `API`.

**Parâmetros:**
- `sock` (opcional): Um objeto socket usado para a conexão. Se não for fornecido, um novo objeto socket será criado.

####  Métodos Privados
#####  `__start_connection(self)`
Estabelece uma conexão com o servidor.

#####  `__end_connection(self)`
Encerra a conexão com o servidor.

#####  `__send(self, msg, headers)`
Envia uma mensagem de requisição para o servidor e recebe a resposta.

**Parâmetros:**
- `msg`: A mensagem a ser enviada para o servidor.
- `headers`: Um dicionário contendo os cabeçalhos da requisição.

**Retorna:**
- Um dicionário representando a resposta do servidor.

####  Métodos Públicos
#####  `GET(self, url)`
Envia uma requisição GET para a URL especificada e retorna a resposta do servidor.

**Parâmetros:**
- `url`: A URL para enviar a requisição GET.

**Retorna:**
- Um dicionário representando a resposta do servidor.

#####  `POST(self, url, dictionary)`
Envia uma requisição POST para a URL especificada com os dados fornecidos e retorna a resposta do servidor.

**Parâmetros:**
- `url`: A URL para enviar a requisição POST.
- `dictionary`: Um dicionário contendo os dados a serem enviados na requisição POST.

**Retorna:**
- Um dicionário representando a resposta do servidor.

<hr />

# Server

## Documentação para a classe Connection

#### Descrição
A classe `Connection` é responsável por lidar com uma conexão estabelecida com um cliente. Ela recebe uma conexão como parâmetro no construtor e fornece métodos para iniciar o tratamento da conexão.

#### Construtor
##### `__init__(self, conn)`
O método construtor inicializa uma instância da classe `Connection` com a conexão fornecida.

**Parâmetros:**
- `conn`: O objeto de conexão.

#### Métodos Públicos
##### `start(self)`
Inicia o tratamento da conexão em uma nova thread.

##### Métodos Privados
##### `__handle_request(self, connection)`
Lida com uma requisição recebida da conexão.

**Parâmetros:**
- `connection`: O objeto de conexão.

**Retorna:**
- Uma tupla contendo o método da requisição, a URL e o payload.

##### `__handle_connection(self, connection)`
Lida com a conexão estabelecida com o cliente, tratando a requisição, executando o roteador e enviando a resposta de volta ao cliente.

**Parâmetros:**
- `connection`: O objeto de conexão.

## Documentação para a classe Router

#### Descrição
A classe `Router` é uma classe que implementa um roteador básico para lidar com requisições HTTP. Ele permite registrar rotas para os métodos GET e POST e associar um callback a cada rota. Quando uma requisição é feita, o roteador verifica a rota correspondente com base no método e URL fornecidos e executa o callback associado.

#### Construtor
##### `__init__(self)`
O método construtor inicializa uma instância da classe `Router`. Ele cria listas vazias para armazenar as rotas GET e POST.

#### Métodos Públicos
##### `get(self, url, callback)`
Registra uma rota GET com a URL e o callback fornecidos.

**Parâmetros:**
- `url`: A URL da rota GET.
- `callback`: A função de callback a ser executada quando a rota for acessada.

##### `post(self, url, callback)`
Registra uma rota POST com a URL e o callback fornecidos.

**Parâmetros:**
- `url`: A URL da rota POST.
- `callback`: A função de callback a ser executada quando a rota for acessada.

##### `run(self, method, url, payload)`
Executa o roteador para lidar com uma requisição.

**Parâmetros:**
- `method`: O método da requisição (GET, POST, etc.).
- `url`: A URL da requisição.
- `payload`: Os dados da requisição (para requisições POST).

**Retorna:**
- O resultado do callback associado à rota correspondente.

