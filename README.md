# Overengineered Blog

A good rule of thumb in software engineering is to **keep it simple whenever possible**.

This project does the opposite.

**Overengineered Blog** is a deliberately overcomplicated blogging application built to experiment with the kind of 
architecture and infrastructure that a normal blog absolutely does not need.
But are indispensable for mission-critical business applications.

## Tech Stacks
- FastAPI
- PostgreSQL
- Docker
- Grafana k6

## To-Do
- [x] Load testing with k6
- [ ] Master-Slave DB architecture with replication
- [ ] Kubernetes
- [ ] CI/CD with Jenkins X 
- [ ] CI/CD with Github actions
- [ ] Observability with Prometheus, Grafana and OpenTelemetry

## Installation

To start the application simply run:
```shell
docker compose up -d
```

## Non-Functional Features

### Load Testing

We added [Grafana k6](https://k6.io/) for load-testing. To load-test the APIs run the following:

```shell
docker compose --profile testing run --rm k6 \            
  run /scripts/load-test.js
```

---

### Work in progress...
