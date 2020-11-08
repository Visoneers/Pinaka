from django.urls import path
from . import views

# from django.conf.urls.static import static
# from django.conf import settings


urlpatterns = [
    path('', views.store, name = "store"),
    path('cart/', views.cart, name = "cart"),
    path('update_item/',views.updateItem,name='update_item'),
    path('process_order/',views.processOrder,name='process_order'),
    path('checkout/', views.checkout, name = "checkout")
]

#urlpatterns+= static(settings.MEDIA_URL , document_roots=settings.MEDIA_ROOT) #chk
