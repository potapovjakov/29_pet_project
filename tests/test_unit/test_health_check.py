from __future__ import annotations

from django.urls import reverse


def test__health_check_view(client):
    url = reverse('health_check:index')

    response = client.get(url)

    assert response.status_code == 200
    assert response.content.decode() == 'OK'
