from django.urls import path, include

urlpatterns = [
    path('category/', include('category.urls')),
    path('menu/', include('menu.urls')),
    path('allergy/', include('allergy.urls')),
    path('drinl/', include('drink.urls')),
]
