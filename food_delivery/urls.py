"""
URL configuration for food_delivery project.

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
from django.urls import path,include
from myapp.views import IndexViewSet
from django.conf import settings
from django.conf.urls.static import static
from myapp import views
from myapp.views import*


urlpatterns = [
    path('admin/', admin.site.urls),
    path("myapp/", include("myapp.urls")),
    path('', IndexViewSet.as_view(), name='index'),
    path('register/', views.register_user, name='register-user'),
    path('create_order/', views.create_order, name='create-order'),
    path('place-order/', views.place_order, name='place-order'),
    path('make-payment/', views.make_payment, name='make-payment'),
    path('notification-list/', views.notification_list, name='notification-list'),
    path('payment-list/', views.payment_list, name='payment-list'),
    path('orders/', views.orders_view, name='order-list'),
    path("send-email/",views.send_email,name='send_email')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



    # path('login/', views.user_login, name='user-login'),
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('accounts/login/', views.user_login, name='login'),
    # path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('user-list/', views.user_list, name='user-list'),


