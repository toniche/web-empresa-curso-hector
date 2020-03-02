from django.urls import path
from . import views

urlpatterns = [
    path('<int:page_id>/', views.page, name='page'),
    #<slug:page_slup>
]

