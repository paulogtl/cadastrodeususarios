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


# RELATÓRIO FINAL – SISTEMA DE CADASTRO DE USUÁRIOS
. Introdução

O nosso relatório apresento o Sistema de Cadastro de Usuários, realizado em duas etapas principais: FASE 1 (Frontend) e FASE 2 (Backend e Banco de Dados).
O projeto visa criar uma aplicação funcional capaz de registrar, armazenar e gerenciar informações de usuários, utilizando tecnologias web modernas e banco de dados relacional.

# Objetivos do Projeto

Criar um sistema de cadastro de usuários funcional e intuitivo.

Separar o código entre frontend, backend e banco de dados.

Utilizar o Flask (framework em Python) e o SQLite para armazenar as informações.

Elaborar a documentação completa do sistema.

# 1. FASE 1 – Documentação

Foi desenvolvido um protótipo funcional da interface do sistema em HTML e CSS, com os seguintes elementos:

Tela inicial com formulário de cadastro de usuário.

Campos de entrada: Nome, E-mail, Senha, Confirmação de Senha, Data de Nascimento e Telefone.

Botão de “Cadastrar”

Layout responsivo e visual limpo.

# 2. FASE 2 –Banco de Dados e Backend

# Pesquisa sobre o Flask 
O Flask é um framework web em Python, ou seja, uma ferramenta que facilita criar sites e sistemas com backend.
Ele é chamado de microframework porque é leve e simples, mas ainda assim muito poderoso.
Com ele, você pode:

Enviar e receber dados entre o site e o servidor;
Conectar seu site a um banco de dados, como o SQLite;
Construir APIs (interfaces de comunicação entre sistemas).

Além dele também ser:
Leve e flexível.
Facilmente integrável com HTML e CSS.
Permite conexão com bancos de dados como SQLite, MySQL e PostgreSQL.
Possui sistema de rotas e templates (Jinja2).

# Pesquisa sobre o SQLite
O SQLite é um banco de dados leve que não precisa de servidor.
Os dados são guardados dentro de um único arquivo no seu computador.
Ele é ótimo para projetos pequenos pois é rápido e fácil de configurar.
Características:

Armazena dados em um único arquivo .db.
Não precisa de servidor dedicado.
Ideal para projetos pequenos e médios.
Compatível com o Flask através da biblioteca sqlite3.

# 3. Conclusão

O desenvolvimento do Sistema de Cadastro de Usuários proporcionou uma experiência completa de criação de um sistema web, desde a fase de planejamento até a integração com o banco de dados.
Durante o processo, foram aplicados conceitos fundamentais da engenharia de software, como levantamento de requisitos, modelagem de dados e separação entre camadas do sistema (frontend, backend e banco de dados).
O projeto atingiu seu objetivo principal de desenvolver um Sistema de Cadastro de Usuários funcional e documentado, utilizando o Flask como backend e o SQLite como banco de dados.
