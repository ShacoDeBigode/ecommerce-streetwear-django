from django.urls import path
from . import views

urlpatterns = [
    path('produtos/', views.ProdutoList.as_view()),
    path('produtos/<int:pk>/', views.ProdutoDetail.as_view()),
path('pedidos/', views.PedidoList.as_view()),
    path('pedidos/<int:pk>/', views.PedidoDetail.as_view()),
    path('itens-pedido/', views.ItemPedidoList.as_view()),
    path('itens-pedido/<int:pk>/', views.ItemPedidoDetail.as_view()),
]