from __future__ import annotations

from django.urls import path
from health_check.views import health_check_view

app_name = 'health_check'

urlpatterns = [path('', health_check_view, name='index')]
