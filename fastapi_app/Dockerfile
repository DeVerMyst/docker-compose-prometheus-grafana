FROM ghcr.io/astral-sh/uv:python3.11-alpine

WORKDIR /app
# Copier les fichiers de dépendances
COPY pyproject.toml uv.lock ./
# Installer les dépendances sans installer le projet lui-même
RUN uv sync --frozen --no-cache

COPY . .
# Utiliser le venv créé par uv
ENV PATH="/app/.venv/bin:$PATH"

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]