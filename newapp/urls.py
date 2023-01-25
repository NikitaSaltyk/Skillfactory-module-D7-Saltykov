from django.urls import path
# Импортируем созданное нами представление
# from .views import PostList, PostDetail, PostSearch, PostCreate, PostUpdate, PostDelete, CategoryListView, subscribe, \
#    NewPostView, IndexView, WeekViews

from .views import *

urlpatterns = [
   path('', PostList.as_view(), name='post_list'),
   path('', NewPostView.as_view()),
   path('', WeekViews.as_view()),
   path('index/', IndexView.as_view()),
   path('<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('search/', PostSearch.as_view(), name='post_search'),
   path('create/', PostCreate.as_view(), name='post_create'),
   path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
   path('categories/<int:pk>/subscribe', subscribe, name='subscribe')

]