from django.urls import path
from.import views
urlpatterns=[
    path("",views.post_list,name='post_list'),
    path('post/add/',views.post_create,name='post_add'),
    path('post/<int:id>/',views.post_detail,name='post_detail'),
    path('post/<int:id>/comment/',views.add_comment,name='add_comment'),
    path('post/<int:id>/like/',views.like_post,name='like_post'),
    ]