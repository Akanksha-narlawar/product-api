# E-Commerce Product API

A REST-based Product API built using Python Flask and Docker.

## Endpoints

- GET /health
- GET /products
- POST /products
- PUT /products/<id>
- DELETE /products/<id>

## Environment Variables

- APP_ENV - Application environment
- DB_HOST - Database host or future database configuration
- APP_PORT - Application port

## Run with Docker

Build the image:

```bash
docker build -t product-api:1.0 .