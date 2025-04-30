from django.urls import path
from .views import AskDoubtView

urlpatterns = [
    path('ask/', AskDoubtView.as_view(), name='ask-doubt'),

]