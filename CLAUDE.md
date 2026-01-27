# CLAUDE.md - AI Assistant Guide for BlackRoad

**Repository:** blackroad
**Organization:** BlackRoad-OS
**Last Updated:** 2026-01-27

---

## Overview

BlackRoad is the core monorepo of **BlackRoad OS** - an AI-first operating system platform focused on AI sovereignty. This repository contains:

- **Lucidia Core** - Specialized AI reasoning agents for physics, mathematics, chemistry, and more
- **The Light Trinity** - Unified intelligence, templating, and infrastructure system
- **Platform Integrations** - Multi-platform deployment and service configuration
- **AI Agent Identities** - Infrastructure and coordination agents (Aria, etc.)

---

## Repository Structure

```
blackroad/
├── packages/
│   └── lucidia-core/           # AI reasoning engines (Python)
│       ├── physicist.py        # Physics reasoning engine
│       ├── mathematician.py    # Math reasoning engine
│       ├── chemist.py          # Chemistry engine
│       ├── geologist.py        # Geology engine
│       ├── analyst.py          # Data analysis
│       ├── architect.py        # System design
│       ├── engineer.py         # Engineering calculations
│       ├── painter.py          # Visual generation
│       ├── poet.py             # Creative text
│       ├── speaker.py          # Speech/NLP
│       └── codex*.yaml         # Agent seed configurations
│
├── .trinity/                   # The Light Trinity System
│   ├── redlight/               # Templates & Brand
│   │   ├── templates/          # 18+ HTML brand templates
│   │   └── docs/
│   ├── greenlight/             # Project & Collaboration
│   │   ├── scripts/            # Memory templates
│   │   └── docs/               # 12+ integration docs
│   ├── yellowlight/            # Infrastructure & Deployment
│   │   └── scripts/
│   └── system/                 # Trinity Core documentation
│
├── .aria/                      # Aria agent identity
├── .github/                    # GitHub workflows & templates
│   └── workflows/              # CI/CD pipelines
├── integrations/               # Platform integration configs
│   ├── platforms.yaml          # Multi-platform deployment config
│   └── examples/               # Integration examples
│
├── package.json                # Monorepo root (Turborepo)
└── turbo.json                  # Turborepo configuration (if exists)
```

---

## Technology Stack

### Build System
- **Monorepo:** Turborepo 2.0+
- **Package Manager:** pnpm 9.0.0
- **Node.js:** 20.x

### Languages & Frameworks
- **Python:** 3.11+ (lucidia-core agents)
- **TypeScript/JavaScript:** Node.js services
- **YAML:** Configuration files
- **HTML/CSS:** Brand templates (Three.js powered)

### Deployment Platforms (Priority Order)
1. Railway (PaaS)
2. Vercel (Frontend/Serverless)
3. Cloudflare Pages/Workers (Static/Edge)
4. DigitalOcean (IaaS)
5. Raspberry Pi (Edge/IoT)

---

## The Light Trinity System

The Light Trinity is BlackRoad's unified intelligence, templating, and infrastructure system.

### RedLight (Templates & Brand)
**Location:** `.trinity/redlight/`

Visual identity and brand consistency:
- 18+ HTML brand templates for landing pages, animations, 3D worlds
- Three.js-powered interactive experiences
- Brand gradient: Amber → Hot Pink → Violet → Electric Blue

### GreenLight (Project & Collaboration)
**Location:** `.trinity/greenlight/`

Real-time intelligence and multi-Claude coordination:
- 14 integration layers
- 103+ template functions for event logging
- 200+ emoji states for visual language
- NATS event bus integration

### YellowLight (Infrastructure & Deployment)
**Location:** `.trinity/yellowlight/`

Infrastructure automation and deployment:
- Multi-platform deployment templates
- Codex integration (8,789+ reusable components)
- Server management across all infrastructure

---

## Development Workflows

### Running the Monorepo

```bash
# Install dependencies
pnpm install

# Run all packages in dev mode
pnpm dev

# Build all packages
pnpm build

# Lint all packages
pnpm lint
```

### Lucidia Core (Python)

```bash
cd packages/lucidia-core

# Install dependencies
pip install -r requirements.txt

# Run CLI
lucidia list                    # List available agents
lucidia run physicist --query "..."  # Run specific agent

# Start API server
lucidia api --port 8000
# Or: python -m lucidia_core.api
```

### Using Trinity Templates

```bash
# Source GreenLight templates
source .trinity/greenlight/scripts/memory-greenlight-templates.sh

# Log a deployment
gl_deployed "my-api" "v1.2.3" "production" "New feature deployed"

# Announce work
gl_announce "claude-agent" "Project Name" "1) Task 2) Task" "Goal"

# Source RedLight for brand templates
source .trinity/redlight/scripts/memory-redlight-templates.sh
```

---

## Brand Guidelines

