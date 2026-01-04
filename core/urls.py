from django.contrib import admin
from django.urls import path
from notas.views import NotaList, NotaCreate, NotaUpdate, NotaDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', NotaList.as_view(), name='nota_list'),
    path('crear/', NotaCreate.as_view(), name='nota_create'),
    path('editar/<int:pk>/', NotaUpdate.as_view(), name='nota_update'),
    path('borrar/<int:pk>/', NotaDelete.as_view(), name='nota_delete'),
]