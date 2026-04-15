#!/usr/bin/env bash
# docker-safe — whitelist wrapper around docker CLI used by claude-mao.
# Allows read-only inspection commands and in-container package installs,
# blocks destructive host/container ops. Log every invocation.

set -euo pipefail
LOG=/home/mao/docker-safe.log
TS=$(date -Iseconds)
ARGS=("$@")

log() { echo "$TS pid=$$ $*" >> "$LOG"; }

deny() {
  log "DENY $*"
  echo "docker-safe: blocked: $*" >&2
  exit 126
}

allow() {
  log "ALLOW ${ARGS[*]}"
  exec /usr/bin/docker "${ARGS[@]}"
}

if [[ ${#ARGS[@]} -eq 0 ]]; then deny "no args"; fi
CMD="${ARGS[0]}"

case "$CMD" in
  ps|images|inspect|logs|top|stats|version|info|network|volume|port|events)
    # read-only or inspection; allow subcommand variants
    allow
    ;;
  exec)
    # allow exec only for safe in-container package/file ops
    # Pattern: docker exec [-flags] <container> <cmd...>
    # Find first non-flag arg as container name, then inspect the inner command
    i=1
    while [[ $i -lt ${#ARGS[@]} && "${ARGS[$i]}" == -* ]]; do i=$((i+1)); done
    CONTAINER="${ARGS[$i]:-}"
    i=$((i+1))
    INNER="${ARGS[$i]:-}"
    case "$INNER" in
      apt|apt-get|dpkg|yum|dnf|apk|pip|pip3|npm|npx|yarn|pnpm|git|node|python|python3|bash|sh|ls|cat|grep|find|tee|echo|mkdir|cp|mv|test|true|false|which|whereis|curl|wget|head|tail|sed|awk|sort|uniq|wc|jq|env|printenv|df|du|uname|hostname|id|whoami|ps|top|htop|free|uptime|date|systemctl|service)
        # allow, but deny obvious foot-guns in the tail
        for a in "${ARGS[@]:$((i+1))}"; do
          case "$a" in
            "--force-yes"|"-rf"|"-fr"|"-Rf"|"-fR"|"/"|"/*")
              deny "dangerous_flag $a in exec $CONTAINER $INNER"
              ;;
          esac
        done
        allow
        ;;
      *) deny "unsafe_exec_inner '$INNER' in container $CONTAINER" ;;
    esac
    ;;
  restart)
    # allow restart of SELF-OWNED containers only (prefix allowlist)
    TARGET="${ARGS[1]:-}"
    case "$TARGET" in
      openclaw-kfgm-*|claude-mao|paperclip-1jd6-*|n8n-solq-*)
        allow ;;
      *) deny "restart_not_in_allowlist $TARGET" ;;
    esac
    ;;
  *)
    deny "subcommand_not_whitelisted $CMD"
    ;;
esac
