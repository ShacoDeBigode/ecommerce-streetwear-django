from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Produto, Pedido, ItemPedido
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
    queryset = ItemPedido.objects.all()
    serializer_class = ItemPedidoSerializer

class ItemPedidoDetail(generics.RetrieveAPIView):
    queryset = ItemPedido.objects.all()
    serializer_class = ItemPedidoSerializer

@api_view(['GET'])
def carrinho_detalhes(request):
    carrinho = request.session.get('carrinho', {})
    produtos_no_carrinho = []
    for produto_id, quantidade in carrinho.items():
        try:
            produto = Produto.objects.get(pk=produto_id)
            serializer = ProdutoSerializer(produto)
            produtos_no_carrinho.append({'produto': serializer.data, 'quantidade': quantidade})
        except Produto.DoesNotExist:
            # Se o produto não existir mais, remove do carrinho
            del carrinho[produto_id]
            request.session['carrinho'] = carrinho
    return Response(produtos_no_carrinho)

@api_view(['POST'])
def carrinho_adicionar(request):
    produto_id = request.data.get('produto_id')
    quantidade = request.data.get('quantidade', 1)

    if not produto_id:
        return Response({'error': 'O ID do produto é obrigatório.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        produto = Produto.objects.get(pk=produto_id)
    except Produto.DoesNotExist:
        return Response({'error': 'Produto não encontrado.'}, status=status.HTTP_404_NOT_FOUND)

    carrinho = request.session.get('carrinho', {})
    carrinho[produto_id] = carrinho.get(produto_id, 0) + int(quantidade)
    request.session['carrinho'] = carrinho
    return Response({'message': f'{quantidade} unidade(s) de {produto.nome} adicionada(s) ao carrinho.'})

@api_view(['PUT'])
def carrinho_atualizar(request):
    produto_id = request.data.get('produto_id')
    quantidade = request.data.get('quantidade')

    if not produto_id or quantidade is None:
        return Response({'error': 'O ID do produto e a quantidade são obrigatórios.'}, status=status.HTTP_400_BAD_REQUEST)

    carrinho = request.session.get('carrinho', {})
    if produto_id in carrinho:
        carrinho[produto_id] = int(quantidade)
        request.session['carrinho'] = carrinho
        return Response({'message': f'Quantidade do produto {produto_id} atualizada para {quantidade}.'})
    else:
        return Response({'error': 'Produto não encontrado no carrinho.'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def carrinho_remover(request):
    produto_id = request.data.get('produto_id')

    if not produto_id:
        return Response({'error': 'O ID do produto é obrigatório.'}, status=status.HTTP_400_BAD_REQUEST)

    carrinho = request.session.get('carrinho', {})
    if produto_id in carrinho:
        del carrinho[produto_id]
        request.session['carrinho'] = carrinho
        return Response({'message': f'Produto {produto_id} removido do carrinho.'})
    else:
        return Response({'error': 'Produto não encontrado no carrinho.'}, status=status.HTTP_404_NOT_FOUND)