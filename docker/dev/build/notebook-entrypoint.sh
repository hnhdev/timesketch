#!/bin/bash
marimo edit --headless --no-token --host 0.0.0.0 --port 8081 --base-url /marimo /home/jovyan/work-marimo &
exec jupyter-lab "$@"
