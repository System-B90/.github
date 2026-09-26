#!/usr/bin/env bash
# One-time root setup on the mks90-laptop WSL host: a dedicated, unprivileged
# account that owns the GitHub runners and the shared Hive, so neither runs as
# a personal user.
#
#   sudo bash host-setup.sh [user]      (default user: hive-ci)
#
# Afterwards, stop the runners running as your own user and start them as the
# new one:  sudo -u hive-ci /actions-runner/run.sh   (and -02, -03), or
# install them as services: cd /actions-runner && sudo ./svc.sh install hive-ci
set -euo pipefail
U="${1:-hive-ci}"

id "$U" >/dev/null 2>&1 || useradd --create-home --shell /bin/bash "$U"
# Docker access. With Docker Desktop's WSL integration the socket is group
# 'docker'; create it if the integration has not.
getent group docker >/dev/null || groupadd docker
usermod -aG docker "$U"

# The runners and their work dirs move to the new account.
chown -R "$U:$U" /actions-runner

# Hostnames the shared Hive and its consumers serve on.
for line in "127.0.0.6 hive.org" "127.0.0.5 peekaboo.dev" "127.0.0.8 madash.dev"; do
  grep -qxF "$line" /etc/hosts || echo "$line" >>/etc/hosts
done
# WSL regenerates /etc/hosts on boot unless told not to.
if ! grep -q '^generateHosts *= *false' /etc/wsl.conf 2>/dev/null; then
  printf '\n[network]\ngenerateHosts = false\n' >>/etc/wsl.conf
fi

# Chromium's system libraries for Playwright. setup-playwright can't install
# them here (no sudo for the runner user), so they are a host prerequisite.
DEBIAN_FRONTEND=noninteractive apt-get install -y -qq libnss3 libnspr4   libatk1.0-0t64 libatk-bridge2.0-0t64 libcups2t64 libdrm2 libxkbcommon0   libxcomposite1 libxdamage1 libxfixes3 libxrandr2 libgbm1 libpango-1.0-0   libcairo2 libasound2t64 libxshmfence1 fonts-liberation

ls -l /var/run/docker.sock
echo "Done. Verify: sudo -u $U docker ps"
