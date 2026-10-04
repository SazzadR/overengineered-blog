# Overengineered Blog

A good rule of thumb in software engineering is to **keep things simple whenever possible**.

This project does the opposite.

**Overengineered Blog** is a deliberately overcomplicated blogging application built to experiment with architecture, infrastructure, and engineering practices that a normal blog absolutely does not need, but larger mission-critical systems often do.

## Table of Contents

- [Tech Stack](#tech-stack)
- [Roadmap](#roadmap)
- [Getting Started](#getting-started)
- [Non-Functional Experiments](#non-functional-experiments)
  - [Load Testing](#load-testing)
  - [Async Benefits for I/O-Bound Operations](#async-benefits-for-io-bound-operations)
- [Work in Progress](#work-in-progress)

## Tech Stack

- FastAPI
- PostgreSQL
- Docker
- Grafana k6

## Roadmap

- [x] Load testing with k6
- [ ] Primary-replica database architecture with replication
- [ ] Kubernetes
- [ ] CI/CD with Jenkins X
- [ ] CI/CD with GitHub Actions
- [ ] Observability with Prometheus, Grafana, and OpenTelemetry

## Getting Started

Start the application with:

```shell
cd core-backend && cp .env.example .env && cd ..

docker compose up -d
```

## Non-Functional Experiments

### Load Testing

The project uses [Grafana k6](https://k6.io/) for load testing.

Run the load test with:

```shell
docker compose --profile testing run --rm k6 \
  run /scripts/load-test.js
```

---

### Async Benefits for I/O-Bound Operations

It is easier to understand the benefit of async I/O by seeing it under load.

This experiment compares:

1. A synchronous version restricted to a single worker thread
2. An asynchronous version that can handle multiple requests while waiting for database I/O

Database connection pooling is also disabled so it does not affect the experiment.

#### 1. Run the synchronous version

The synchronous implementation exists in an older Git commit.

Instead of checking out that commit directly and losing the current README instructions, create a separate Git worktree:

```shell
# Stop the current containers to avoid port conflicts
docker compose down

# Create a worktree using the synchronous implementation
git worktree add ../overengineered-blog-sync c5c0af2b4c1920d3cf3cfd5e3d08c22c8236ef21

# Move into the worktree
cd ../overengineered-blog-sync

cp .env.example .env

docker compose up -d --build
```

In this version:

- FastAPI is limited to **1 thread**
- Starlette normally allows up to [40 thread-pool tokens](https://starlette.dev/threadpool/)
- Database connection pooling is disabled
- The [`healthcheck`](core-backend/src/main.py#L29) endpoint runs an intentionally slow SQL query that takes about **5 seconds**

Now send **10 concurrent requests**:

```shell
docker compose --profile testing run --rm k6 \
  run /scripts/load-test.js
```

Because only one synchronous request can execute at a time:

```text
10 requests × 5 seconds ≈ 50 seconds
```

![Synchronous Result](/docs/2026-10-04_14-56.png?raw=true "Synchronous Result")

#### 2. Clean up the synchronous worktree

```shell
# Run inside overengineered-blog-sync
docker compose down

# Return to the main repository
cd ../overengineered-blog

# Remove the temporary worktree
git worktree remove ../overengineered-blog-sync

# Start the current version
docker compose up -d --build
```

#### 3. Run the asynchronous version

Run the same load test again:

```shell
docker compose --profile testing run --rm k6 \
  run /scripts/load-test.js
```

The same **10 concurrent requests** now finish in roughly:

```text
≈ 5 seconds
```

![Asynchronous Result](/docs/2026-10-04_14-57.png?raw=true "Asynchronous Result")

While one request waits for database I/O, the event loop can continue processing other requests instead of blocking.

This demonstrates one of the key benefits of async for I/O-bound workloads.

## Work in Progress

More overengineering is coming.
