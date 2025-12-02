## 📚 Repositório de Estudos: Sistema de Gerenciamento de Biblioteca

Este repositório contém um projeto simples desenvolvido em **Python** para fins de **estudo e prática de Programação Orientada a Objetos (POO)**. O objetivo é simular um pequeno sistema de gerenciamento para uma biblioteca, utilizando conceitos como herança, polimorfismo, encapsulamento e classes abstratas.

---

### ✨ Funcionalidades

O sistema implementa as seguintes funcionalidades principais:

* **Gerenciamento de Itens da Biblioteca:**
    * Criação de itens genéricos (`LibraryItem`).
    * Classes específicas para **Livros** (`Book`) e **Revistas** (`Magazine`), que herdam de `LibraryItem`.
    * **Polimorfismo** na aplicação de descontos: cada tipo de item possui sua própria lógica de desconto (`apply_dicount`).
        * Livros: 10% de desconto.
        * Revistas: 5% de desconto.
* **Gerenciamento de Bibliotecas:**
    * A classe `Library` gerencia coleções de itens e mantém um registro de todas as instâncias de biblioteca criadas.
    * **Estado Ativo/Inativo:** Possibilidade de alternar o estado de funcionamento da biblioteca (`toggle_state`).
    * **Avaliações:** Recebimento e cálculo da média de avaliações de clientes (`receive_evaluation`, `evaluate_media`).
    * Listagem de todas as bibliotecas cadastradas com seu status e nota média (`list_Libraries`).
* **Encapsulamento:** Uso de atributos protegidos (`_title`, `_author`, `_price`, etc.) para controlar o acesso e modificação de dados internos.

---

### 📁 Estrutura do Projeto

O projeto está organizado em módulos para melhor separação de responsabilidades:
