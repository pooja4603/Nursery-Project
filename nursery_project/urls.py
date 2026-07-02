from django.contrib import admin
from django.urls import path
from nursery import views
from nursery.views import FertilizerView, FertilizerDetailView
from nursery.views import (
    add_plant,
    plant_list,
    # dashboard,
    edit_plant,
    delete_plant,

    add_pot,
    pot_list,
    edit_pot,
    delete_pot,
)

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Nursery API",
      default_version='v1',
      description="Nursery Management System API",
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),

    # 🌿 Home page
    # path('', plant_list, name='plant_list'),
    path('', views.home),

    # 🌿 Add plant
    path('add-plant/', add_plant, name='add_plant'),

    # 🌿 Plant list (optional duplicate safe)
    path('plants/', plant_list, name='plant_list'),

    # ✏️ Edit plant (MISSING FIX)
    path('edit/<int:id>/', edit_plant, name='edit_plant'),

    # ❌ Delete plant (MISSING FIX)
    path('delete/<int:id>/', delete_plant, name='delete_plant'),

    path('api/plants/', views.get_plants),
    path('api/addplant/', views.add_plant_api),
    path('api/updateplant/<int:id>/', views.update_plant_api),
    path('api/deleteplant/<int:id>/', views.delete_plant_api),

    path('api/pots/', views.get_pots),
    path('api/addpot/', views.add_pot_api),
    path('api/updatepot/<int:id>/', views.update_pot_api),
    path('api/deletepot/<int:id>/', views.delete_pot_api),

    path('api/customers/', views.get_customers),
    path('api/addcustomer/', views.add_customer_api),
    path('api/updatecustomer/<int:id>/', views.update_customer_api),
    path('api/deletecustomer/<int:id>/', views.delete_customer_api),

    path('api/orders/', views.get_orders),
    path('api/addorder/', views.add_order_api),
    path('api/updateorder/<int:id>/', views.update_order_api),
    path('api/deleteorder/<int:id>/', views.delete_order_api),

    path('api/orderitems/', views.get_order_items),
    path('api/addorderitem/', views.add_order_item_api),
    path('api/updateorderitem/<int:id>/', views.update_order_item_api),
    path('api/deleteorderitem/<int:id>/', views.delete_order_item_api),

    path('api/fertilizers/', FertilizerView.as_view()),
    path('api/fertilizers/<int:id>/', FertilizerDetailView.as_view()),

    path(
    'swagger/',
    schema_view.with_ui('swagger', cache_timeout=0),
    name='schema-swagger-ui'
),
path(
    'redoc/',
    schema_view.with_ui('redoc', cache_timeout=0),
    name='schema-redoc'
),
    
]