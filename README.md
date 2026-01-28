# Playwright API Tests – Polskie Jednostki Samorządu Terytorialnego

**English (short abstract):**  
A minimal API test automation project using **Playwright (Python)** and **pytest**.  
Demonstrates positive and negative REST API testing, data-driven tests, fixtures, and HTML reporting.  
Designed as a portfolio-quality example for QA / Automation Engineer roles.

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
- poprawna nazwa (pozytywne)
- nieistniejąca nazwa (404)
- niepoprawna nazwa (404)
- pusty parametr ścieżki (BAD_REQUEST)
- Walidacja:
- kodów HTTP
- pól biznesowych (`success`)
- struktury błędów (`error.code`, `error.message`)
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

#### Instalacja zależności (Installing dependencies)
pip install -r requirements.txt
Instalacja Playwright:

python -m playwright install

#### Uruchomienie testów (bez raportu):

pytest
#### Uruchomienie testów z raportem HTML:

pytest --html=reports/report.html --self-contained-html
Po zakończeniu testów raport HTML zostanie wygenerowany w katalogu:

reports/
### Struktura projektu
text

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

### Możliwe rozszerzenia (possible extentions)
Walidacja schematu odpowiedzi (JSON Schema)

Parametryzacja środowisk (dev / test / prod)

Rozszerzenie testów o kolejne endpointy

Integracja z GitHub Actions (CI)

Raportowanie Allure

Testy wydajnościowe API

Obsługa timeoutów i retry

### Dlaczego Pytest a nie unittest ? (Why Pytest, not unittest ?)

- Mniej boilerplate’u – brak klas testowych i `self`, testy to zwykłe funkcje
- Czytelniejsze asercje – `assert` z automatycznym, bogatym opisem błędów
- Parametryzacja testów wbudowana we framework (`@pytest.mark.parametrize`)
- Potężny system fixture do współdzielenia danych i setupu testów
- Bogaty ekosystem pluginów (raporty, parallel run, coverage)
