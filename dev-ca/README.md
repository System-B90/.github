# System-B90 Dev Root CA

Root CA for **development only**. Every System-B90 project's nginx ships a default cert signed
by it. Trust this root once and `https://bluz.dev`, `https://madash.dev`,
`https://peekaboo.dev`, `https://samkasotron.localhost`, etc. load without warnings.

| Field | Value |
|---|---|
| Subject | `CN=System-B90 Dev Root CA, OU=Development, O=System-B90` |
| Key | ECDSA P-384, SHA-384 |
| Valid until | 2036-09-24 |
| SHA-256 fingerprint | `E1:FC:FC:02:58:B1:04:6D:37:56:B0:3B:04:76:B1:36:2A:39:16:12:FD:36:B7:92:36:DA:C1:1A:6D:DF:65:4D` |

> **2026-09-28: root re-issued** to permit `*.dev` (was `bluz.dev` only). Same key and subject,
> so already-issued leaf certs keep verifying. If you trusted the previous root
> (fingerprint `E3:AE:39:EC:…:0E:B0`), remove it and trust this one, or the madash and
> peek-a-boo certs are rejected.

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

## What trusting it allows

The CA carries a critical **name constraint**. Clients reject any cert it signs outside:

- DNS: `localhost`, `*.localhost`, `*.test`, `*.internal`, `*.local`, `*.dev`
- IP: `127.0.0.0/8`, `::1`, `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`

`pathlen:0` blocks intermediate CAs. **`.dev` is a public TLD**: whoever holds the CA key, or
can run the *Issue dev TLS cert* workflow, can mint certs that machines trusting this root
accept for *any* `*.dev` site (e.g. `web.dev`). Keep the key and the workflow's write access
tight. The other names are reserved or private and cannot be public sites.

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
| madash | `madash.dev` | `madash.dev`, `*.madash.dev`, `madash.localhost`, `localhost`, `127.0.0.1`, `127.0.0.8`, `::1` | `nginx/ssl-default/` |
| peek-a-boo | `peekaboo.dev` | `peekaboo.dev`, `*.peekaboo.dev`, `peekaboo.test`, `peekaboo.localhost`, `localhost`, `127.0.0.1`, `127.0.0.4`, `127.0.0.5`, `::1` | `nginx/ssl-default/` |

Hive (`pyhive/hive-stack`) keeps its own self-signed cert.

## Where the CA key lives

- `SB90_DEV_ROOT_CA_KEY` Actions secret on `System-B90/.github` (used by the workflow).
- Offline backup with the maintainer (`~/.sb90/dev-ca/`).

It is never committed. To change the constraints only, re-sign with the **existing** key (the
secret stays valid and issued leaves keep verifying):

```bash
openssl req -x509 -new -key ~/.sb90/dev-ca/sb90-dev-root-ca.key -sha384 -days 3650 -config dev-ca/ca.cnf -out dev-ca/sb90-dev-root-ca.crt
```

`ca.cnf` here is the config it was generated with — reuse it to rotate the key:

```bash
openssl ecparam -name secp384r1 -genkey -noout -out sb90-dev-root-ca.key
openssl req -x509 -new -key sb90-dev-root-ca.key -sha384 -days 3650 -config dev-ca/ca.cnf -out dev-ca/sb90-dev-root-ca.crt
gh secret set SB90_DEV_ROOT_CA_KEY -R System-B90/.github < sb90-dev-root-ca.key
```
