from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from Book.views import BookView, GenreView, CommentView, LikeView, BookRatingView , FavoriteView
from custom_auth.views import RegisterView, LoginView


schema_view = get_schema_view(
   openapi.Info(
      title="Magazine API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
                  re_path(r'^swagger(?P<format>\.json|\.yaml)$',
                          schema_view.without_ui(cache_timeout=0), name='schema-json'),
                  re_path(r'^swagger/$',
                          schema_view.with_ui('swagger', cache_timeout=0),
                          name='schema-swagger-ui'),
                  re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0),
                          name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('book/', BookView.as_view({'get': 'list'})),
    path('create/', BookView.as_view({'post': 'create'})),
    path('book/<int:pk>/', BookView.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}
    )),
    path('genre/', GenreView.as_view({'get': 'list', 'post': 'create'})),
    path('genre/<int:pk>/', GenreView.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}
    )),
    path('rating/', BookRatingView.as_view({'post': 'create'})),
    path('rating/<int:pk>', BookRatingView.as_view({'get': 'list'})),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('<int:pk>/comment/create/', CommentView.as_view(
        {'post': 'create', 'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})
         ),
    path('<int:pk>/like/', LikeView.as_view()),
    path('<int:pk>/favorite/', FavoriteView.as_view()),
    path('i18n/', include('django.conf.urls.i18n')),
    path('silk/', include('silk.urls', namespace='silk'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


