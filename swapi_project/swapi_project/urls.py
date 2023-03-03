"""swapi_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from swapi_app.views.single_table import SwapiSingleTableView
from swapi_app.views.tables import SwapiTablesView
from swapi_app.views.values_count import ValuesCountTableView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", SwapiTablesView.as_view(), name="tables"),
    path(
        "single_table/<int:id>",
        SwapiSingleTableView.as_view(),
        name="single_table",
    ),
    # path(
    #     "values_count/<int:id>",
    #     ValuesCountTableView.as_view(),
    #     name="values_count",
    # ),
    path(
        "single_table/<int:id>/values_count/",
        ValuesCountTableView.as_view(),
        name="values_count",
    ),
]
