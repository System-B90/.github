#!/bin/sh
# Runs from the nginx image's /docker-entrypoint.d before nginx starts.
#
# Builds the plugin marketplace as a git repo and starts fcgiwrap, through which
# nginx serves it with git-http-backend (smart HTTP). `/plugin marketplace add`
# makes a shallow clone, which the static "dumb" protocol can't serve. Built
# here rather than in the image so the plugins' hooks can point at this
# mirror's own pip index: they hard-code the GitHub Pages URL, and a git pack
# can't be rewritten on the fly the way nginx rewrites the HTML (nginx.conf).
set -eu

src=/srv/marketplace
repo=/srv/git/marketplace.git
pages=https://system-b90.github.io/.github
url="${MIRROR_URL:?MIRROR_URL is not set - run python3 bootstrap.py setup}"
url="${url%/}"

work=$(mktemp -d)
cp -a "$src/." "$work/"
grep -rlF "$pages" "$work" | while IFS= read -r file; do
  sed -i "s#$pages#$url#g" "$file"
done

git -C "$work" init -q -b main
git -C "$work" add -A
# Fixed dates: the commit (and what `/plugin marketplace update` sees) changes
# only when the plugins or the mirror's address do, not on every restart.
GIT_AUTHOR_DATE=2000-01-01T00:00:00Z GIT_COMMITTER_DATE=2000-01-01T00:00:00Z \
  git -C "$work" -c user.name="System-B90 mirror" -c user.email=mirror@localhost \
  commit -q -m "System-B90 marketplace via $url"

rm -rf "$repo"
git clone -q --bare "$work" "$repo"
rm -rf "$work"
# git-http-backend runs as nginx and refuses a repo another user owns.
chown -R nginx:nginx "$repo"

# A restarted container keeps /run, and fcgiwrap won't bind over the old socket.
mkdir -p /run/fcgiwrap
rm -f /run/fcgiwrap/fcgiwrap.sock
chown nginx:nginx /run/fcgiwrap
su -s /bin/sh nginx -c 'fcgiwrap -s unix:/run/fcgiwrap/fcgiwrap.sock </dev/null >/dev/null 2>&1 &'
echo "40-marketplace.sh: marketplace served at $url/marketplace.git"
