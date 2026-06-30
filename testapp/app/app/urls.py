"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from baton.autodiscover import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.views import static
from django.contrib.staticfiles.views import serve
from app.views import admin_search
from news.views import news_change_view

# Non-localized urls: the set_language view and API/asset endpoints. These must
# keep stable paths (e.g. admin/search/ is hardcoded in the BATON SEARCH_FIELD
# config) and don't need a language prefix.
urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/search/', admin_search),
    path('baton/', include('baton.urls')),
    path("select2/", include("django_select2.urls")),
    path('tinymce/', include('tinymce.urls')),
    path('editor-js/', include('editor_js.urls')),
]

# Localized urls: admin pages get a language prefix (/en/admin/, /it/admin/) so
# the active language is reflected in the url.
urlpatterns += i18n_patterns(
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    # path('admin/newschange/<int:id>', news_change_view),
    path('admin/', admin.site.urls),
)

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', static.serve,
                {'document_root': settings.MEDIA_ROOT}),
    ]
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', serve),
    ]
