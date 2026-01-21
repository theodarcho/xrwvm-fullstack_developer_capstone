from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

app_name = 'djangoapp'

urlpatterns = [
    # Authentication paths
    path('login', views.login_user, name='login'),
    path('logout', views.logout_request, name='logout'),

    # Cars
    path('get_cars', views.get_cars, name='get_cars'),

    # Dealers
    path('get_dealers/', views.get_dealerships, name='get_dealers'),
    path(
        'get_dealers/<str:state>',
        views.get_dealerships,
        name='get_dealers_by_state',
    ),
    path(
        'dealer/<int:dealer_id>',
        views.get_dealer_details,
        name='dealer_details',
    ),

    # Reviews
    path(
        'reviews/dealer/<int:dealer_id>',
        views.get_dealer_reviews,
        name='dealer_reviews',
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
