# AutoMatters : Free‑First, Scalable Study‑Visa Automation

Welcome to **VisaMate‑AI**, an end‑to‑end platform that automates the Canada study‑visa workflow for Indian students—SOP writing, document OCR, checklist tracking, and file packaging—while running entirely on permanent free tiers.

---

## ✨ Key Features

* **Edge‑native API** on Cloudflare Workers (100 k req/day free)
* **FastAPI core** with Supabase Auth & Postgres (500 MB free)
* **Async background worker** (Render 750 CPU‑h/mo free)
* **AI agents** (Llama‑3 via Together AI, \$1 ≈ 10 M tokens free)
* **Event backbone** with Cloudflare Queues (5 k msg/s free)
* **WhatsApp & Stripe** integrations for alerts and pay‑per‑SOP revenue

---

## 🏗️ High‑Level Architecture

```
┌────────────────────────── Client (Web / Mobile / WhatsApp) ──────────────────────────┐
│                                                                                     │
│   1. HTTPS request ➜  Cloudflare Worker  ➜ 2. JWT/Auth & Rate‑limit                  │
│                                                                                     │
│   ┌───────────────┐             ┌────────────────────────┐                          │
│   │ Workers  KV   │             │  FastAPI  /api/*       │                          │
│   │ (quota cache) │             │  (stateless replicas)  │                          │
│   └───────┬───────┘             └──────────┬─────────────┘                          │
│           │ 3. signed URLs / vectors / events         │                            │
│           ▼                                        async                           │
│   ┌───────────────┐   SQL   ┌────────────────┐   ⬅───────────┐                     │
│   │ Supabase PG   │◀────────│  Supabase S3   │              │                     │
│   └───────────────┘         └────────────────┘              │                     │
│          ▲                          ▲                       │                     │
│          │  OCR‑JSON                │  ZIP file             │                     │
│          └──────────────┬───────────┘                       │                     │
│                         │ enqueue (Cloudflare Queue)        │                     │
│                         ▼                                   │                     │
│               ┌──────────────────────┐ 5. OCR / embeddings  │                     │
│               │ Render Worker (CPU)  │──────────────────────┘                     │
│               └──────────────────────┘                                             │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

*Fast path (edge ➜ API) stays < 100 ms; heavy tasks are off‑loaded to the worker.*

---

## 📂 Repository Layout

```
apps/          # entry‑points (api, worker)
services/      # business orchestration (DB, storage, queue)
agents/        # pure AI / LangGraph logic (no direct I/O)
libs/          # framework‑free helpers (DTOs, storage, LLM client)
models/        # SQLAlchemy schema
compose/       # Dockerfiles for api & worker + edge‑worker bundle
infra/         # Terraform / wrangler / Render blueprints
db/            # Alembic migrations
tests/         # pytest suites
colab/         # R&D notebooks (export ➜ agents)
```

---

## ⚙️  Quick Start (Local Dev)

```bash
# clone and enter
git clone https://github.com/<org>/visamate-ai.git
cd visamate-ai

# env vars
cp .env.example .env.dev  # fill Supabase / Together AI keys

# bring up full stack (Postgres, Redis, MinIO, API, Worker)
docker compose -f docker-compose.dev.yml up --build

# check health
curl http://localhost:8000/healthz
```

Hot‑reload is enabled for the API container; edits trigger `uvicorn --reload`.

---

## 🚀 First Deploy (Free Tier)

```bash
# 1 – Edge Worker
cd compose/edge-worker
wrangler deploy

# 2 – API & Background Worker (Render Blueprint)
git push render main
```

---

## 🧩 Scaling Knobs

| Signal                        | Next Step                                  |
| ----------------------------- | ------------------------------------------ |
| >100 k req/day                | Cloudflare Workers Paid (US \$5/mo)        |
| >500 k Redis ops/mo           | Upstash pay‑go (₹0.2 per 100 k cmds)       |
| >1 GB Supabase Storage        | Move cold files ➜ Cloudflare R2            |
| >1 M vectors / >3 worker pods | Migrate Chroma ➜ Pinecone serverless       |
| Long OCR >15 min              | Split to `worker-ocr` on Railway or Lambda |

---

## 👥 4‑Day Sprint Split

| Day | You (AI Lead)                                 | Friend (Data/Infra Lead)                |
| --- | --------------------------------------------- | --------------------------------------- |
| 1   | Build `agents/sop_generator` stub; unit tests | Terraform CF & Supabase; CI pipeline    |
| 2   | `/routes/auth.py`, `/next-step` logic         | `services/documents/parser.py` + Queue  |
| 3   | Embeddings + Stripe pay‑wall                  | `services/visa/packager.py`, WhatsApp   |
| 4   | OTEL tracing, k6 load‑test                    | Render deploy, quota alerts, purge cron |

---
