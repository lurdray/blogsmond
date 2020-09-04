
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from main.sitemaps import StaticViewSitemap, BlogSitemap
from django.conf import settings
from django.conf.urls.static import static


sitemaps = {
	"main_static": StaticViewSitemap,
	"blog": BlogSitemap,
}

urlpatterns = [
	path('', include("main.urls")),
	path("sitemap.xml", sitemap, {"sitemaps": sitemaps}),
    path('admin/', admin.site.urls),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
