# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

"""
FastAPI application for the My Env Environment.
"""

import uvicorn

try:
    from openenv.core.env_server.http_server import create_app
except Exception as e:
    raise ImportError(
        "openenv is required for the web interface. Install dependencies with '\n    uv sync\n'"
    ) from e

try:
    from models import MyAction, MyObservation
    from .my_env_environment import MyEnvironment
except ModuleNotFoundError:
    from models import MyAction, MyObservation
    from server.my_env_environment import MyEnvironment


# Create the app with web interface and README integration
app = create_app(
    MyEnvironment,
    MyAction,
    MyObservation,
    env_name="my_env",
    max_concurrent_envs=1,
)


# ✅ ADD THIS ROOT ENDPOINT
@app.get("/")
async def root():
    return {
        "message": "Email Generator API is running",
        "docs": "/docs",
        "status": "healthy"
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)