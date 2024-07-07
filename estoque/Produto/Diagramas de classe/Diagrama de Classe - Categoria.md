
## 1. **Classe Categoria:**

   - Atributos:  `id`, `categoria`, e `slug`.
   
   - A `Categoria` permite distinguir produtos com base em alguma similaridade, agrupando-os de acordo com características comuns.
   - A `Categoria` é usada para agrupar produtos com características semelhantes, facilitando a organização e a busca de produtos no inventário. Por exemplo, produtos podem ser categorizados por tipo, função, ou qualquer outro atributo comum.

1. **Relacionamento:**
   - Usamos `-->` para representar a relação de que  [[Diagrama de Classe - Produto]] pertence a  [[Diagrama de Classe - Categoria]].


```mermaid
classDiagram
	 class Categoria {
        +Integer id
        +String categoria
        +String slug
    }
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

   

    Produto --> Categoria : belongs to




