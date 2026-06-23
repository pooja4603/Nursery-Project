from django.contrib import admin
from django.urls import path
from nursery import views
from nursery.views import (
    add_plant,
    plant_list,
    # dashboard,
    edit_plant,
    delete_plant
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

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]