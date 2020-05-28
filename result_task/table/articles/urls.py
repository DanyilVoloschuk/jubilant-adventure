from django.urls import path

from . import views


app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search),
    path('search/cancel/', views.cancel),
    path('search/delete/<int:article_id>/', views.delete_btn),
    path('search/delete/<int:article_id>/cancel/', views.cancel),
    path('search/delete/<int:article_id>/delete_confirm/', views.delete_confirm),
    path('search/delete/<int:article_id>/delete_confirm/cancel/', views.cancel),

    path('search/edit/<int:article_id>/', views.edit_btn),
    path('search/edit/<int:article_id>/edit_confirm/', views.edit_confirm),
    path('search/edit/<int:article_id>/cancel/', views.cancel),

    path('delete/<int:article_id>/', views.delete_btn),
    path('delete/<int:article_id>/delete_confirm/', views.delete_confirm),
    path('delete/<int:article_id>/delete_confirm/cancel/', views.cancel),
    path('delete/<int:article_id>/cancel/', views.cancel),

    path('edit/<int:article_id>/', views.edit_btn),
    path('edit/<int:article_id>/edit_confirm/', views.edit_confirm),
    path('edit/<int:article_id>/cancel/', views.cancel),

    path('add-new-human/', views.add_new_btn, name='add'),
    path('add-new-human/add_new_confirm/', views.add_new_confirm, name='add_confirm'),
    path('add-new-human/cancel/', views.cancel),
]
