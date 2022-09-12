from django.urls import path, include
from . import views
from django.contrib import admin
from django.conf.urls.static import static
#from django.conf.urls import url

urlpatterns = [
    path('books/', views.BookListView, name='books'),
    path('book/create/', views.BookCreate, name='book_create'),
    path('book/<int:pk>/update/', views.BookUpdate, name='book_update'),
    path('book/<int:pk>/delete/', views.BookDelete, name='book_delete'),
]
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),

]
