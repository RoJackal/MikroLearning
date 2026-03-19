# MikroLearning - Platformă de Cursuri Online (Proiect de Absolvire)

MikroLearning este o aplicație web complexă dezvoltată în **Django**, destinată gestionării certificărilor MikroTik. Proiectul a fost creat ca lucrare de absolvire pentru cursul de Python, punând accent pe bunele practici de programare, securitate și automatizare prin containerizare.

## 🚀 Caracteristici Principale (Requirements)

Proiectul implementează următoarele funcționalități obligatorii:

* **Arhitectură Django**: Structură modulară cu aplicații dedicate (`courses`, `home`).
* [cite_start]**Containerizare Docker**: Utilizarea **Docker** și **Docker Compose** pentru a asigura un mediu de rulare identic între dezvoltare și producție (include servicii pentru aplicația web și baza de date MariaDB). [cite: 1]
* [cite_start]**Modele de Date**: Implementarea modelelor `Course`, `Enrollment` și `News` cu relații complexe (Foreign Keys). [cite: 6, 7]
* **Interfață Administrativă**: Gestiune completă via Django Admin.
* **Validări Avansate**:
    * [cite_start]Verificarea logică a datelor (ex: data de final a cursului trebuie să fie după data de început). [cite: 11]
    * [cite_start]Prevenirea înscrierilor duplicate la același curs direct din logica formularului (`clean()`). [cite: 11]
* [cite_start]**Sistem de Autentificare**: Înregistrare, login și protecția rutelelor folosind Mixins și decoratori. [cite: 2]
* [cite_start]**Comunicare Automată**: Integrare `send_mail` pentru confirmarea înscrierii la cursuri prin email. [cite: 4]
* [cite_start]**Context Processors**: Afișarea globală a celor mai populare 5 cursuri în interfață. [cite: 5, 10]
* [cite_start]**Static & Media Files**: Integrare Tailwind CSS și gestionarea materialelor de curs (PDF-uri, imagini) folosind **WhiteNoise**. [cite: 2, 5]

## 🛠️ Tehnologii Utilizate

* **Backend**: Python 3.14, Django 5.1
* **Bază de date**: MariaDB 10.11
* **Frontend**: Tailwind CSS
* **Server/Container**: Docker, Docker Compose, Gunicorn, WhiteNoise

## 📦 Instalare și Rulare

### 1. Utilizând Docker (Recomandat)
Asigurați-vă că aveți Docker Desktop instalat. Rulați următoarea comandă în rădăcina proiectului:

```powershell
docker-compose -f docker-compose.prod.yml up --build -d
```

Aplicația va fi accesibilă la adresa http://localhost:8000.

2. Instalare Locală (Dezvoltare)
Dacă doriți să rulați proiectul fără Docker:

Creați un mediu virtual: python -m venv venv

Activați mediul: .\venv\Scripts\activate.ps1

Instalați dependențele: pip install -r requirements.txt

Configurați baza de date în settings.py (Local DB: root / alfabet).

Rulați migrarea: python manage.py migrate

Porniți serverul: python manage.py runserver

📂 Structura Proiectului
courses/: Logica principală pentru cursuri, formulare și vizualizări.

home/: Pagina principală și știri.

templates/: Fișierele HTML (Base, Cursuri, Înregistrare).

static/: Asset-uri CSS (Tailwind) și imagini.

media/: Materiale de curs încărcate (PDF-uri).

Dockerfile.prod & docker-compose.prod.yml: Configurația pentru Docker.

Autor: Paul (RoJackal)
