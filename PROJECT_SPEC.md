# Project Specification: Lawflow Mono-Repo

This document outlines the architecture, modules, and development workflow for the **Lawflow** application.

---

## 1. Tech Stack

- **Backend**
  - Python 3.11
  - FastAPI
  - SQLAlchemy ORM
  - Alembic for database migrations

- **Frontend**
  - React 18 (Vite)
  - TypeScript

- **Async Tasks**
  - Celery
  - Redis

- **CLI**
  - Typer

- **Testing**
  - pytest (backend)
  - React Testing Library (frontend)

- **Containerization**
  - Docker
  - docker-compose

- **IDE**
  - VS Code workspace settings
  - Recommended extensions (see `.vscode/extensions.json`)

---

## 2. Services / Modules

All modules live under `services/` in the mono-repo. Each module has its own package, stub folder structure, interface definitions, placeholder functions, and unit tests.

1. **intake**
   - Natural-language CLI wrapper and REST endpoint
   - Entry point: `services/intake/main.py`
   - Defines Typer CLI command `lawflow intake`

2. **clarifier**
   - Follow-up question engine for missing or ambiguous inputs
   - Entry point: `services/clarifier/main.py`

3. **query_builder**
   - Composes Boolean/keyword Westlaw queries
   - Entry point: `services/query_builder/main.py`

4. **executor**
   - Runs headless browser or API-based Westlaw searches
   - Entry point: `services/executor/main.py`

5. **cocounsel**
   - Orchestrates AI loops via CoCounsel
   - Entry point: `services/cocounsel/main.py`

6. **retriever**
   - Fetches and stores documents
   - Entry point: `services/retriever/main.py`

7. **analyzer**
   - Computes weighted scores and citation analysis
   - Entry point: `services/analyzer/main.py`

8. **reporter**
   - Generates final memo with audit-log links
   - Entry point: `services/reporter/main.py`

Each module includes:
- `__init__.py` (Python) or `index.tsx` (TypeScript)
- Service interface definitions
- Placeholder functions for Westlaw API and CoCounsel prompts
- Basic unit-test file under `tests/`

---

## 3. Cross-Cutting Concerns

- **Credential Management**
  - `.env` for local secrets
  - Encrypted secrets in Docker

- **Audit Log**
  - Central table schema defined in `common/models/audit_log.py`

- **Docker Compose**
  - Wires all services + Redis + Postgres
  - File: `docker-compose.yml`

- **Root Manifests**
  - `requirements.txt` (Python dependencies)
  - `package.json` (frontend dependencies)

- **VS Code Configuration**
  - Workspace settings: `.vscode/settings.json`
  - Debug launch profiles: `.vscode/launch.json`

- **Top-Level README**
  - Overview of modules and instructions to build, test, and run

---

## 4. CLI & UI Workflow

### CLI (`lawflow`)

Runs the full pipeline in console:
```
$ lawflow --query "search terms"
```
Outputs progress logs and final report text.

### React UI

A multi-step wizard showing:
1. **Intake**
2. **Clarify**
3. **Run**
4. **Refine**
5. **View Report**

Components live under `web/src/components/` with progress indicators and async updates.

---

## 5. Test-Driven Development Approach

1. **Write tests** for each module interface and workflow step
2. **Implement minimal stubs** to satisfy tests
3. **Iteratively expand functionality** with passing tests
4. **Use pytest** (backend) and **React Testing Library** (frontend)

---

_Last updated: June 20, 2025_
