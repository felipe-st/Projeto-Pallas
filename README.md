# Projeto-Pallas
Projeto básico do backend de uma aplicação de lista de compras em python (com FastApi)
<hr>

## Tecnologias utlizadas:
* Python (FastApi, SQLAlchemy);
* MySQL
<hr>

## Como utilizar:
1. Criar o ambiente e instalar as dependências do projeto, que encontram-se em requirements.txt;
2. No arquivo core.configs, preencha <i>DB_URL</i> com os dados do seu banco de dados, seguindo o exemplo e de acordo com a documentação do SQLAlchemy: str = "mysql+asyncmy://root:senha1234@localhost:3300/projeto_pallas";
3. Ainda no arquivo core.configs preencha <i>JWT_SECRET</i> com um token que servirá de segredo para as senhas geradas na aplicação. Você pode utilizar a biblioteca "secrets" do próprio python assim:
    ~~~ 
    no terminal: python 
    import secrets
    token: str = secrets.token_urlsafe(32)
    token
    ~~~
    O token gerado dever ser algo parecido com isso: 'JlcfqOq6_PP7j1L5DyUMqxAfB5ZQZ6_YWKIFYRvPdxA';
4. Execute o arquivo criar_tabelas.py. Se tudo correr bem, você terá criado duas tabelas no seu banco de dados: lista e usuarios;
5. Execute o server.py;
6. Com o servidor sendo executado você já pode executar as operações básicas de crud. Acesse localhost:8000/docs para obter a documentação básica da API, com Swagger. É possível criar usuários, realizar login, cadastrar, editar e apagar produtos da lista de compras, bem como exibir os produtos de um determinado usuário;
7. Fiquem à vontade para aperfeiçoar a aplicação, bem como utiliza-la como base para criação de um front-end.
