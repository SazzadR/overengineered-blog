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

#### Async Benefits for I/O Bound Operation - A Practical Demonstration.

It's always more enlightening to see things in action rather than just knowing.
So here is a demonstration of the benefits of async for I/O bound operation.

* We will limit the FastAPI application to use only 1
  thread (<a href="https://starlette.dev/threadpool/" target="_blank">default 40</a>)
  and also disable the database pooling.

```shell
git worktree add ../overengineered-blog-sync c5c0af2b4c1920d3cf3cfd5e3d08c22c8236ef21
# Stop the current docker containers to prevent port conflicts
docker compose down
# Open a new terminal tab and go to that worktree and run the docker containers
cd ../overengineered-blog-sync
docker compose up -d
```

* We are running expensive SQL in the [healthcheck](core-backend/src/main.py#L29) API. Which will take 5 seconds to
  run.
* Now let's test with 10 concurrent user. It will take `(10 * 5) ≈ 50` seconds to complete.

```shell
docker compose --profile testing run --rm k6 \
  run /scripts/load-test.js
```
![Without Async](/docs/2026-10-04_14-56.png?raw=true "Without Async")

---

### Work in progress...
