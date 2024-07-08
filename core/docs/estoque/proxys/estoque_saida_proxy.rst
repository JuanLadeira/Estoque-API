Estoque saida Proxy
======================================================================

Estoque saida Proxy

.. mermaid::

 classDiagram
    class Estoque {
      -User funcionario
      -PositiveIntegerField nf
      -CharField movimento
      -BooleanField processado
      -DateField data
      +__str__() String
      +get_movimento_display() String
      +nf_formated() String
      +processar()
      +atualizar_estoque_entrada_ou_saida()
    }
    
.. automodule:: estoque_api.estoque.models.proxys.estoque_saida
   :members:
   :noindex:



