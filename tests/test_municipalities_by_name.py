import pytest
from tests.test_data import POSITIVE_CITIES, NEGATIVE_CITIES

# Testy dla endpointu pobierającego jednostki samorządowe po nazwie miasta
# Asercje sprawdzają, czy odpowiedzi API są zgodne z oczekiwaniami dla istniejących i nieistniejących nazw miast.
# @pytest.mark.parametrize("city", POSITIVE_CITIES)
# - odpowiednik pętli for dla testów jednostkowych 
#   uruchamia test dla każdej wartości w POSITIVE_CITIES

@pytest.mark.parametrize("city", POSITIVE_CITIES)
def test_get_municipality_by_name_should_return_data(api_request, city):
    response = api_request.get(f"/api/v1/municipalities/name/{city}")

    assert response.status == 200

    body = response.json()
    assert body.get("success") is True
    assert "data" in body
    assert len(body["data"]) > 0

# Test negatywny dla tego samego endpointu
# Spawdza, czy odpowiedź API jest poprawna dla NIEISTNIEJĄCEJ nazwy miasta

@pytest.mark.parametrize("city", NEGATIVE_CITIES)
def test_get_municipality_by_non_existing_name_should_return_404_not_found(api_request, city):
    response = api_request.get(f"/api/v1/municipalities/name/{city}")

    assert response.status == 404

    body = response.json()
    assert body.get("success") is not True

    # kontrakt błędu API jest zagnieżdżony: error.code / error.message
    assert "error" in body
    # assert body["error"].get("code").equals("NOT_FOUND")
    assert body["error"].get("code") == "NOT_FOUND"
    assert "message" in body["error"]

# Test negatywny dla tego samego endpointu
# Sprawdza, czy odpowiedź API jest poprawna dla PUSTEJ nazwy miasta
# jeden kontrakt błędu API jest zagnieżdżony: error.code / error.message
# bez parametryzacji (@pytest.mark.parametrize...), 
# bo to tylko jeden przypadek testowy (pusta nazwa)

def test_get_municipality_with_empty_name_should_return_400_bad_request(api_request):
    response = api_request.get("/api/v1/municipalities/name/")

    assert response.status == 400

    body = response.json()
    error = body["error"]

    assert body["success"] is False
    assert error["code"] == "BAD_REQUEST"
    assert "message" in error