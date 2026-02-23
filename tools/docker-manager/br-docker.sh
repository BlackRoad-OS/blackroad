#!/usr/bin/env zsh

# Colors
AMBER='[38;5;214m'; PINK='[38;5;205m'; VIOLET='[38;5;135m'; BBLUE='[38;5;69m'
GREEN='[0;32m'; RED='[0;31m'; BOLD='[1m'; DIM='[2m'; NC='[0m'
CYAN="$AMBER"; YELLOW="$PINK"; BLUE="$BBLUE"; MAGENTA="$VIOLET"; PURPLE="$VIOLET"
NC='\033[0m'

DB_FILE="$HOME/.blackroad/docker-manager.db"

init_db() {
    mkdir -p "$(dirname "$DB_FILE")"
    sqlite3 "$DB_FILE" <<EOF
CREATE TABLE IF NOT EXISTS containers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    container_id TEXT UNIQUE,
    name TEXT,
    image TEXT,
    status TEXT,
    ports TEXT,
    created_at INTEGER
);

CREATE TABLE IF NOT EXISTS images (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    image_id TEXT UNIQUE,
    repository TEXT,
    tag TEXT,
    size TEXT,
    created_at INTEGER
);
EOF
}

check_docker() {
    if ! command -v docker &> /dev/null; then
        echo "${RED}❌ Docker not found${NC}"
        echo "Install: https://docs.docker.com/get-docker/"
        exit 1
    fi
}

cmd_ps() {
    check_docker
    init_db
    
    local show_all=false
    [[ "$1" == "-a" || "$1" == "--all" ]] && show_all=true
    
    echo -e "${CYAN}🐳 Docker Containers:${NC}\n"
    
    local cmd="docker ps --format '{{.ID}}|{{.Names}}|{{.Image}}|{{.Status}}|{{.Ports}}'"
    [[ "$show_all" == true ]] && cmd="$cmd -a"
    
    eval "$cmd" | while IFS='|' read -r id name image status ports; do
        if [[ "$status" == *"Up"* ]]; then
            echo -e "${GREEN}●${NC} $name ($id)"
        else
            echo -e "${RED}●${NC} $name ($id)"
        fi
        echo "  Image: $image"
        echo "  Status: $status"
        [[ -n "$ports" ]] && echo "  Ports: $ports"
        echo ""
    done
}

cmd_start() {
    check_docker
    local container="$1"
    
    if [[ -z "$container" ]]; then
        echo -e "${RED}❌ Specify container name or ID${NC}"
        exit 1
    fi
    
    echo -e "${CYAN}🚀 Starting $container...${NC}"
    docker start "$container"
    echo -e "${GREEN}✓ Started${NC}"
}

cmd_stop() {
    check_docker
    local container="$1"
    
    if [[ -z "$container" ]]; then
        echo -e "${RED}❌ Specify container name or ID${NC}"
        exit 1
    fi
    
    echo -e "${CYAN}🛑 Stopping $container...${NC}"
    docker stop "$container"
    echo -e "${GREEN}✓ Stopped${NC}"
}

cmd_logs() {
    check_docker
    local container="$1"
    local lines="${2:-50}"
    
    if [[ -z "$container" ]]; then
        echo -e "${RED}❌ Specify container name or ID${NC}"
        exit 1
    fi
    
    echo -e "${CYAN}📋 Logs for $container:${NC}\n"
    docker logs --tail "$lines" -f "$container"
}

cmd_exec() {
    check_docker
    local container="$1"
    shift
    local command="${@:-/bin/sh}"
    
    if [[ -z "$container" ]]; then
        echo -e "${RED}❌ Specify container name or ID${NC}"
        exit 1
    fi
    
    echo -e "${CYAN}💻 Executing in $container...${NC}"
    docker exec -it "$container" $command
}

cmd_images() {
    check_docker
    init_db
    
    echo -e "${CYAN}🖼️  Docker Images:${NC}\n"
    
    docker images --format '{{.ID}}|{{.Repository}}|{{.Tag}}|{{.Size}}' | while IFS='|' read -r id repo tag size; do
        echo -e "${BLUE}▸${NC} $repo:$tag"
        echo "  ID: $id"
        echo "  Size: $size"
        echo ""
    done
}

