# System-B90 Dev Root CA

Root CA for **development only**. Every System-B90 project's nginx ships a default cert signed
by it. Trust this root once and `https://bluz.dev`, `https://samkasotron.localhost`, etc. load
without warnings.

| Field | Value |
|---|---|
| Subject | `CN=System-B90 Dev Root CA, OU=Development, O=System-B90` |
| Key | ECDSA P-384, SHA-384 |
| Valid until | 2036-09-23 |
| SHA-256 fingerprint | `E3:AE:39:EC:FA:6C:84:03:77:37:48:1A:6F:13:B6:A9:E8:F6:13:91:04:68:72:F5:7A:36:FF:9C:9C:3F:0E:B0` |

## Quick Start

Download and check the fingerprint against the table above:

```powershell
curl.exe -fLo sb90-dev-root-ca.crt https://raw.githubusercontent.com/System-B90/.github/main/dev-ca/sb90-dev-root-ca.crt
certutil -hashfile sb90-dev-root-ca.crt SHA256
```

Trust it:

```powershell
# Windows (current user, no admin). Chrome/Edge use this store.
certutil -user -addstore Root sb90-dev-root-ca.crt
```

```bash
# Debian/Ubuntu
sudo cp sb90-dev-root-ca.crt /usr/local/share/ca-certificates/sb90-dev-root-ca.crt && sudo update-ca-certificates
# macOS
sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain sb90-dev-root-ca.crt
```

Firefox has its own store: Settings → Certificates → View Certificates → Authorities → Import.
Node ignores the OS store: set `NODE_EXTRA_CA_CERTS=/path/to/sb90-dev-root-ca.crt`.
Python `requests` likewise: set `REQUESTS_CA_BUNDLE` (or `SSL_CERT_FILE`) to a bundle that includes it.

Remove it:

```powershell
certutil -user -delstore Root "System-B90 Dev Root CA"
```

## Why trusting it is low-risk

The CA carries a critical **name constraint**. Clients reject any cert it signs outside:

- DNS: `localhost`, `*.localhost`, `*.test`, `*.internal`, `*.local`, `bluz.dev`, `*.bluz.dev`
- IP: `127.0.0.0/8`, `::1`, `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`

Even a leaked CA key cannot impersonate a public site. `pathlen:0` blocks intermediate CAs.

The default leaf keys committed to project repos are **public**. They are dev-only. Never put
them in front of real traffic; production deploys supply their own certs.

## Issuing a cert for a project

Pick names inside the constraints above — `<project>.localhost` is the default choice.

**Via GitHub Actions** (no key on your machine): run **Issue dev TLS cert** in this repo's
Actions tab, then download the `dev-cert-<name>` artifact (kept 1 day).

```powershell
gh workflow run issue-dev-cert.yml -R System-B90/.github -f name=madash -f common_name=madash.localhost -f san="DNS:madash.localhost,DNS:localhost,IP:127.0.0.1,IP:::1"
gh run download -R System-B90/.github -n dev-cert-madash
```

**Locally** (needs the CA key at `~/.sb90/dev-ca/sb90-dev-root-ca.key`):

```bash
bash dev-ca/issue-cert.sh madash madash.localhost "DNS:madash.localhost,DNS:localhost,IP:127.0.0.1,IP:::1" "" out/
```

Output: `<name>.key`, `<name>.crt`, `<name>.fullchain.crt` (leaf + root). Point nginx
`ssl_certificate` at the fullchain file.

## Issued certs

| Project | CN | SANs | Repo path |
|---|---|---|---|
| Bluz | `bluz.dev` | `bluz.dev`, `*.bluz.dev`, `bluz.localhost`, `localhost`, `127.0.0.1`, `127.0.0.3`, `::1` | `nginx/ssl-default/` |
| Samkasotron | `samkasotron.localhost` | `samkasotron.localhost`, `localhost`, `127.0.0.1`, `::1` | `certs-default/` |

Hive (`pyhive/hive-stack`) keeps its own self-signed cert. madash and peek-a-boo: tracked in
their repos' issues.

## Where the CA key lives

- `SB90_DEV_ROOT_CA_KEY` Actions secret on `System-B90/.github` (used by the workflow).
- Offline backup with the maintainer (`~/.sb90/dev-ca/`).

It is never committed. `ca.cnf` here is the config it was generated with — reuse it to rotate:

```bash
openssl ecparam -name secp384r1 -genkey -noout -out sb90-dev-root-ca.key
openssl req -x509 -new -key sb90-dev-root-ca.key -sha384 -days 3650 -config dev-ca/ca.cnf -out dev-ca/sb90-dev-root-ca.crt
gh secret set SB90_DEV_ROOT_CA_KEY -R System-B90/.github < sb90-dev-root-ca.key
```
