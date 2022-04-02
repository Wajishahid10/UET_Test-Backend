"""uet_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path
from test_app import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('api/signup', views.SignUp),
    path('api/login', views.Login),

    path('api/getLoginManagerFromUID<str:uid>', views.getLogin_Manager),
    path('api/getTypeFromEmail/<str:mail>', views.getAccountTypeFromEmail),

    path('api/userinfo/<int:pk>', views.getUser),
    path('api/user', views.user ),

    path('api/admininfo/<int:pk>', views.getAdmin),
    path('api/admin', views.admin ),

    path('api/deptinfo/<int:pk>', views.getDepartment),
    path('api/department', views.department ),

    path('api/testinfo/<int:pk>', views.getTest),
    path('api/test', views.test ),

    path('api/testImageinfo/<int:pk>', views.getTestImages),
    path('api/testImage', views.testImages ),

    path('api/personAssignedinfo/<int:pk>', views.getPerson_Assigned),
    path('api/personAssigned', views.person_Assigned ),

    path('api/orderinfo/<int:pk>', views.getOrder),
    path('api/order', views.order ),

    path('api/resultinfo/<int:pk>', views.getResult),
    path('api/result', views.result ),

    path('api/completedOrderInfo/<int:pk>', views.getCompleted_Order),
    path('api/completedOrder', views.Completed_Order ),

]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)