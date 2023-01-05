from django.urls import path
from .views import SubscriptionView

urlpatterns = [
    path('', SubscriptionView.as_view(), name='subscription'),
    # path('success/', success, name='success')
]