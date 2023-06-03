from django.apps import path
from app.views import *
app_name='app'
urlpatterns=[
    path('bhargavi/',bhargavi,name='bhargavi')
]
