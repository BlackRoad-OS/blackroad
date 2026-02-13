# CLAUDE.md

This file provides guidance for AI assistants working with the **BlackRoad** repository — the central monorepo for the BlackRoad OS ecosystem ("The Road to AI Sovereignty").

## Project Overview

BlackRoad is a multi-language AI infrastructure and DevOps automation ecosystem containing:

- **`tools/`** — 30 CLI tools (Zsh/shell scripts) providing the `br` developer toolkit
- **`packages/lucidia-core/`** — Python package with 10+ domain-specific AI reasoning agents (FastAPI/Pydantic)
- **`orgs/`** — Multi-org structure (ai, core, enterprise, personal) managing 100+ repositories
- **`.trinity/`** — Light Trinity system (RedLight/GreenLight/YellowLight) for brand, intelligence, and infrastructure
- **`integrations/`** — Platform integration configs (Railway, Vercel, Cloudflare, DigitalOcean, etc.)
- **`.aria/`** — Aria agent identity (Infrastructure Queen, Raspberry Pi ARM64)
- **`tests/`** — Test suite

## Build & Package Management

- **Package manager**: pnpm v9.0.0 (specified in `package.json` `packageManager` field)
- **Build orchestration**: Turbo v2.0.0 (monorepo)
- **Python build**: Hatchling (via `pyproject.toml`)

### Key commands

```bash
pnpm install          # Install JS/TS dependencies
pnpm dev              # turbo dev — start dev servers
pnpm build            # turbo build — production build
pnpm lint             # turbo lint — run linters

# Python (Lucidia Core)
pip install -e "packages/lucidia-core[dev]"   # Install with dev deps
pytest                                         # Run Python tests
black --check .                                # Check formatting
ruff check .                                   # Lint
mypy .                                         # Type check
```

## CI/CD

The main CI pipeline (`.github/workflows/ci.yml`) runs on push/PR to `main`, `master`, or `develop`:

1. Node.js 20 setup + `npm ci`
2. Python 3.11 setup + `pip install`
3. Lint, type-check, test, build (all conditional on relevant files existing)

Additional workflows in `.github/workflows/`:
- `ai-ml-deploy.yml` — AI/ML model deployment
- `auto-deploy.yml` — Automatic deployment
- `auto-label.yml`, `auto-merge.yml`, `blackroad-auto-merge.yml` — PR automation
- `blackroad-codeql-analysis.yml`, `security-scan.yml` — Security scanning
- `trinity-compliance.yml` — Light Trinity system validation
- `tunnel-deploy.yml` — Tunnel-based deployment
- `stale-issues.yml` — Stale issue management
- `blackroad-agents.yml` — Agent coordination

## Code Style & Linting

### Python (configured in `packages/lucidia-core/pyproject.toml`)

| Tool | Setting |
|------|---------|
| **Black** | `line-length = 100`, targets py310-py312 |
| **Ruff** | `line-length = 100`, rules: E, F, I, N, W |
| **MyPy** | `python_version = "3.10"`, `warn_return_any = true` |

### Shell scripts (tools/)

- All tool scripts are Zsh
- Each tool is a self-contained script in its own directory under `tools/`
- Follow existing patterns: structured functions, consistent option parsing, colored output

## Commit Message Convention

Use conventional commits:

```
<type>(<scope>): <subject>
```

**Types**: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

**Examples**:
```
feat(api): Add new authentication endpoint
fix(ui): Resolve button alignment issue
docs(readme): Update installation instructions
```

## Project Principles

These principles **must** be respected in all contributions:

- **Sovereignty** — Users own their data and infrastructure
- **Privacy** — No telemetry, tracking, or external analytics. Never add these.
- **Offline-First** — Core features must work without internet connectivity
- **No Vendor Lock-in** — Never introduce cloud-only functionality or single-provider dependencies

### What is explicitly disallowed

- Adding external analytics or telemetry
- Required internet connectivity for core features
- Vendor lock-in mechanisms
- Cloud-only functionality
- Compromising user privacy

## Repository Structure

