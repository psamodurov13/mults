from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

from .models import Movies, Tags
from .forms import MoviesForm, ContactForm
from django.core.mail import send_mail
from django.contrib import messages


class HomeMovies(ListView):
    model = Movies
    template_name = 'movies/home_movies_list.html'
    context_object_name = 'movies'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Мультфильмы'
        return context

    def get_queryset(self):
        return Movies.objects.filter(is_published=True)


class MoviesList(ListView):
    model = Movies
    template_name = 'movies/home_movies_list.html'
    context_object_name = 'movies'
    allow_empty = False
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Tags.objects.get(pk=self.kwargs['tag_id'])
        return context

    def get_queryset(self):
        return Movies.objects.filter(tags=self.kwargs['tag_id'])


class ViewMovie(DetailView):
    model = Movies
    context_object_name = 'movie_item'
    # template_name = 'movies/movies_detail.html'
    # pk_url_kwarg = 'movie_id'


class CreateMovie(LoginRequiredMixin, CreateView):
    form_class = MoviesForm
    template_name = 'movies/add_movie.html'
    login_url = '/admin/'
    # raise_exception = True
    # success_url = reverse_lazy('home')


def get_tag(request, tag_id):
    movies = Movies.objects.filter(tags=tag_id)
    tag = Tags.objects.get(pk=tag_id)
    context = {
        'movies': movies,
        'title': tag
    }
    return render(request, 'movies/tags.html', context)


# def view_movie(request, movie_id):
#     # movie_item = Movies.objects.get(pk=movie_id)
#     movie_item = get_object_or_404(Movies, pk=movie_id)
#     context = {
#         'movie_item': movie_item
#     }
#     return render(request, 'movies/view_movie.html', context)


# def add_movie(request):
#     if request.method == 'POST':
#         form = MoviesForm(request.POST)
#         if form.is_valid():
#             # tags_data = form.cleaned_data['tags']
#             # form.cleaned_data.pop('tags')
#             # new_movie = Movies.objects.create(**form.cleaned_data)
#             # new_movie.tags.set(tags_data)
#             new_movie = form.save()
#             return redirect(new_movie)
#     else:
#         form = MoviesForm()
#     return render(request, 'movies/add_movie.html', {'form': form})

