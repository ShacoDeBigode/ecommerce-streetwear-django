from django.shortcuts import render
from rest_framework import generics
from .models import Produto, Pedido, Item_pedido
from .serializers import ProdutoSerializer
from .serializers import ProdutoSerializer, PedidoSerializer, ItemPedidoSerializer



class ProdutoList(generics.ListAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class ProdutoDetail(generics.RetrieveAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


class PedidoList(generics.ListAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer


class PedidoDetail(generics.RetrieveAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class ItemPedidoList(generics.ListAPIView):
    queryset = Item_pedido.objects.all()
    serializer_class = ItemPedidoSerializer

class ItemPedidoDetail(generics.RetrieveAPIView):
    queryset = Item_pedido.objects.all()
    serializer_class = ItemPedidoSerializer