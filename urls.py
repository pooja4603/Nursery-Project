from django.contrib import admin
from django.urls import path
from nursery import views
from nursery.views import (
    add_plant,
    plant_list,
    edit_plant,
    delete_plant
)

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

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

    path('', views.home),

    path('add-plant/', add_plant, name='add_plant'),
    path('plants/', plant_list, name='plant_list'),

    path('edit/<int:id>/', edit_plant, name='edit_plant'),
    path('delete/<int:id>/', delete_plant, name='delete_plant'),

    path('api/plants/', views.get_plants),
    path('api/addplant/', views.add_plant_api),
    path('api/updateplant/<int:id>/', views.update_plant_api),
    path('api/deleteplant/<int:id>/', views.delete_plant_api),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
    
]