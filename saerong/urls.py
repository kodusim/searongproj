from django.apps import apps
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from analytics.admin_override import AnalyticsAdminSite
from core.views import robots_txt, ads_txt
from django.contrib.sitemaps.views import sitemap
from core.sitemaps import StaticViewSitemap, PsychoTestSitemap, FaceTestSitemap, CommunityPostSitemap

# 관리자 메뉴에 조회수 분석 메뉴 추가
AnalyticsAdminSite.add_analytics_menu()

sitemaps = {
    'static': StaticViewSitemap,
    'psychotest': PsychoTestSitemap,
    'facetest': FaceTestSitemap,
    'community': CommunityPostSitemap,
}

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("", include("core.urls")),
    path("", include("psychotest.urls")),
    path("community/", include("community.urls")),
    path("facetest/", include("facetest.urls")),
    path('summernote/', include('django_summernote.urls')),
    path('analytics/', include('analytics.urls')),
    path('misc/', include('misc.urls')),
    path('robots.txt', robots_txt),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('ads.txt', ads_txt),    
]

# 개발 환경에서 미디어 파일 서빙 설정
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if apps.is_installed("debug_toolbar"):
     urlpatterns += [
         path("__debug__/", include("debug_toolbar.urls")),
     ]