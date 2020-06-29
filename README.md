# EmployeeWorkStatusManagement
#Prerequisites

python3.7

redis

#Create virtual environment in python3.7
 
 virtualenv venv --python=python3.7
 
 source venv/bin/activate

#Install requirements
 
pip install -r requirements.txt
 
#Migrate
 
 python manage.py migrate
 
#Create User

 python manage.py createsuperuser

#Run project

 python manage.py runserver
 
#Run celery(For generate weekly report )

 Execute commands in terminals(different tab)
 1. redis-server
 2. celery -A employee_management worker -l info
 3. celery -A employee_management beat -l info
 
 