### Required Colors
- **Hot Pink:** #FF1D6C (primary accent)
- **Amber:** #F5A623
- **Electric Blue:** #2979FF
- **Violet:** #9C27B0
- **Background:** #000000 (black)
- **Text:** #FFFFFF (white)

### Forbidden Colors
Do NOT use: #FF9D00, #FF6B00, #FF0066, #FF006B, #D600AA, #7700FF, #0066FF

### Golden Ratio Spacing
- Scale: 8px → 13px → 21px → 34px → 55px → 89px → 144px
- Line height: 1.618 (phi)

### Typography
- **Font:** SF Pro Display, -apple-system, sans-serif

### Gradients
```css
background: linear-gradient(135deg, #FF1D6C 38.2%, #F5A623 61.8%);
```

---

## Key Conventions

### Code Style
- Python: Follow PEP 8
- TypeScript: ESLint with project config
- Use type hints/annotations where applicable
- Keep functions focused and well-documented

### Git Workflow
1. Create feature branch from main
2. Make changes following brand/code guidelines
3. Submit PR with detailed description
4. All code becomes BlackRoad OS, Inc. property

### Commit Messages
- Use conventional commits when possible
- Be descriptive about the "why" not just the "what"

### File Naming
- Python: snake_case (e.g., `physicist.py`)
- TypeScript: camelCase for files, PascalCase for components
- Config: kebab-case (e.g., `platforms.yaml`)

---

## Agent Identities

### Aria (Infrastructure Queen)
**Location:** `.aria/`
- Role: Infrastructure Architecture & Cost Optimization
- Machine: aria64 (Raspberry Pi ARM64)
- Specializations: Zero-cost deployment, auto-healing, multi-cloud orchestration

### GreenLight Agent Identities
| Emoji | Agent | Role |
|-------|-------|------|
| Cece | Primary reasoning (Claude) |
| Lucidia | Recursive AI |
| Alice | Edge agent (Pi) |
| Silas | Creative (Grok) |
| Aria | Multimodal (Gemini) |
| Caddy | General (GPT) |

---

## CI/CD & GitHub Actions

### Main Workflows
- **ci.yml** - Build, lint, test on push/PR
- **trinity-compliance.yml** - Verify Trinity system integrity
- **auto-merge.yml** - Auto-merge approved PRs
- **security-scan.yml** - Security scanning
- **auto-deploy.yml** - Automated deployments

### Workflow Triggers
- `push` to main/master/develop
- `pull_request` to main/master/develop

---

## API Endpoints (Lucidia Core)

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/health` | GET | Health check and agent list |
| `/physicist/analyze` | POST | Physics analysis |
| `/physicist/energy-flow` | POST | Energy flow modeling |
| `/mathematician/compute` | POST | Mathematical computation |
| `/mathematician/prove` | POST | Proof assistance |
| `/chemist/analyze` | POST | Chemical analysis |
| `/geologist/terrain` | POST | Terrain analysis |
| `/analyst/insights` | POST | Data insights |
| `/architect/design` | POST | System design |

---

## Security

### Reporting Vulnerabilities
- **DO NOT** create public GitHub issues for security vulnerabilities
- Email: blackroad.systems@gmail.com

### Standards
- OWASP Top 10 security best practices
- NIST Cybersecurity Framework
- SOC 2 Type II controls (in progress)

---

## Important Files

| File | Purpose |
|------|---------|
| `package.json` | Monorepo root configuration |
| `.trinity/README.md` | Complete Trinity system guide |
| `.trinity/system/THE_LIGHT_TRINITY.md` | Trinity canonical documentation |
| `integrations/platforms.yaml` | Multi-platform deployment config |
| `.github/SECURITY.md` | Security policy |
| `packages/lucidia-core/README.md` | Lucidia agents documentation |

---

## Quick Commands Reference

```bash
# Monorepo
pnpm install          # Install all dependencies
pnpm dev              # Run development
pnpm build            # Build all packages
pnpm lint             # Lint all packages

# Lucidia Core
lucidia list          # List agents
lucidia api           # Start API server

# Trinity Templates
source .trinity/greenlight/scripts/memory-greenlight-templates.sh
gl_announce           # Announce work
gl_progress           # Update progress
gl_deploy             # Log deployment

# Git (follow these patterns)
git checkout -b feature/amazing-feature
git commit -m "Add amazing feature"
git push origin feature/amazing-feature
```

---

## Contact

- **Email:** blackroad.systems@gmail.com
- **CEO:** Alexa Amundson
- **Organization:** BlackRoad OS, Inc.
- **Website:** https://blackroad.io
- **Docs:** https://docs.blackroad.io

---

## License

**Proprietary** - BlackRoad OS, Inc. All rights reserved.

This software is provided for authorized use only. All contributions become the property of BlackRoad OS, Inc.

---

*"The Road to AI Sovereignty"* - BlackRoad OS
