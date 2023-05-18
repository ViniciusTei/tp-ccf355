# Trabalho Prático/PARTE 1 – Sistemas Distribuídos

> **Professora:** Thais Regina de M. B. Silva \
> **Entrega:** 11/04/2023

O trabalho prático da disciplina de Sistemas Distribuídos será desenvolvido em 5 partes e ao
longo de todo o semestre. O objetivo é que os alunos tenham a oportunidade de passar pelas
etapas de especificação, modelagem e implementação de um sistema, colocando em prática
boa parte do conteúdo teórico discutido. \


O sistema distribuído a ser considerado neste trabalho será uma rede social. Em linhas
gerais, os usuários deste sistema poderão construir relacionamentos (amigos, grupos,
comunidades, seguidores,...) e compartilhar algum tipo de dado (texto, fotos/imagens,
vídeos, arquivos,...) por meio de um processo servidor. De maneira geral, cada usuário com
cadastro/perfil já criado poderá: (1) inserir dados vinculados ao seu perfil; (2) visualizar os
dados do perfil de outros usuários; (3) criar ou participar de algum tipo de relacionamento
com demais usuários; (4) interagir de alguma forma com os dados de outros usuários. Veja
que, propositalmente, a descrição das características do sistema foi deixada em alto nível, de
maneira que cada grupo fará a especificação dos detalhes de projeto e implementação de seu
sistema. \

Nesta primeira parte, cada dupla deverá apresentar os requisitos funcionais e o diagrama de
casos de uso (atores e casos de uso) do sistema distribuído que planeja implementar,
utilizando os mesmos de forma a deixar claro os detalhes de funcionamento do sistema.
Através desta especificação, deve ficar evidente a forma como o processo servidor fará
gestão dos usuários/perfis, bem como de cada uma das 4 tarefas obrigatórias enunciadas
acima. Para cada tarefa, deve ficar claro tudo o que o usuário encontrará como
funcionalidades disponíveis. Não é necessário se apegar a algum processo de
desenvolvimento de software específico, desde que os elementos solicitados fiquem claros
no documento produzido. Os requisitos precisam ser enumerados, os casos de uso
detalhados e um diagrama de casos de uso apresentado. \


Cada grupo definirá o nome que o seu sistema terá, bem como qual será o contexto de sua
rede social (com bom senso, por favor!), isto é, a que nicho de pessoas ela atende (alunos,
jogadores, crianças, músicos, etc...), qual a sua temática (animais, música, culinária, etc...),
que tipo de dados manipula (letras de músicas, apostilas de estudo, fotos de animais de
estimação, etc…), que tipo de relacionamentos constrói (seguidores, comunidades, amigos,
etc...). Embora o sistema precise ter uma interface gráfica funcional, a mesma não será
avaliada na distribuição de notas. Dessa maneira, o foco deverá estar no desenvolvimento
dos serviços e não na visualização dos mesmos.

# Trabalho 2

Neste segunda parte do trabalho, os alunos deverão fazer a modelagem do sistema
distribuído especificado na parte 1.
Ao pensarem sobre os modelos fundamentais, tentem criar as respostas pensando no negócio do sistema, bem como nos modelos físico e de arquitetura selecionados. Utilizem a parte 1 do trabalho para guiá-los. Cada grupo deverá construir um documento que explique ou responda a todos os pontos colocados a seguir, de maneira concisa porém completa. Será avaliado, além do conteúdo, a forma do documento, o qual deverá ser bem escrito, estruturado e ilustrado, se for o caso.

- Considerando os 3 tipos de modelos físicos apresentados em sala de aula, indique aquele mais alinhado com o SD proposto. Justifique.
- Com relação ao modelo de arquitetura, apresente/responda:
  - Qual é o paradigma de comunicação pretendido para ser utilizado entre as entidades arquitetônicas?
  - Qual dos modelos de arquitetura básicos será usado?
  - Quais são as funções e responsabilidades atribuídas à cada uma das entidades do
modelo? Responda à essa pergunta utilizando os casos de uso levantados na parte 1 do trabalho.
  - Há potencial para que o SD seja estruturado em camadas físicas? E em camadas
lógicas? Em caso afirmativo para cada uma das perguntas, indique como isso
poderia ser feito.
- Com relação aos modelos fundamentais (interação, falhas e segurança),
apresente/responda:
  - Para o modelo de interação, identifique: (a) no seu SD, qual a importância da
latência, taxa de transmissão de dados e jitter na interação entre as entidades?; (b)
o SD utilizará modelo síncrono ou assíncrono? Justifique.
  - Para o modelo de falhas, considerando uma das 3 classes de falhas estudadas em
sala de aula ((a) falhas por omissão, (b) falhas arbitrárias e (c) falhas de
temporização), descreva uma possível falha que poderia atrapalhar o sistema e
aponte como a mesma poderia ser detectada e tratada.
  - Para o modelo de segurança, explique se o seu SD necessita de um ou mais
mecanismos para realizar (a) proteção aos processos e (b) proteção ao canal de
comunicação.