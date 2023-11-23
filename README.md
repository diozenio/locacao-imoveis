### Demandas do Projeto

As demandas identificadas no estabelecimento para o projeto incluíam a necessidade de criar um sistema de locação de propriedades. O objetivo principal era oferecer uma plataforma onde usuários pudessem se cadastrar, publicar propriedades para locação, visualizar propriedades disponíveis, e realizar ações como alugar e devolver propriedades.

### Objetivos do Projeto

Os objetivos traçados para o projeto eram:

1. Permitir o registro de novos usuários.
2. Facilitar o login de usuários registrados.
3. Possibilitar a publicação de propriedades para locação.
4. Permitir que os usuários visualizem todas as propriedades disponíveis.
5. Permitir que os proprietários visualizem as propriedades que eles próprios publicaram.
6. Permitir que os usuários vejam detalhes de uma propriedade específica.
7. Permitir que os usuários aluguem propriedades disponíveis.
8. Permitir que os usuários devolvam propriedades alugadas.
9. Possibilitar que os usuários visualizem as propriedades que alugaram.

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
