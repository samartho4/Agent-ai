# AutoMatters · VisaMate‑AI

*Free‑First, Policy‑Aware Study‑Visa Platform for Indian SDS Applicants & Certified Consultants*

Business Model -  https://www.canva.com/design/DAGqJ9adkzk/h7vRg4dKJIEjPtH_P-YHMw
---

## 🚀 Why AutoMatters?

> 433 k Indian applications reached IRCC last cycle. 15 % were refused—mostly for missing docs, stale rules, or unlicensed agents. AutoMatters turns **policy‑aware AI + RCIC supervision** into a workflow that costs ₹0 until scale and pays for itself with every SOP, file, or consultant seat sold.

---

## ✨ Flagship Feature Set

| Layer                                  | Student Value                           | Consultant Value                  | Platform Revenue                |
| -------------------------------------- | --------------------------------------- | --------------------------------- | ------------------------------- |
| **Smart Intake** (voice forms, doc‑AI) | Upload once; auto‑parse marksheets      | 3× faster client onboarding       | ↑ Pro‑file conversion           |
| **Policy‑Live Checklist**              | Zero guesswork; 20‑day SDS promise      | Lower rework cost                 | Seat licence churn ↓            |
| **ML Risk‑Score (89 % acc.)**          | Approval probability before paying fees | Prioritise high‑probability files | Add‑on ₹799/score               |
| **Scholarship & Funding Planner**      | Finds ₹1–2 L grants                     | Upsell to premium package         | Part of Pro (₹2 499/file)       |
| **One‑click ZIP + RPA Upload**         | No portal maze                          | File 200 cases/agent/mo           | Seat ₹15 000/mo + token overage |
| **WhatsApp Multilingual Bot**          | Real‑time status & reminders            | White‑label notifications         | Template pass‑through           |
| **Community + Badge Engine**           | Peer/alumni answers + LinkedIn badge    | Lead‑gen & brand halo             | Futures: Alumni SaaS            |
| **Consultant Certification**           | “VisaMate‑Certified” shield on profiles | Trust signal = more clients       | ₹18 000 exam + renewals         |

---

## 🏗  Four‑Tier System Anatomy (Exec View)

```
T┌────────────────────────────────────────────────────────────────────────────┐
│                          Tier 1  ▸  DATA INGESTION                        │
│ ┌─────────────────────┐  ┌─────────────────────┐  ┌─────────────────────┐ │
│ │ Smart Forms (Voice) │  │ Gen-AI Doc Extract  │  │ Policy + Quota Craw │ │
│ └──────────┬──────────┘  └──────────┬──────────┘  └──────────┬──────────┘ │
└────────────┼────────────────────────┼────────────────────────┼────────────┘
             ▼                        ▼                        ▼
      (Supabase PG + RLS)       (Supabase PG + RLS)       (Supabase PG)               Uni/Scholarships ETL

            ╔═══════════════════════════════════════════════════╗
            ║          SHARED  SERVICES (Zero-Trust)           ║
            ║  Postgres RLS │ Storage SSE-KMS │ CF Queues      ║
            ║  Chroma/Pinecone │ Upstash Redis │ Audit Log     ║
            ╚═══════════════════════════════════════════════════╝

┌────────────────────────────────────────────────────────────────────────────┐
│                         Tier 2  ▸  ELIGIBILITY & ML                       │
│ ┌─────────────────────┐    ┌──────────────────────────────────────────┐   │
│ │  SDS Rule Engine    │──▶ │  ML Risk-Score API (89 % accuracy)      │   │
│ └─────────────────────┘    └──────────────────────────────────────────┘   │
└────────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
┌────────────────────────────────────────────────────────────────────────────┐
│                         Tier 3  ▸  PACKAGE BUILDER                        │
│ ┌───────────────┐  ┌───────────────────┐  ┌───────────────────────────┐   │
│ │ SOP Generator │  │ Financial Planner │  │ PAL / TAL Validator      │   │
│ │ (Llama-3 RAG) │  └─────────┬─────────┘  └───────────────────────────┘   │
│ └───────────────┘            │                                           │
└──────────────────────────────┼────────────────────────────────────────────┘
                               ▼
┌────────────────────────────────────────────────────────────────────────────┐
│                      Tier 4  ▸  SUBMISSION OPTIMIZER                      │
│ ┌─────────────────────┐  ┌───────────────────┐  ┌──────────────────────┐  │
│ │ Quota Monitor       │  │ RPA Uploader →    │  │ Human RCIC Review    │  │
│ │  (Prov & IRCC)      │  │    IRCC Portal    │  └──────────────────────┘  │
│ └─────────────────────┘  └───────────────────┘                            │
└────────────────────────────────────────────────────────────────────────────┘

                
```

