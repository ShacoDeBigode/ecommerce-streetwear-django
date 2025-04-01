from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome do Produto')
    descricao = models.TextField(verbose_name='Descrição do Produto')
    preco = models.FloatField(verbose_name='Preço do Produto')
    estoque = models.IntegerField(default=0, verbose_name='Estoque')
    categoria = models.CharField(max_length=100, verbose_name='Categoria')
    marca = models.CharField(max_length=100, verbose_name='Marca')
    tamanhos = models.CharField(max_length=255, verbose_name='Tamanhos Disponíveis')  # Ex: "P, M, G" ou JSON
    cores = models.CharField(max_length=255, verbose_name='Cores Disponíveis')  # Ex: "Preto, Branco, Vermelho" ou JSON
    imagens = models.TextField(verbose_name='URLs das Imagens')  # Pode ser JSON com URLs
    data_cadastro = models.DateTimeField(auto_now_add=True, verbose_name='Data de Cadastro')


    def clean(self):
        super().clean()
        if self.preco is not None and self.preco <= 0:
            raise ValidationError({'preco': 'O preço deve ser um valor positivo.'})

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'





class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Cliente')
    data_pedido = models.DateTimeField(auto_now_add=True, verbose_name='Data de Pedido')
    status = models.CharField(max_length=20, choices=[
        ('pendente', 'Pendente'),
        ('processando', 'Processando'),
        ('enviado', 'Enviado'),
        ('entregue', 'Entregue'),
        ('cancelado', 'Cancelado'),
    ],
        default='pendente',
        verbose_name='Status do Pedido')
    endereco_entrega = models.TextField(verbose_name='Endereço Entrega')
    metodo_pagamento = models.CharField(max_length= 100, verbose_name='Método Pagamento')
    valor_total = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor Total')

    def __str__(self):
        return f"pedido {self.id} - {self.usuario} - {self.data_pedido}"


    class meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'



class Item_pedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, verbose_name='Pedido', related_name='itens')
    produto = models.ForeignKey('Produto', on_delete=models.CASCADE, verbose_name='Produto')
    quantidade = models.IntegerField(default= 1, verbose_name='Quantidade')
    preco_unitario = models.DecimalField(max_digits=10, decimal_places= 2, verbose_name= 'Preço Unitário')

    def __str__(self):
        return f"pedido {self.quantidade} x {self.produto.nome} no pedido {self.pedido_id}"

    class Meta:
        verbose_name = 'Item Pedido'
        verbose_name_plural = 'Itens do Pedido'