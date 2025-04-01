from django.contrib import admin
from .models import Produto, Item_pedido, Pedido

admin.site.register(Produto)
admin.site.register(Pedido)
admin.site.register(Item_pedido)
