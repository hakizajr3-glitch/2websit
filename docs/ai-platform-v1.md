# AI Multi-Agent App Platform (Atoms/Base44/Manus-Inspired) — Focused v1 Plan

## Positioning

**We build and operate subscription B2B SaaS products for non-technical founders.**

Core promise:
1. Ship a working full-stack SaaS from a short brief.
2. Continue improving it weekly using usage data.
3. Keep customer data safe with built-in backups and recoverability.

## What We Support at Launch

- Product type: web-first subscription SaaS
- Built-in capabilities:
  - Auth (email/password)
  - Team/workspace basics
  - Billing (Stripe subscriptions)
  - Dashboard + CRUD admin screens
  - Event tracking + weekly optimization suggestions
- Deployment target: one-click deploy to a managed platform

## Why Users Would Pick This Over General Builders

Most agent builders optimize for **first launch**. We optimize for **post-launch outcomes**:

- Automated “operator loop” after deployment
- Explainable, reviewable change plans
- Git-first workflow (branch, PR, tests, merge gates)
- Production safety defaults (backups, restores, alerts)

## v1 Agent Pipeline

### 1) Discovery Agent
Input: founder brief + optional competitor links

Output:
- ICP summary
- Jobs-to-be-done assumptions
- MVP scope recommendation

### 2) Product Spec Agent
Input: discovery package

Output:
- PRD-lite
- user stories + acceptance criteria
- risk/assumption list

### 3) Architecture Agent
Input: spec

Output:
- data model
- API contract
- component map
- deployment plan

### 4) Build Agent
Input: architecture package

Output:
- generated app scaffold
- database migrations
- auth + billing wiring
- CI checks + baseline tests

### 5) QA/Release Agent
Input: build output

Output:
- test report
- release checklist
- deploy + smoke-check evidence

### 6) Operator Agent (weekly)
Input: analytics + error logs + funnel data

Output:
- experiment ideas ranked by impact/confidence/effort
- auto-generated implementation PRs for approved experiments

## Integrated Backups and Recovery (v1)

- **Database backup policy**
  - nightly full backups
  - point-in-time recovery (PITR) window (7-14 days)
  - encrypted backup storage by default
- **Application state backup**
  - scheduled export of config, environment metadata, and schema snapshots
  - retention tiers: 7 days (hot), 30 days (warm), 90 days (cold)
- **Restore workflows**
  - one-click restore to a temporary environment for verification
  - controlled promote-to-production restore step
- **Recovery objectives**
  - target RPO: <= 24h for v1
  - target RTO: <= 2h for standard restore path
- **Reliability checks**
  - weekly automated restore drill in staging
  - alerting on backup failures and stale backups

## Integration Framework (v1)

A minimal but extensible integration layer so generated products connect to common business tools.

### Launch integrations

- Payments: Stripe
- Auth/identity: built-in email/password (OAuth in v1.1)
- Email: Resend or SendGrid
- Analytics: PostHog or Segment
- Support/CRM sync: HubSpot (contacts + lifecycle stages)

### Integration architecture

- connector interface (`auth`, `sync`, `webhook`, `healthcheck` methods)
- event bus for app events (`user_signed_up`, `trial_started`, `subscription_changed`)
- idempotency keys and replay-safe webhook processing
- per-tenant secrets management + key rotation
- integration health dashboard and retry queues

### Integration governance

- explicit scopes/permissions shown before connect
- audit log of integration actions
- tenant-level enable/disable controls

## Human-in-the-Loop Controls

- Stage approvals:
  - Spec approval
  - Architecture approval
  - Release approval
- Every stage includes:
  - rationale
  - alternatives considered
  - editable artifacts

## Developer-Grade Standards

- Git-native project structure
- Required checks before merge:
  - typecheck
  - lint
  - tests
- Environment separation:
  - preview
  - staging
  - production
- Infrastructure as code from day one

## Success Metrics (First 90 Days)

- Time-to-first-deploy (TTFD): target < 2 hours
- % projects shipped with no manual code edits: target 50%+
- Weekly accepted operator suggestions per app: target >= 1
- D30 retained builders/founders: target >= 30%
- Backup reliability: >= 99% successful scheduled backups
- Restore confidence: >= 1 successful restore drill/week
- Integration activation: >= 60% of projects connect at least 2 integrations

## 4-Week Build Plan

### Week 1
- Brief intake + spec generation
- Basic project scaffold generator

### Week 2
- DB schema generation + auth + dashboard CRUD
- Stripe subscription integration

### Week 3
- One-click deploy flow
- CI test + release checks
- Backup schedules + backup status visibility

### Week 4
- Analytics ingestion
- Weekly operator suggestions with one-click PR generation
- Integration hub v1 (Stripe, email, analytics, CRM sync)

