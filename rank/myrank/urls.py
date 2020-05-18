from django.conf.urls import url
from myrank import views
urlpatterns = [
    url(r'^get_or_update_rank/', views.RankSolver.as_view(),name='rank'),
]
