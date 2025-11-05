from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("",views.SnippetsList.as_view(),name = "snippestslist"),
    path('<int:pk>/', views.SnippetDetails.as_view() ,name = "snippestdetails"),
]
urlpatterns = format_suffix_patterns(urlpatterns)