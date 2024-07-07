
## 1. **Classe Produto:**

   - Atributos:  `importado`, `ncm`, `produto`, `slug`, `preco`, `estoque`, `estoque_minimo`, `data`, e `categoria`.
   
   - `categoria` é uma ForeignKey para a classe `Categoria`.
   - A entidade Produto Funciona como um inventário, armazenando informações sobre o produto e sua quantidade em estoque e quanto deve ser seu estoque mínimo.
   - Cada instância

1. **Relacionamento:**
   - Usamos `-->` para representar a relação de que  [[Diagrama de Classe - Produto]] pertence a [[Diagrama de Classe - Categoria]].


```mermaid
classDiagram
	%% Explicação 
	%% A entidade Produto funciona como um inventário, 
	%% armazenando informações sobre o produto e sua quantidade.
    class Produto {
        +Boolean importado
        +String ncm
        +String produto
        +String slug
        +Decimal preco
        +Integer estoque
        +PositiveInteger estoque_minimo
        +Date data
        +ForeignKey categoria
    }

    class Categoria {
        +Integer id
        +String categoria
        +String slug
    }

    Produto --> Categoria : belongs to




