# Descrição

Essa api tem o objetivo de buscar por medicamentos a partir do arquivo api/MedicationGuides.csv (fornecido a pelo site https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm?event=medguide.page).
Inicialmente foi necessário realizar sanitização do arquivo, retirando caracteres especiais e espaços em branco no cabeçalho para o funcionamento correto do código.


## Execução

Para executar o projeto pode ser utilizado o docker ou executando direto.

**Docker**

1. Clone o projeto

2. Execute o comando 

> docker build -t api-bluestorm .

3. Execute a imagem com 
> docker run -d --name mycontainer -p 80:80 api-bluestorm
4. A imagem será executada e rodará na porta 80
ps: o nome do container e porta pode ser alterado

**Execução local**
1. Execute pip install requeriments.txt
2. Execute o comando
> uvicorn api.main:api --reloado
3. O projeto sera executado na porta 8000

ps: caso opte pela execução local é aconcelhável criar um abiente virtual para a instalação dos requeriments

##  Documentação 
A documentação do projeto é gerada pelo swagger e pode ser encontrada em localhost:8000/docs

## Utilização
A api faz uma busca por todos os medicamentos que utilizam determinado ingrediente e retorna uma lista de objetos que correspondem a busca.
Esse ingrediente pode ser passado de forma inteira ou apenas parte dele atraves do link. 
O end point para a utilização é
>localhost:8000/api/{ingrediente}
O retorno é um objeto com status e o retorno da aplicação
