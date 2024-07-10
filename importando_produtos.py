import csv
from pathlib import Path

from projeto.produto.models import Produto


def csv_to_list(filename: str) -> list:
    """
    Lê um csv e retorna um OrderedDict.
    Créditos para Rafael Henrique
    https://bit.ly/2FLDHsH
    """
    with Path.open(filename) as csv_file:
        reader = csv.DictReader(csv_file, delimiter=",")
        return list(reader)


def save_data(data):
    """
    Salva os dados no banco.
    """
    aux = []
    for item in data:
        produto = item.get("produto")
        ncm = str(item.get("ncm"))
        importado = item.get("importado") == "True"
        preco = item.get("preco")
        estoque = item.get("estoque")
        estoque_minimo = item.get("estoque_minimo")
        obj = Produto(
            produto=produto,
            ncm=ncm,
            importado=importado,
            preco=preco,
            estoque=estoque,
            estoque_minimo=estoque_minimo,
        )
        aux.append(obj)
    Produto.objects.bulk_create(aux)


data = csv_to_list("fix/produtos.csv")
save_data(data)
