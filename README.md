# Cadastro de usuários

# Tecnologias utilizadas:

*Frontend:*
HTML5, CSS3, JavaScript 

*Backend:*
Python 3 + Flask 

*Banco de Dados:* 
SQLite3

# Requisitos do sistema:
 
*Requisitos Funcionais:*

RF 1 - Cadastrar usuário (cliente):
O sistema deve permitir o registro de novos usuários, utilizando informações como nome, e-mail, CPF, endereço e telefone.

RF 2 - Validar dados obrigatórios:
O sistema deve verificar se todos os campos obrigatórios estão preenchidos antes de concluir o cadastro.

RF 3 - Verificação de CPF:
O sistema deve verificar se o CPF informado é válido e não duplicado.

RF 4 - Evitar Cadastros Duplicados:
O sistema deve impedir o cadastro de usuários com o mesmo e-mail ou nome de usuário já existentes.

RF 5 - Login de Usuário:
O sistema deve permitir que o usuário cadastrado realize login informando seu nome de usuário e senha. O sistema deve autenticar o usuário e liberar o acesso à área correspondente.

RF 6 - Consulta de cadastros:
O sistema deve permitir ao administrador a consulta de todos os usuários cadastrados em formato de tabela.

*Requisitos Não Funcionais:*

RNF 1 - Desempenho:
O sistema deve responder às requisições de cadastro e listagem de usuários em tempo razoável

RNF 2 - Usabilidade:
A interface deve ser simples, intuitiva e responsiva, funcionando corretamente em diferentes tamanhos de tela.

RNF 3 - Linguagens:
O sistema deve ser desenvolvido utilizando Python e JavaScript.

RNF 4 - Portabilidade:
O sistema deve poder ser executado em qualquer ambiente que possua Python instalado, sem necessidade de configurações complexas.

RNF 5 - Legalidade (LGPD):
O sistema deve respeitar a Lei Geral de Proteção de Dados (LGPD), evitando exposição de informações pessoais sem consentimento.

RNF 6 - Segurança:
As senhas devem ser armazenadas em formato de hash e o sistema deve validar dados para evitar injeção de código.

# DIAGRAMA ENTIDADE RELACIONAMENTO:

<img width="528" height="255" alt="Entidade relacionamento" src="https://github.com/user-attachments/assets/1f715115-32e4-47cb-8447-d8af7db5986b" />

# DIAGRAMA DE CASO DE USO:

<img width="726" height="437" alt="Caso de uso" src="https://github.com/user-attachments/assets/dc690e35-393e-4963-b0de-4f3e7594c12b" />