*Shared spine:* Supabase PG (RLS+pgcrypto) · Supabase Storage ▶ CF R2 · Cloudflare Queues · Chroma▶Pinecone · Upstash Redis.

---

## 🔌 API & Webhook Hub

| Direction                                                                                                | Endpoint / Hook                | Auth  | Purpose                                          |
| -------------------------------------------------------------------------------------------------------- | ------------------------------ | ----- | ------------------------------------------------ |
| **Inbound**                                                                                              | `POST /webhook/stripe`         | HMAC  | Payment -> unlock Pro features                   |
|                                                                                                          | `POST /webhook/proctor`        | Token | Exam result -> set `consultant.status=certified` |
| **Outbound**                                                                                             | `POST /uni/{code}/hook`        | mTLS  | Push admitted‑list CSV & scholarship matches     |
|                                                                                                          | `POST /consultant/{id}/review` | JWT   | RCIC review payload & sign‑off                   |
|                                                                                                          | IRCC RPA upload (headless)     | —     | Submit ZIP, then `status‑webhook` back           |
| *All events also land in `event_bus` table; partners poll `GET /status/{req_id}` to avoid chatty hooks.* |                                |       |                                                  |

---

## 🛡  Compliance Blueprint

* **Encryption‑at‑Rest** – SSE‑KMS on buckets, `pgcrypto` for PII columns.
* **Row‑Level Security** – JWT tenant‑ID guards every SELECT.
* **Audit Trail** – immutable `audit_log` partitions; Logpush to R2 (90‑day WORM).
* **Human‑in‑Loop** – RCIC must click **Approve** before RPA uploads.
* **Pen‑Test & SOC‑2** – scheduled Q3 once ARR > ₹6 Cr.

---

## 📊 Scalability Levers
using aws from now on

| Signal              | Next Move                            | Cost Δ                   |
| ------------------- | ------------------------------------ | ------------------------ |
| >100 k edge req/day | CF Workers \$5 plan                  | +\$5/mo                  |
| >1 GB hot storage   | Auto‑tier older files to R2          | +\$0.015/GB              |
| >1 M vectors        | Spin Pinecone serverless (pay‑go)    | +\$8/M RU                |
| ML inference >50 ms | Deploy Fine‑tuned Llama‑3 on GPU pod | +₹14/hr (GPUs on‑demand) |

---

## 💻 Quick Start (Local Dev)

```bash
git clone https://github.com/<org>/visamate-ai.git
cd visamate-ai
cp .env.example .env.dev && nano .env.dev   # fill Supabase, Cloudflare, Together, Gemini, Pinecone & EduCanada keys
docker compose -f docker-compose.dev.yml up --build
open http://localhost:8000/docs   # Swagger UI
```

### Demo Document Upload

1. Open `frontend/index.html` in your browser.
2. Select a file and click **Upload**. The page submits to `/documents/upload` and shows the saved filename.


---

## 🌍 First Deploy (All Free‑Tier)

```bash
# Edge Worker
yarn install -g wrangler
cd compose/edge-worker && wrangler deploy
# API & Worker
git push render main   # Render auto‑blueprint
```

Live staging appears at `https://visamate-api.onrender.com/docs`.

---


## 🤝 Community & Marketplace Road‑Map

1. **Q2 Gate** (10 k MAU, NPS 60) – Launch alumni mentor hub & badge engine.
2. **Q3 Gate** (1 k paid files) – Open consultant marketplace; certification exam live.
3. **Q4 Gate** (ARR ₹6 Cr) – Add AUS/USA crawlers + accommodation affiliate board.

---

### License

MIT © 2025 AutoMatters Team
a cache) │             │  (stateless replicas)  │                          │
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
