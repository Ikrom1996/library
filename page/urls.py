from django.urls import path
from page import views


urlpatterns = [

    #----Class Based Views----
    path('book_create/', views.BookCreateView.as_view(), name='book_create'),
    path('book_list/', views.BookListView.as_view(), name='book_list'),
    path('book_detail/<int:pk>/',views.BookDetailView.as_view(), name='book_detail'),
    path('book_update/<int:pk>/', views.BookUpdateView.as_view(), name='book_update'),
    path('book_delated/<int:pk>',views.BookDeleteView.as_view(), name='book_delated'),
    path('author_list/', views.AuthorListView.as_view(), name='author_list'),
    path('author_create/', views.AuthorCreateView.as_view(), name='author_create'),

    # ---Functions Based Views----
    # path('', views.books, name='books'),
    # path('book_list/', views.book_list, name='book_list'),
    # path('book_detail/<int:id>/',views.book_detail, name='book_detail'),
    # path('book_create/',views.book_create,name='book_create')
    # path('book_update/<int:id>/', views.book_update, name='book_update'),
    # path('book_delated/<int:id>',views.book_delated, name='book_delated'),
    # path('author_create/',views.author_create, name='author_create'),
    # path('author_list/',views.authors_list, name='author_list'),
    # path('file_upload/',views.file_upload, name='file_upload'),

]