cmd_clean() {
    check_docker
    echo -e "${YELLOW}🧹 Cleaning Docker resources...${NC}\n"
    
    echo "Removing stopped containers..."
    docker container prune -f
    
    echo "Removing dangling images..."
    docker image prune -f
    
    echo "Removing unused volumes..."
    docker volume prune -f
    
    echo -e "\n${GREEN}✓ Cleanup complete${NC}"
}

cmd_compose() {
    check_docker
    local action="$1"
    shift
    
    local compose_cmd="docker compose"
    ! docker compose version &> /dev/null 2>&1 && compose_cmd="docker-compose"
    
    case "$action" in
        up)
            echo -e "${CYAN}🚀 Starting compose stack...${NC}"
            $compose_cmd up -d "$@"
            echo -e "${GREEN}✓ Stack started${NC}"
            ;;
        down)
            echo -e "${CYAN}🛑 Stopping compose stack...${NC}"
            $compose_cmd down "$@"
            echo -e "${GREEN}✓ Stack stopped${NC}"
            ;;
        logs)
            $compose_cmd logs -f "$@"
            ;;
        ps)
            echo -e "${CYAN}�� Compose Services:${NC}\n"
            $compose_cmd ps
            ;;
        *)
            echo -e "${RED}❌ Unknown compose action: $action${NC}"
            echo "Use: up, down, logs, ps"
            exit 1
            ;;
    esac
}

cmd_stats() {
    check_docker
    echo -e "${CYAN}📊 Container Stats:${NC}\n"
    docker stats --no-stream
}

cmd_help() {
    echo -e "  ${AMBER}${BOLD}◆ BR DOCKER${NC}  container manager\n"
    echo -e "  ${BOLD}containers${NC}"
    echo -e "  ${AMBER}br docker ps [-a]${NC}               list running"
    echo -e "  ${AMBER}br docker start|stop|restart${NC}    lifecycle"
    echo -e "  ${AMBER}br docker logs <name> [n]${NC}        tail logs"
    echo -e "  ${AMBER}br docker exec <name> [cmd]${NC}      exec in container"
    echo -e "  ${AMBER}br docker stats${NC}                  resource usage\n"
    echo -e "  ${BOLD}images${NC}"
    echo -e "  ${AMBER}br docker images${NC}                 list images"
    echo -e "  ${AMBER}br docker pull <image>${NC}           pull image"
    echo -e "  ${AMBER}br docker build [path]${NC}           build from Dockerfile\n"
    echo -e "  ${BOLD}compose${NC}"
    echo -e "  ${AMBER}br docker compose up|down|ps|logs${NC}\n"
    echo -e "  ${BOLD}maintenance${NC}"
    echo -e "  ${AMBER}br docker clean${NC}                  remove unused"
    echo -e "  ${AMBER}br docker prune${NC}                  ${RED}full cleanup${NC}"
}

# Main dispatch
init_db

case "${1:-help}" in
    ps) cmd_ps "${@:2}" ;;
    start) cmd_start "${@:2}" ;;
    stop) cmd_stop "${@:2}" ;;
    restart) 
        check_docker
        docker restart "${2}"
        echo -e "${GREEN}✓ Restarted${NC}"
        ;;
    logs) cmd_logs "${@:2}" ;;
    exec) cmd_exec "${@:2}" ;;
    images) cmd_images ;;
    pull)
        check_docker
        docker pull "${2}"
        ;;
    build)
        check_docker
        docker build "${@:2}"
        ;;
    compose) cmd_compose "${@:2}" ;;
    stats) cmd_stats ;;
    clean) cmd_clean ;;
    prune)
        check_docker
        echo -e "${YELLOW}⚠️  Full system cleanup${NC}"
        docker system prune -a -f --volumes
        echo -e "${GREEN}✓ Done${NC}"
        ;;
    help|--help|-h) cmd_help ;;
    *)
        echo -e "${RED}❌ Unknown command: $1${NC}"
        cmd_help
        exit 1
        ;;
esac
