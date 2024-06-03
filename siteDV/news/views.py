from django.shortcuts import render, redirect
from .models import Articles
from django.views.generic import DetailView
from .forms import ArticlesForm


def news_home(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})



def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма заполнена неправильно'


    form = ArticlesForm()

    data = {'form': form,
            'error': error

    }

    return render(request, 'news/create.html', data)


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'


