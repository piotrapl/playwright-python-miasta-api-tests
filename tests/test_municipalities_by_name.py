import pytest
from tests.test_data import POSITIVE_CITIES, NEGATIVE_CITIES

# Testy dla endpointu pobierającego jednostki samorządowe po nazwie miasta
# Asercje sprawdzają, czy odpowiedzi API są zgodne z oczekiwaniami dla istniejących i nieistniejących nazw miast.

@pytest.mark.parametrize("city", POSITIVE_CITIES)
def test_get_municipality_by_name_should_return_data(api_request, city):
    response = api_request.get(f"/api/v1/municipalities/name/{city}")

    assert response.status == 200

    body = response.json()
    assert body.get("success") is True
    assert "data" in body
    assert len(body["data"]) > 0


@pytest.mark.parametrize("city", NEGATIVE_CITIES)
def test_get_municipality_by_non_existing_name_should_return_404(api_request, city):
    response = api_request.get(f"/api/v1/municipalities/name/{city}")

    assert response.status == 404

    body = response.json()
    assert body.get("success") is not True

    # API error contract is nested: error.code / error.message
    assert "error" in body
    assert body["error"].get("code") in {"NOT_FOUND", "BAD_REQUEST"}
    assert "message" in body["error"]


def test_get_municipality_with_empty_name_should_return_404_and_bad_request(api_request):
    response = api_request.get("/api/v1/municipalities/name/")

    # As requested
    assert response.status == 404

    body = response.json()
    assert body.get("success") is not True

    assert "error" in body