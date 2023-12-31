from user.views import CreateUserView, CreateTokenView

from django.urls import path

app_name = 'user'

urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create'),
    path('token/', CreateTokenView.as_view(), name='token')
]
