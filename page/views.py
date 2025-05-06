from django.db.models import Q
# from django.shortcuts import render
# from django.shortcuts import redirect
from accounts.utils import login_required,librarian_required
from page.models import Authors, Books
from page.forms import AuthorForm,BooksForm
from django.views import View
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import UpdateView
from django.urls import reverse_lazy


# def books(request):
#     name = request.GET.get('name')
#     return render(request, 'index.html', context={'name': name})



class BookListView(LoginRequiredMixin,ListView):
    model = Books
    template_name = 'book_list.html'
    login_url = 'accounts:login_url'
    context_object_name ='book_list'

    def get_queryset(self):
        q = self.request.GET.get('q','')
        if q:
            return Books.objects.filter(title__icontains= q)

        return Books.objects.all()


#oddiy based view
# @login_required
# def book_list(request):
#     q = request.GET.get('q', '')
#     book = Books.objects.all()
#     if q:
#         book = Books.objects.filter(Q(title__icontains=q) | Q(description__icontains=q))
#     return render(request, 'book_list.html', context={'book_list': book, 'q': q})




class BookDetailView(LoginRequiredMixin,DetailView):
    model = Books
    template_name = 'book_detail.html'
    login_url = 'accounts:login_url'
    context_object_name ='book'




#oddiy based view
# @login_required
# def book_detail(request, id):
#     book = Books.objects.get(id=id)
#     return render(request, 'book_detail.html', context={'book': book})


# @librarian_required
# @login_required
# def get_success_url():
#     return reverse_lazy('book_list')


class BookCreateView(LoginRequiredMixin,CreateView):
    model = Books
    form_class = BooksForm
    template_name = 'book_create.html'
    success_url = reverse_lazy('book_list')
    login_url = 'accounts:login_user'

    def test_func(self):
        return self.request.user.role == 'librarian'



# def book_create(request):
#     if request.method == 'POST':
#         form = BooksForm(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('book_list')
#     else:
#         form = BooksForm()

    # return render(request, 'book_create.html', {'form': form})




class BookUpdateView(LoginRequiredMixin,UpdateView):
    model = Books
    form_class = BooksForm
    login_url = 'account:login_user'
    template_name = 'page/update.html'
    success_url = reverse_lazy('book_list')

    def test_func(self):
        return self.request.user.role == 'librarian'


# @librarian_required
# @login_required
# def book_update(request, id):
#     book = Books.objects.get(id=id)
#     if request.method == 'POST':
#         form = BooksForm(request.POST, instance=book)
#         if form.is_valid():
#             form.save()
#             return redirect('book_list')
#         return render(request, 'page/update.html', {'form': form})
#
#     if request.method == 'GET':
#         form = BooksForm(instance=book)
#         return render(request, 'page/update.html', {'form': form,'book': book})

# @librarian_required
# @login_required
# def book_delated(request, id):
#     Books.objects.get(id=id).delete()
#     return redirect('book_list')

class BookDeleteView(LoginRequiredMixin,DeleteView):
    model = Books
    success_url = reverse_lazy('book_list')
    http_method_names = 'get'
    login_url = 'accounts:login_user'


    def test_func(self):
        return self.request.user.role == 'librarian'





class AuthorListView(LoginRequiredMixin,ListView):
    model = Authors
    template_name = 'authors/authors.html'
    login_url = 'accounts:login_user'


# @login_required
# def authors_list(request):
#     authors = Authors.objects.all()
#     return render(request, 'authors/authors.html', {'author_list': authors})


class AuthorCreateView(LoginRequiredMixin,CreateView):
    model = Authors
    form_class = AuthorForm
    success_url = reverse_lazy('author_list')
    template_name = 'authors/create.html'
    login_url = 'accounts:login_user'


    def test_func(self):
        return self.request.user.role == 'librarian'



# @librarian_required
# @login_required
# def author_create(request):
#     if request.method == 'POST':
#         form = AuthorForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('author_list')
#         return render(request, 'authors/create.html', {'form': form})
#     if request.method == 'GET':
#         form = AuthorForm()
#         return render(request, 'authors/create.html', {'form': form})


#
#
# def file_upload(request):
#     if request.method == 'POST':
#         form = FileUpload1(request.POST, request.FILES)
#         if form.is_valid():  # Corrected: add parentheses here
#             form.save()
#     else:
#         form = FileUpload1()
#     return render(request, 'file_upload.html', {'form': form})