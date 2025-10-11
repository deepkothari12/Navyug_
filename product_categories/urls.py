from django.contrib import admin
from django.urls import path , include
from . import views


urlpatterns = [
    # path('', view=views.product_categories_ , name="product_categoris"),
    path('<slug:category_slug>/' , view=views.only_specify_categories , name="specific_categories"),
    path('<slug:category_slug>/<slug:product_slug>/' , view=views.product_details , name="product_details")

]
