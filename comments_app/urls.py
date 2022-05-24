from django.urls import path


from . import views

urlpatterns = [
	path('', views.TimeLineApi.as_view(), name='index'),
	path('timeline', views.TimeLineApi.as_view(), name='timeline'),
	path('login', views.Login.as_view(), name='login'),
	path('create-post', views.PostApi.as_view(), name='posts'),
	path('add-comment', views.CommentsApi.as_view(), name='comments'),
]