## Non-Goals (v1)

- Native mobile app generation
- “Build anything” support outside SaaS dashboard pattern
- Autonomous production changes without user approval
- Unlimited connector marketplace at launch

## One-Sentence Thesis

**A focused AI product factory that not only ships your B2B SaaS quickly, but keeps operating and improving it every week with transparent, reviewable agent actions, built-in backups, and practical integrations.**


## Implementation Blueprint

For execution details (repo structure, agent contracts, template strategy, deployment stack, and operator data model), see `docs/mvp-architecture-blueprint.md`.


## Backend Framework Default (v1)

- Default stack for generated backends: **FastAPI (Python)**
- Secondary option for Node-centric teams: **NestJS**
- Framework choice is validated against:
  - project complexity and scaling profile
  - team language familiarity
  - ecosystem maturity and documentation quality
  - runtime performance targets

See `docs/mvp-architecture-blueprint.md` for the full backend framework decision guide.


## Backend Foundation and Builder Upgrade (Added Scope)

The implementation blueprint now includes two additive execution sections:

- **Working Backend Foundation**: concrete FastAPI project skeleton, dependencies, and orchestration flow
- **Builder Upgrade**: template engine + design generation + feature injection + UI polish path

See `docs/mvp-architecture-blueprint.md` sections "12) Working Backend Foundation" and "13) Builder Upgrade".

## Workspace Settings Coverage (Additive)

To align with expected product administration, include the following settings areas in the v1+ settings model. Existing settings remain unchanged; these are additive checks.

### Workspace Settings

- Basic information
- Plan and billing
- Credit usage
- Members
- Auth and security
- Integrations
- Skills
- Apps configuration

### Integrations Settings

- Connectors

### Account Settings

- Account settings
- MCP connections

## Prompt-to-Build and Text-to-Edit UX (Core Product Behavior)

The default user journey should be:

1. User describes what they want to create in plain language.
2. AI agents automatically plan and start building immediately.
3. User reviews progress/artifacts.
4. User can request changes by sending text instructions.
5. AI applies edits, regenerates affected components, and redeploys safely.

### Product requirement

- No mandatory technical form before first build.
- Free-form text edits are accepted throughout the lifecycle.
- Every edit request produces a tracked change plan and implementation result.

## Settings System (Expanded, Additive)

Keep existing settings and add missing settings only.

### Final settings structure

```text
Settings
 ├── Workspace
 ├── Basic information
 ├── Plan and billing
 ├── Credit usage
 ├── Members
 ├── Auth and security
 ├── Integrations
 │    └── Connectors
 ├── Skills
 ├── Apps configuration
 ├── Account
 │    └── Account settings
 └── MCP connections
```

This structure is additive and non-destructive by design.

## Interactive Build Flow (Describe → Auto Build → Modify by Text)

1. **User describes app in plain language**
   - Example: "I want a B2B SaaS dashboard for tracking marketing campaigns. Include auth, team features, billing, and charts."
2. **Planner Agent returns structured outputs**
   - spec (pages, features, data model)
   - UI suggestions
3. **AI starts building automatically**
   - Builder copies premium template, injects features, generates UI/backend artifacts
   - Deployer publishes preview/live stub on selected providers
4. **User requests changes in text**
   - Example: "Change charts to weekly trends and add onboarding flow."
   - Operator/Builder update spec, apply code changes, and redeploy preview

### Smooth-UX requirements

- always maintain preview branch before production changes
- keep human-in-the-loop for major/risky changes
- explain all AI changes in plain language
- allow rollback to previous version

## Atoms/Base44/Manus-Style Experience (Additive)

This platform should explicitly mirror the best parts of Atoms/Base44/Manus while optimizing for luxurious SaaS quality and interactive control.

### Core principles

1. natural-language input (text first, voice-supported)
2. multi-agent orchestration (Planner, Designer, Builder, Deployer, Operator)
3. immediate interactivity (chat-based edits and iterative rebuilding)
4. end-to-end output (frontend + backend + auth + billing + integrations)
5. human-in-the-loop approvals with rollback and plain-language change summaries

### Interactive lifecycle (required)

1. user describes product idea in text or speech
2. planner/designer generate product spec + UX direction
3. builder/deployer generate and publish functional SaaS preview
4. user sends iterative edits in chat/text/voice
5. operator + builder apply updates, show diffs, and redeploy safely

### Luxurious UI quality bar

- base template: Next.js + Tailwind + shadcn/ui + Lucide icons
- design generation: palette, typography, spacing, hierarchy
- polish pass: responsiveness, alignment, consistency, visual refinement
- continuous UX optimization via operator suggestions + user approvals
