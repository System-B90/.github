#!/usr/bin/env bash
# Issue a dev TLS leaf cert signed by the System-B90 Dev Root CA.
#
# Usage: issue-cert.sh <name> <common-name> <SAN list> [ca-key] [out-dir]
#   issue-cert.sh madash madash.localhost "DNS:madash.localhost,DNS:localhost,IP:127.0.0.1,IP:::1"
#
# The CA key defaults to ~/.sb90/dev-ca/sb90-dev-root-ca.key (or $SB90_DEV_ROOT_CA_KEY_FILE).
# SANs must fall inside the CA's name constraints (see ca.cnf) or clients reject the cert.
set -euo pipefail

name=${1:?name}
cn=${2:?common name}
san=${3:?SAN list}
ca_key=${4:-${SB90_DEV_ROOT_CA_KEY_FILE:-$HOME/.sb90/dev-ca/sb90-dev-root-ca.key}}
out=${5:-.}
here=$(cd "$(dirname "$0")" && pwd)
ca_crt=$here/sb90-dev-root-ca.crt

mkdir -p "$out"
tmp=$(mktemp -d)
trap 'rm -rf "$tmp"' EXIT

cat > "$tmp/ext" <<EOF
basicConstraints=critical,CA:FALSE
keyUsage=critical,digitalSignature
extendedKeyUsage=serverAuth
subjectAltName=$san
authorityKeyIdentifier=keyid
subjectKeyIdentifier=hash
EOF
# Relative paths + MSYS_NO_PATHCONV: Git Bash would otherwise rewrite the -subj DN into a Windows path.
(
    cd "$tmp"
    openssl ecparam -name prime256v1 -genkey -noout -out key
    MSYS_NO_PATHCONV=1 openssl req -new -key key -subj "/O=System-B90/OU=Development/CN=$cn" -out csr
)
mv "$tmp/key" "$out/$name.key"
openssl x509 -req -in "$tmp/csr" -CA "$ca_crt" -CAkey "$ca_key" -set_serial "0x$(openssl rand -hex 16)" \
    -days 825 -sha256 -extfile "$tmp/ext" -out "$out/$name.crt"
cat "$out/$name.crt" "$ca_crt" > "$out/$name.fullchain.crt"
openssl verify -CAfile "$ca_crt" "$out/$name.crt"
