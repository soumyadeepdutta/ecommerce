# Django Ecommerce 
A full featured web application using Python Django Framework and MySQL.
## Features
1. User authentication
2. Add to cart (AJAX)
3. Previous order list

## Usage
Clone the repository <br/>
```commandline
git clone https://github.com/soumyadeepdutta/ecommerce.git
cd ecommerce
```
Install all the dependencies
```commandline
 pip install -r requirements.txt
```
Create database migrations
```commandline
python manage.py makemigrations
python manage.py migrate
```
Start the development server on port 8000
```commandline
python manage.py runserver
```
Follow http://127.0.0.1:8000 to view the homepage
