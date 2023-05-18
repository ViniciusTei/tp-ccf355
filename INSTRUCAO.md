# Instruções

Aqui você vai encontrar instruçõe de como rodar o programa na sua máquina.

**Ambiente virtual**

Para começar, deve rodar o ambiental virtual você pode fazer isso manualmente seguindo a documentação ou rodar o script ```install.ps1```.
Nele são executados os comandos que vão criar o ambiente virtual, instalar as dependências do projeto e iniciar o ambiente para desenvolvimento e testes.

**Executando**

Para executar você precisa iniciar o servidor e o cliente separadamente. Pode fazer isso de forma manual executando os arquivo [server.py](server/server.py), e o arquivo [client.py](client/client.py). Sem esquecer de ativar o ambiente virtual e instalar o arquivo requirements.txt.

Mas para facilitar, podemos apenas utilizar a ferramenta make para executar os processos. Basta usar ```make run_server``` e ```make run_client``` em terminais diferentes.

#### Problemas

[Instalando make no windows](https://stackoverflow.com/questions/32127524/how-to-install-and-use-make-in-windows)