```
blackroad/
├── .aria/                  # Aria agent identity configuration
├── .github/
│   ├── workflows/          # 12 CI/CD workflow files
│   ├── CODEOWNERS          # @blackboxprogramming owns all paths
│   ├── dependabot.yml      # Automated dependency updates
│   └── SECURITY.md         # Security policy
├── .trinity/
│   ├── redlight/           # Brand templates & visual identity
│   ├── greenlight/         # Project intelligence & multi-agent coordination
│   ├── yellowlight/        # Infrastructure automation & deployment
│   └── system/             # Trinity system core
├── integrations/
│   ├── platforms.yaml      # Platform definitions (Railway, Vercel, CF, DO, etc.)
│   ├── examples/           # Integration examples
│   └── mobile/             # Mobile tool configs (Warp, Working Copy, etc.)
├── orgs/
│   ├── ai/                 # AI-focused repos (~9)
│   ├── core/               # Core BlackRoad repos (~102)
│   ├── enterprise/         # Enterprise integrations (~8)
│   └── personal/           # Personal projects (~27)
├── packages/
│   └── lucidia-core/       # Python AI reasoning engine package
│       ├── pyproject.toml  # Build config, deps, tool settings
│       ├── physicist.py    # Physics/energy reasoning agent
│       ├── mathematician.py# Symbolic computation agent
│       ├── chemist.py      # Molecular analysis agent
│       ├── geologist.py    # Terrain modeling agent
│       ├── analyst.py      # Data analysis agent
│       ├── architect.py    # System design agent
│       ├── engineer.py     # Structural calculation agent
│       ├── painter.py      # Visual generation agent
│       ├── poet.py         # Creative text agent
│       ├── speaker.py      # Speech/NLP agent
│       └── ...             # Additional modules (quantum, engines, etc.)
├── tools/                  # 30 CLI tools (Zsh scripts)
│   ├── agent-router/       # Routes tasks between AI agents
│   ├── api-tester/         # HTTP client with history
│   ├── backup-manager/     # Backup automation
│   ├── cloudflare/         # Cloudflare integration
│   ├── code-quality/       # Linting/formatting utilities
│   ├── context-radar/      # Smart file suggestions (SQLite)
│   ├── db-client/          # Multi-database connection manager
│   ├── dependency-helper/  # npm/pip/cargo/go dep management
│   ├── deploy-manager/     # Multi-platform deployment
│   ├── docker-manager/     # Container/image management
│   ├── env-manager/        # .env file management with secret masking
│   ├── file-finder/        # Advanced file search with bookmarks
│   ├── git-integration/    # AI-enhanced Git workflows
│   ├── ocean-droplets/     # DigitalOcean integration
│   ├── pair-programming/   # AI pair programming assistant
│   ├── pi-manager/         # Raspberry Pi SSH/SCP deployment
│   ├── security-scanner/   # Security vulnerability scanning
│   ├── smart-search/       # Advanced search with regex
│   ├── snippet-manager/    # Code snippet library
│   ├── test-suite/         # Test runner with coverage
│   ├── web-dev/            # Web development utilities
│   ├── web-monitor/        # Website monitoring
│   └── ...                 # (+ agent-mesh, agent-watch, log-parser, etc.)
├── tests/                  # Test suite (golden tests, etc.)
├── .env.example            # 109 environment variables template
├── .gitignore              # Excludes .env, secrets, keys, IDE files
├── package.json            # Root monorepo config (pnpm + turbo)
├── CONTRIBUTING.md         # Contribution guidelines
├── CODE_OF_CONDUCT.md      # Contributor Covenant v2.0
├── LICENSE                 # Proprietary (BlackRoad OS, Inc.)
└── README.md               # Project overview
```

## Key Files to Know

| File | Purpose |
|------|---------|
| `package.json` | Root monorepo config — pnpm 9, turbo 2 |
| `packages/lucidia-core/pyproject.toml` | Python package config, all linter/formatter settings |
| `.github/workflows/ci.yml` | Main CI pipeline |
| `.github/CODEOWNERS` | All paths owned by `@blackboxprogramming` |
| `.env.example` | Template for all environment variables (109 vars) |
| `CONTRIBUTING.md` | PR process, commit format, coding standards |
| `TRAFFIC_LIGHT_SYSTEM.md` | Status indicators (Green/Yellow/Red/Blue) for repos |
| `integrations/platforms.yaml` | All supported deployment platforms |

## Environment Variables

The `.env.example` file defines 109 variables across these categories:
- Deployment platforms (Railway, Vercel, Cloudflare, DigitalOcean)
- Container registries (Docker Hub, GitHub)
- Tunnel providers (Cloudflare Tunnel, ngrok, Tailscale)
- Productivity (Asana, Notion)
- Auth (Clerk), Payments (Stripe), AI/ML (Hugging Face)
- Edge/IoT (Raspberry Pi), Application (DATABASE_URL, JWT_SECRET, etc.)

**Never commit `.env` files or secrets.** The `.gitignore` excludes `.env*`, `*.pem`, `*.key`, `*secret*`, and `*credential*`.

## Testing

- **Python**: pytest with pytest-cov. Config and deps in `packages/lucidia-core/pyproject.toml`.
- **Golden tests**: `tests/operator.golden` for operator validation.
- CI runs `npm test` (if package.json exists) and can run pytest for Python.

## Traffic Light System

Repos use a status system defined in `TRAFFIC_LIGHT_SYSTEM.md`:
- **Green** — Production ready, all tests passing, docs complete
- **Yellow** — Functional but has known issues or incomplete features
- **Red** — Experimental/broken, not safe for production
- **Blue** — Archived/deprecated

## License

The main repository is **Proprietary** (BlackRoad OS, Inc.). The Lucidia Core subpackage is licensed under **MIT** for public distribution.

## AI Agent Identities

The repo includes two AI agent profiles — reference these for context but do not modify their identity files:
- **Alice** (`ALICE.md`) — Migration Architect & Ecosystem Builder
- **Aria** (`.aria/ARIA_IDENTITY.json`) — Infrastructure Queen, Raspberry Pi ARM64 specialist

## Working with This Repo

1. **Use pnpm** (not npm/yarn) for JS dependency management
2. **Python 3.10+** is required for Lucidia Core
3. **Node.js 20** is the target runtime
4. **Never add telemetry** or tracking of any kind
5. **Follow conventional commits** — `type(scope): subject`
6. **Run linters before committing** — Black, Ruff, MyPy for Python
7. **Keep tools self-contained** — each tool in `tools/` is an independent Zsh script
8. **Respect CODEOWNERS** — all paths require review from `@blackboxprogramming`
