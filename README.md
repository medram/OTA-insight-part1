# OTA-insight-part1

### Linux installation guide:
Run the following commands one at a time:

```bash
mkdir OTA-insight && cd OTA-insight

git clone https://github.com/medram/OTA-insight-part1.git .

python3 -m venv venv

source venv/bin/activate

pip3 install -r requirements.txt

python3 manage.py migrate

python3 manage.py collectstatic --no-input --skip-checks

# than create a superuser account:
python3 manage.py createsuperuser

# Running the local server:
python3 manage.py runserver
```

Available API endpoints:
```bash
# Note: No slash “/” at the end of the URL.
GET - http://127.0.0.1:8000/invoices/2
```
