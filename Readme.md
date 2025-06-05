# Patient Management System (PAMS)

A Django-based web application for managing patient records and workflows.

---

## 🚀 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/vivekkushwaha373/patient_management_system.git
cd patient_management_system

python -m venv pams_env
source pams_env/bin/activate

pip install django python-decouple

cd claimbuddy_pams
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

```