FROM ghcr.io/astral-sh/uv:python3.11-alpine

WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-cache

COPY . .
ENV PATH="/app/.venv/bin:$PATH"

CMD ["streamlit", "run", "app.py", "--server.port", "8501", "--server.address", "0.0.0.0"]