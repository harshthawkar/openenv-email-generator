---
title: Leave Request Email Generator
emoji: 📧
colorFrom: blue
colorTo: yellow
sdk: docker
pinned: false
app_port: 8000
base_path: /web
tags:
  - openenv
---

# Leave Request Email Generator

An OpenEnv environment that generates professional leave request emails from user messages.

## Quick Start

```python
from my_env import MyAction, MyEnv

# Create environment
env = MyEnv.from_docker_image("my_env-env:latest")

# Reset environment
result = env.reset()
print(f"Reset: {result.observation.echoed_message}")

# Generate leave email
result = env.step(MyAction(message="I need leave for 2 days due to personal work"))
print(f"Email:\n{result.observation.echoed_message}")
print(f"Message length: {result.observation.message_length}")

env.close()

## Project Structure

```
my_env/
├── .dockerignore         # Docker build exclusions
├── __init__.py            # Module exports
├── README.md              # This file
├── openenv.yaml           # OpenEnv manifest
├── pyproject.toml         # Project metadata and dependencies
├── uv.lock                # Locked dependencies (generated)
├── client.py              # MyEnv client
├── models.py              # Action and Observation models
└── server/
    ├── __init__.py        # Server module exports
    ├── my_env_environment.py  # Core environment logic
    ├── app.py             # FastAPI application (HTTP + WebSocket endpoints)
    └── Dockerfile         # Container image definition
```
