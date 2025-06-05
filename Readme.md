# Patient Management System (PAMS)

A Django-based web application for managing patient records and workflows.

---

### use Credentials in .env

## 🔐 Environment Variables (`.env`)

Create a `.env` file in the root directory with the following content:

```bash
# Django Secret Key & Debug Mode
SECRET_KEY=your-secret-key-here
DEBUG=True

# PostgreSQL Database Configuration (Supabase)
DATABASE_NAME=postgres
DATABASE_USER=postgres.pgfsdnwnitlplwhakzii
DATABASE_PASSWORD=B74KfK9Dc&Gb*#Z
DATABASE_HOST=aws-0-ap-south-1.pooler.supabase.com
DATABASE_PORT=6543

# Admin Credentials (for local development)
ADMIN_USERNAME=vivek
ADMIN_PASSWORD=12345678



## 🚀 How to Run Locally

### 1. Clone the Repository



```bash
git clone https://github.com/vivekkushwaha373/patient_management_system.git
cd patient_management_system

python -m venv pams_env
source pams_env/bin/activate

pip install django python-decouple psycopg2-binary



cd claimbuddy_pams
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

```


