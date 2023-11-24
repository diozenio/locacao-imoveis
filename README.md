### Demandas do Projeto

As demandas identificadas no estabelecimento para o projeto incluíam a necessidade de criar um sistema de locação de propriedades. O sistema deveria permitir o registro e login de usuários, a publicação e visualização de propriedades, além de funcionalidades relacionadas à locação e devolução de propriedades.

### Objetivos do Projeto

O objetivo principal é oferecer uma plataforma onde usuários pudessem se cadastrar, publicar propriedades para locação, visualizar propriedades disponíveis, e realizar ações como alugar e devolver propriedades.

### Requisitos Desenvolvidos

Os requisitos desenvolvidos para o projeto incluíam a implementação de funções como `register`, `login`, `publish_property`, `view_all_properties`, `view_properties_by_owner`, `view_property_details`, `rent_property_action`, `return_property_action`, e `view_properties_by_renter`. Essas funções atendiam aos objetivos estabelecidos.

### Atendimento pelo Projeto

O projeto atendeu às demandas estabelecidas ao fornecer uma aplicação que permite o registro e login de usuários, a publicação e visualização de propriedades, além de funcionalidades relacionadas à locação e devolução de propriedades.

### Utilização de Estruturas no Código

1. **Funções Aninhadas:** As funções `UnAuthApp` e `AuthApp` são estruturas aninhadas que representam o fluxo de autenticação e ações do usuário no aplicativo.

2. **Listas de Opções (`options`):** As listas de opções são estruturas utilizadas para apresentar escolhas ao usuário nos menus, facilitando a navegação e interação com o sistema.

3. **Dicionários para Propriedades (`property_data`, `prop`):** Dicionários são utilizados para representar propriedades, armazenando informações como nome, descrição, preço e status.

4. **Chamadas Recursivas:** A estrutura de chamadas recursivas está presente no fluxo de autenticação (`UnAuthApp` e `AuthApp`), representando uma forma de controle de fluxo.

Estas estruturas contribuem para a organização e funcionamento do código.

### Requisitos funcionais e não funcionais

#### Requisitos Funcionais

De acordo com a [seção 3.1 do capítulo 3 do livro Engenharia de Software Moderna](https://engsoftmoderna.info/cap3.html#requisitos), os requisitos funcionais são aqueles que descrevem as funcionalidades que o sistema deve oferecer. Os requisitos funcionais identificados para o projeto foram:

- [x] Cadastro de um novo usuário.
- [x] Autenticação de um usuário registrado.
- [x] Listar todas as propriedades registradas.
- [x] Publicação de uma propriedade para locação.
- [x] Visualização das propriedades publicadas pelo usuário.
- [x] Visualização dos detalhes de uma propriedade específica.
- [x] Locação de uma propriedade disponível.
- [x] Devolução de uma propriedade alugada.
- [x] Visualização das propriedades alugadas pelo usuário.

#### Requisitos não Funcionais

De acordo com a [seção 3.1 do capítulo 3 do livro Engenharia de Software Moderna](https://engsoftmoderna.info/cap3.html#introdução), os requisitos não funcionais são aqueles que descrevem as características que o sistema deve apresentar, definindo restrições ao seu funcionamento. Os requisitos não funcionais identificados para o projeto foram:

#### Requisitos Não Funcionais

- [x] Usabilidade: o sistema deve ser fácil de usar, apresentando uma interface intuitiva.
- [x] Confiabilidade: o sistema deve ser confiável, apresentando tolerância a falhas ou a erros.
- [x] Velocidade: o sistema deve ser rápido, apresentando respostas rápidas às ações do usuário.

### História de Usuário

De acordo com a [seção 3.3 do capítulo 3 do livro Engenharia de Software Moderna](https://engsoftmoderna.info/cap3.html#introdução), as histórias de usuário são descrições curtas de funcionalidades que o sistema deve oferecer, escritas na perspectiva do usuário. As histórias de usuário identificadas para o projeto foram:

- [x] Como usuário, eu quero acessar a opção de Criar conta, preencher todas as informações necessárias e realizar o cadastro.
- [x] Como usuário, eu quero acessar a opção de Entrar, fazer login a partir das credenciais registradas e ter acesso ao sistema.
- [x] Como usuário, eu quero acessar a opção de Publicar propriedade, preencher todas as informações necessárias e publicar uma propriedade para locação.
- [x] Como usuário, eu quero acessar a opção de Visualizar todas as propriedades, para ver todas as propriedades registradas no sistema.
- [x] Como usuário, eu quero acessar a opção de Visualizar minhas propriedades, para ver todas as propriedades que publiquei.
- [x] Como usuário, eu quero acessar a opção de Visualizar detalhes de uma propriedade para ver todas as informações sobre uma propriedade específica.
- [x] Como usuário, eu quero acessar a opção de Alugar uma propriedade para fazer a locação de uma propriedade disponível.
- [x] Como usuário, eu quero acessar a opção de Devolver uma propriedade para fazer a devolução de uma propriedade alugada.
- [x] Como usuário, eu quero acessar a opção de Ver propriedades alugadas para ver todas as minhas propriedades alugadas até então.
- [x] Como usuário, eu quero acessar a opção de Sair para encerrar a sessão e sair do sistema.
