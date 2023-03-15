from django.urls import path,include
from main.views import *
urlpatterns = [
    path("main/", ImageView.as_view(), name="homepage"),
    path("", register_request, name="register"),
    path("login/", login_request, name="login"),
    path('<pk>/delete/', MediaDriveaDeleteView.as_view(),name="delete"),
    path('<pk>/update/', MediaDriveaUpdateView.as_view(), name="update"),
    path('videos/',recent,name="videos"),
    path('accounts/', include('django.contrib.auth.urls')),
    
    

]

