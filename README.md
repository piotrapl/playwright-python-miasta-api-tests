# Testy API serwisu z danymi o polskich jednostkach samorządu terytorialnego
  https://local-gov-units.polandapi.com

![CI](https://github.com/piotrapl/playwright-python-miasta-api-tests/actions/workflows/ci.yml/badge.svg)

*English abstract:*  
_A minimal API test automation project using **Playwright (Python)** and **pytest**.  
Demonstrates positive and negative REST API testing, data-driven tests, fixtures, and HTML reporting.  
Designed as a portfolio-quality example for QA / Automation Engineer roles._

---

Projekt demonstracyjny automatyzacji testów **REST API**

Repozytorium pokazuje praktyczne użycie:
- **Playwright (Python)** do testów API
- **pytest** jako framework testowy
- testów **pozytywnych i negatywnych**
- testów **data-driven**
- **fixture’ów**
- generowania **raportów HTML**

Testowany jest publiczny endpoint API polskich jednostek samorządu terytorialnego.

---

## Zakres projektu

- Testy **REST API** (GET)
- Jeden endpoint:
/api/v1/municipalities/name/{name}


## Scenariusze:
1. poprawna nazwa (pozytywne)
2. nieistniejąca nazwa (negatywne: 404, NOT_FOUND)
3. pusty parametr zamiast nazwy (scenariusz negatywny: 400, BAD_REQUEST)
Walidacja:
- kodów HTTP
- pól biznesowych (`success`)
- struktury błędów: 
    istnienia i treści `error.code`, 
    istnienia (ale nie treści) `error.message`
- Raportowanie wyników w **HTML**

---

## Technologie (tech stack)

- Python **3.9+**
- Playwright (APIRequestContext)
- pytest
- pytest-html

---

## Wymagania (test evironment reqiurements)

- Python **3.9 lub nowszy**
- pip
- Pytest
- OS: Windows / macOS / Linux

---

## Instalacja (installing the project locally)

#### Klonowanie repozytorium:
 ```bash
 git clone <adres-repozytorium>
 cd playwright-python-miasta-api-tests
 ```

#### Przygotowanie projektu

```bash
pip install -r requirements.txt

python -m playwright install
```
#### Uruchomienie testów (bez raportu):
```bash
pytest
```
#### Uruchomienie testów z generowaniem raportu HTML:
```bash
pytest --html=reports/report.html --self-contained-html
```
Po zakończeniu testów raport HTML zostanie wygenerowany w katalogu:

reports/
### Struktura projektu
```bash
api-playwright-polish-gov/
│
├── tests/
│   ├── test_municipalities_by_name.py
│   └── test_data.py
│
├── reports/
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```
### Możliwe rozszerzenia (possible extentions)
- Walidacja schematu odpowiedzi z usługi (JSON Schema)

- Parametryzacja środowisk, jeśli jest ich więcej (dev / test / prod)

- Rozszerzenie testów o kolejne endpointy

- Integracja z GitHub Actions (CI)

- Raportowanie Allure

- Testy wydajnościowe API

- Obsługa timeoutów i retry

### Dlaczego Pytest a nie unittest ? (Why Pytest, not unittest ?)

- Mniej powtarzalnego kodu (tzw. boilerplate’u)
- Czytelniejsze asercje – `assert` z automatycznym, bogatym opisem błędów
- Parametryzacja testów wbudowana we framework (`@pytest.mark.parametrize`)
- System fixture do współdzielenia danych i setupu testów
- Duży wybór pluginów, np. do raportów
