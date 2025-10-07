# Minimal container for Strands agent on Amazon Bedrock AgentCore
# - Exposes port 8080
# - Starts your runtime entrypoint: strands_agent_DevOps_SRE.py (uses BedrockAgentCoreApp)
# - Runs as non-root

FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# (Optional) Set your AWS default region at runtime via env if you want to override the role/metadata.
# ENV AWS_DEFAULT_REGION=us-east-1

# Install runtime tools (curl for healthcheck)
RUN apt-get update && apt-get install -y --no-install-recommends curl && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install dependencies first (better layer caching)
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy your agent code
COPY . .

# Expose the AgentCore default port
EXPOSE 8080

# Health check hits the AgentCore app's /ping endpoint
HEALTHCHECK --interval=30s --timeout=5s --start-period=30s --retries=3 \
  CMD curl -f http://localhost:8080/ping || exit 1

# Create non-root user and switch
RUN useradd -m appuser
USER appuser

# Start the runtime (your file must call app.run() when __main__)
# If your file has a different name, change it here.
CMD ["python", "strands_agent_DevOps_SRE.py"]
