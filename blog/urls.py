from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('ml/', views.PostList_ML.as_view(), name='ML'),
    path('contact/',views.contact, name='Contact'),
    path('about/',views.about, name='About'),
    path('cloud/', views.PostList_Cloud.as_view(), name='Cloud'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT ) 