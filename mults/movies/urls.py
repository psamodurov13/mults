from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    # path('', index, name='home'),
    path('', HomeMovies.as_view(), name='home'),
    # path('', cache_page(60)(HomeMovies.as_view()), name='home'),
    # path('tags/<int:tag_id>/', get_tag, name='tag'),
    path('tags/<int:tag_id>/', MoviesList.as_view(extra_context={'title': 'тайтл'}), name='tag'),
    # path('movies/<int:movie_id>/', view_movie, name='view_movie'),
    path('movies/<int:pk>/', ViewMovie.as_view(), name='view_movie'),
    # path('movies/add-movie/', add_movie, name='add_movie'),
    path('movies/add-movie/', CreateMovie.as_view(), name='add_movie'),
]

if settings.DEBUG:
    # urlpatterns = [
    #     path('__debug__/', include('debug_toolbar.urls')),
    # ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)