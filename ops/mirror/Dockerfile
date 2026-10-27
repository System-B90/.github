# System-B90 offline mirror (System-B90/.github#42). Built from the context
# ops/mirror/build_site.py stages, never from the repo root.
FROM nginx:1.27.5-alpine

# git builds the marketplace repo at start, and git-daemon's git-http-backend
# serves it through fcgiwrap (40-marketplace.sh, nginx.conf). nodejs is only
# for sb90-deploy's post-upgrade health check, which runs `node -e fetch(...)`
# inside the health service.
RUN apk add --no-cache git git-daemon fcgiwrap nodejs

COPY site/ /srv/www/
COPY marketplace/ /srv/marketplace/
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --chmod=755 40-marketplace.sh /docker-entrypoint.d/40-marketplace.sh
