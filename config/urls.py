"""config URL Configuration

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
from django.contrib import admin
from django.urls import path, include

# 다음은 server에서 설정하는것이지만 local에서 볼수있게 mapping 한다.
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # 127.0.0.1:8000/aasdfasldfkj 도 아래 url로 들어가게 된다.
    path('', include('photo.urls')),
    # login-out을 위한 urls
    path('accounts/', include('accounts.urls')),
]



# debug 모드일때 - static 기능을 사용한다.
# 1. 미디어 파일 서버를 별도로 두고 사용한데 (aws s3)
# 2. 웹서버에서 별도로 서빙 설정을 한다. (local server, apache)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)