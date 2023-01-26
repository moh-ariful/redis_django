from django.conf import settings
from posting.views import index, AddPost, UpdatePost, DeletePost, SearchPosting, PostingView
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from posting import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('detail/<int:pk>', PostingView.as_view(), name='detail'),
    path('add/', views.AddPost.as_view(), name='add'),
    path('<int:pk>/update', UpdatePost.as_view(), name='update'),
    path('detail/<int:pk>/delete', DeletePost.as_view(), name='delete'),
    path('search/', SearchPosting.as_view(), name='search'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
