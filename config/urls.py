from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('bbs/', include('bbs.urls')),
    path('hello/', include('hello.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')), # accounts/以下のルーティングはaccounts.urls.pyに任せる
    path('accounts/', include('django.contrib.auth.urls')),
]
