from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView

def news_home(request):
    art = Articles.objects.order_by('-date')
    return render(request, 'news/news_home.html',   {"art": art}, )

class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'

class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'

    form_class = ArticlesForm

class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news'
    template_name = 'news/news-delete.html'

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма некорректна  '

    form = ArticlesForm()

    data = {
        'form': form
    }

    return render(request, 'news/create.html',data)