from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path ('user_profile/<int:pk>', views.MyAccountView.as_view(), name='user_profile'),
	path('my_collections/<int:pk>', views.MyCollectionsView.as_view(), name='my_collections'),
]


