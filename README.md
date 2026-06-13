# AI DevOps Assignment

## Project Overview

This project demonstrates a production-style deployment of a FastAPI application using Docker and Docker Compose on an AWS EC2 instance.

The application is deployed behind an NGINX reverse proxy and integrates PostgreSQL and Redis services. Automated deployment is implemented using GitHub Actions CI/CD.

---

## Technology Stack

* FastAPI
* Python 3.12
* Docker
* Docker Compose
* PostgreSQL 16
* Redis 7
* NGINX
* GitHub Actions
* AWS EC2 (Ubuntu 26.04 LTS)
* UFW Firewall
* Fail2Ban

---

## Architecture Diagram

```text
GitHub Repository
        |
        v
GitHub Actions
        |
        v
AWS EC2 Ubuntu Server
        |
        v
Docker Compose
        |
+----------------+
|     NGINX      |
+----------------+
        |
        v
+----------------+
|    FastAPI     |
+----------------+
     |       |
     |       |
     v       v
  Redis   PostgreSQL
```

---

## Project Structure

```text
ai-devops/
│
├── app/
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── nginx/
│   └── nginx.conf
│
├── scripts/
│   └── backup.sh
│
├── .github/
│   └── workflows/
│       └── deploy.yml
│
├── docker-compose.yml
├── .env.example
├── README.md
└── screenshots/
```

---

## Application Features

### Root Endpoint

```http
GET /
```

Response:

```json
{
  "message": "AI DevOps Assignment Running"
}
```

---

### Health Check Endpoint

```http
GET /health
```

Response:

```json
{
  "status": "healthy"
}
```

Purpose:

* Container health verification
* Monitoring integration
* Load balancer health checks

---

### Redis Test Endpoint

```http
GET /redis-test
```

Response:

```json
{
  "redis": "working"
}
```

Purpose:

* Redis connectivity verification
* Cache service validation

---

## Dockerization

The FastAPI application is containerized using Docker.

### Dockerfile Responsibilities

* Uses Python 3.12 slim image
* Installs dependencies
* Copies application code
* Starts FastAPI using Uvicorn

Benefits:

* Consistent deployment
* Environment portability
* Easy scaling

---

## Docker Compose Setup

The application stack is managed through Docker Compose.

### Services

#### FastAPI

Application container serving API requests.

#### PostgreSQL

Database container used for persistent storage.

#### Redis

In-memory cache and message broker.

#### NGINX

Reverse proxy that forwards incoming traffic to FastAPI.

---

## Environment Variables

Environment variables are managed through a `.env` file.

Example:

```env
POSTGRES_USER=admin
POSTGRES_PASSWORD=admin123
POSTGRES_DB=devopsdb
REDIS_HOST=redis
```

Benefits:

* Configuration separation
* Security
* Portability

---

## Deployment Process

### Server

AWS EC2 Ubuntu 26.04 LTS

### Deployment Steps Performed

1. Launch EC2 instance
2. Configure Security Groups
3. Install Docker
4. Install Docker Compose
5. Clone GitHub repository
6. Create environment variables
7. Start services using Docker Compose
8. Verify service health
9. Configure security tools

---

## CI/CD Pipeline

GitHub Actions is used for Continuous Integration and Continuous Deployment.

### Trigger

```yaml
on:
  push:
    branches:
      - main
```

### Deployment Workflow

```text
Developer Push
        |
        v
GitHub Repository
        |
        v
GitHub Actions
        |
        v
SSH into EC2
        |
        v
git pull origin main
        |
        v
docker compose up -d --build
        |
        v
Updated Application
```

### Benefits

* Automated deployment
* Reduced manual effort
* Consistent releases

---

## Logging Strategy

Docker container logs are used.

Examples:

```bash
docker logs fastapi
docker logs nginx
docker logs postgres
docker logs redis
```

Benefits:

* Centralized container logs
* Easy troubleshooting
* Operational visibility

---

## Backup Strategy

A backup script is provided:

```text
scripts/backup.sh
```

### Command Used

```bash
docker exec postgres pg_dump -U admin devopsdb > backup.sql
```

### Purpose

* Database backup generation
* Disaster recovery preparation
* Operational resilience

---

## Restart Strategy

Containers are managed using Docker Compose.

### Manual Restart

```bash
docker compose restart
```

### Rebuild Deployment

```bash
docker compose up -d --build
```

This ensures application recovery after updates or failures.

---

## Security Measures

### UFW Firewall

Configured rules:

```text
22/tcp  -> SSH
80/tcp  -> HTTP
443/tcp -> HTTPS
```

Status:

```bash
sudo ufw status
```

---

### Fail2Ban

Installed and enabled.

Purpose:

* Protects against brute-force attacks
* Monitors authentication failures
* Automatically blocks malicious IPs

Verification:

```bash
sudo systemctl status fail2ban
```

---

## SSL Setup Approach

This assignment uses a public EC2 IP address.

In a production environment:

1. Purchase or configure a domain.
2. Point DNS to EC2.
3. Install Certbot.
4. Generate Let's Encrypt certificates.
5. Configure NGINX for HTTPS termination.

Example:

```bash
sudo certbot --nginx
```

Benefits:

* HTTPS encryption
* Secure communication
* Trusted certificates

---

## Public Application URL

Application:

http://13.206.197.60

Health Check:

http://13.206.197.60/health

Redis Validation:

http://13.206.197.60/redis-test

---

## Outcome

Successfully deployed a production-style FastAPI application with:

* Dockerized services
* Docker Compose orchestration
* PostgreSQL integration
* Redis integration
* NGINX reverse proxy
* GitHub Actions CI/CD
* EC2 deployment
* Health checks
* Backup strategy
* Security hardening using UFW and Fail2Ban

This demonstrates practical implementation of DevOps deployment, automation, infrastructure management, and production readiness.
And successfully deployed the project.
