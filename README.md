# SPACE-Y Backend Assignment

This repository contains the backend implementation for an on-counter billing system designed for a small-scale shopping mall. The backend is developed using Django and Django Rest Framework, utilizing Generic Views with a PostgreSQL database.

## Statement

Build a backend for an on-counter billing system that enables the following mandatory features:
- Authenticate employees
- Manage products (Add, Update, Delete)
- Manage customers (Add, Update, Delete)
- Bill customers using cash payment method

Additionally, deploy the backend on a cloud platform (e.g., AWS, Google Cloud, Azure, Heroku, Python Anywhere) and ensure that the PostgreSQL database is hosted for the application to function correctly. The APIs should be browsable via the Swagger interface using something like drf-spectacular.

## Features Implemented

- *Authentication*
  - Employees can authenticate to access the system securely.

- *Product Management*
  - *Add, Update, Delete*: Products can be added to, updated in, or removed from the system.

- *Customer Management*
  - *Add, Update, Delete*: Customers can be added to, updated in, or removed from the system.

- *Billing*
  - Customers can be billed for purchases using the cash payment method.

### Endpoints

- *Home*: /home/ - Main landing page of the application.
- *Products*: /products/ - Endpoint to manage products.
- *Customers*: /customers/ - Endpoint to manage customers.
- *Main Page*: /main/ - Main page of the application.
- *Add Bill*: /add_bill/ - Endpoint to create a bill for a customer.
- *Add Product*: /add_product/ - Endpoint to add a new product.
- *Product List*: /product_list/ - Endpoint to list all products.
- *Customer List*: /customer_list/ - Endpoint to list all customers.
- *Delete Product*: /delete_product/<int:product_id>/ - Endpoint to delete a specific product.
- *Update Product*: /update_product/<int:product_id>/ - Endpoint to update a specific product.
- *Delete Customer*: /delete_customer/<int:customer_id>/ - Endpoint to delete a specific customer.
- *Add Customer*: /add_customer/ - Endpoint to add a new customer.

## Deployment

The backend is deployed on [Render](https://billingsystem-52rq.onrender.com/) and can be accessed at [Render App URL]. The PostgreSQL database is also hosted to support the application's functionalities.

### API Documentation

The API documentation is available via Swagger UI at /api. Please note that the current Swagger UI returns HTML documentation and is not integrated directly with the REST API.

## Bonus Features (Not Implemented)

- *Analytics API*: Provides insights such as the top-selling employee and product.
- *JWT Authentication*: Supports JWT for enhanced authentication and security.

### Admin Credentials

username: harshith

password: 1234

### Employee credentials

usernames: Raju

password: raju