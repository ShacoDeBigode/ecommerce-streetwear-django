from rest_framework import serializers
from .models import Produto, Pedido, ItemPedido
from django.contrib.auth.models import User



class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'

class ItemPedidoSerializer(serializers.ModelSerializer):
    produto = ProdutoSerializer(read_only=True)
    class Meta:
        model = ItemPedido
        fields = '__all__'