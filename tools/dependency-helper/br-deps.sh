#!/bin/zsh
# BR Deps - Dependency Helper
AMBER='[38;5;214m'; PINK='[38;5;205m'; VIOLET='[38;5;135m'; BBLUE='[38;5;69m'
GREEN='[0;32m'; RED='[0;31m'; BOLD='[1m'; DIM='[2m'; NC='[0m'
CYAN="$AMBER"; YELLOW="$PINK"; BLUE="$BBLUE"; MAGENTA="$VIOLET"; PURPLE="$VIOLET"

check_node() {
    [[ ! -f "package.json" ]] && return
    echo -e "${CYAN}📦 Checking Node dependencies...${NC}\n"
    if command -v npm &>/dev/null; then
        npm outdated || echo -e "${GREEN}✓ All dependencies up to date${NC}"
    fi
}

check_python() {
    [[ ! -f "requirements.txt" ]] && return
    echo -e "${CYAN}🐍 Checking Python dependencies...${NC}\n"
    if command -v pip &>/dev/null; then
        pip list --outdated || echo -e "${GREEN}✓ All dependencies up to date${NC}"
    fi
}

check_go() {
    [[ ! -f "go.mod" ]] && return
    echo -e "${CYAN}🐹 Checking Go dependencies...${NC}\n"
    go list -u -m all 2>/dev/null || echo -e "${GREEN}✓ Dependencies OK${NC}"
}

audit_security() {
    echo -e "${RED}🔒 Security Audit:${NC}\n"
    [[ -f "package.json" ]] && npm audit 2>/dev/null
    [[ -f "Cargo.toml" ]] && cargo audit 2>/dev/null
    [[ -f "requirements.txt" ]] && pip check 2>/dev/null
}

case ${1:-check} in
    check|c) check_node; check_python; check_go ;;
    audit|a) audit_security ;;
    *) check_node; check_python; check_go ;;
esac
