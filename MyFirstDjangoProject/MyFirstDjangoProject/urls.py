"""
URL configuration for MyFirstDjangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter
from user.views import ProfileViewSet
from user.views import AccountViewSet

from user.viewset import AccViewSet

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'accounts', AccountViewSet)

# account_list = AccViewSet.as_view({'get': 'get_accounts', 'post': 'add_account', })
# account_list2 = AccViewSet.as_view({'get': 'get_account', 'put': 'update_account', 'delete': 'delete_account'})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include(router.urls)),
    path("accounts/", AccViewSet.as_view({"get": "get_accounts"})),
    path("accounts/info/<int:pk>/",
         AccViewSet.as_view({"get": "get_account"})),
    path("accounts/add/", AccViewSet.as_view({"post": "add_account"})),
    path("accounts/update/",
         AccViewSet.as_view({"put": "update_account"})),
    path("accounts/delete/<int:pk>/",
         AccViewSet.as_view({"delete": "delete_account"}))
]
