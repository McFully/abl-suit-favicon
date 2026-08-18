# Critical Files - Suit Favicon

This document maps the core files that must be protected to ensure system stability.

## 1. Entry Point
- `main.py`: Application initialization and event loop.

## 2. Core Services
- `app/services/api_service.py`: External communication (Exclusivo Grok xAI).
- `app/services/image_service.py`: Neuronal processing and local export.
- `app/services/project_service.py`: Filesystem management.

## 3. Concurrency
- `app/workers/gen_worker.py`: Pipeline orchestration and threading logic.

## 4. UI Architecture
- `app/ui/wizard.py`: Main state machine for the user interface.
- `app/ui/pages.py`: Step definitions and input handling.

## 5. Build & Deployment
- `build_all.ps1`: Automated compilation and packaging script.
- `installer/setup.iss`: Inno Setup configuration.
