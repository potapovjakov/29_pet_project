from __future__ import annotations

from django.http import HttpRequest, HttpResponse


def health_check_view(request: HttpRequest) -> HttpResponse:
    return HttpResponse('OK', status=200)
