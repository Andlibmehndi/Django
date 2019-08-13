from django.urls import path

from . import views
from . import apiviews

app_name = 'polls'
urlpatterns = [
    # old without generic view
    # path('', views.index, name='index'),
    # path('<int:question_id>/', views.detail, name='detail'),
    # path('<int:question_id>/results/', views.results, name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),

    #With Generic view
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('questions/', apiviews.questions_view, name='questions_view'),
    path('questions/<int:question_id>/', apiviews.question_detail_view, name='question_detail_view'),
]

