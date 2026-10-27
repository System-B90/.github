"""
Name: setup.py
Purpose: Interactive wizard that writes the System-B90 mirror's .env and
    issues its TLS certificate.
Created: 2026-10-27
Author: Michael K. Steinberg

Runs from the bundle root (./install.sh runs it; re-run with
`python3 bootstrap.py setup`). The questions themselves live in sb90-deploy.
"""

import sys
from pathlib import Path

try:
    from sb90_deploy.spec import AppSpec
    from sb90_deploy.wizard import Wizard
except ImportError:
    print(
        "Error: sb90-deploy is not installed. In a release bundle, run ./install.sh.",
        file=sys.stderr,
    )
    sys.exit(1)


def main() -> None:
    w = Wizard(AppSpec.load(str(Path(__file__).resolve().parent / "app.json")))
    domain = w.domain(example="mirror.school.internal")
    w.ports()
    # nginx reads /etc/nginx/ssl/{cert,key}.pem and serves ca.crt, mounted from ./ssl.
    w.tls(domain, ssl_dir="ssl", cert_name="cert.pem", key_name="key.pem")
    # w.domain also writes NEXTAUTH_URL, which nothing here reads. w.url is the
    # same address; the marketplace's plugin hooks are pointed at it.
    w.set("MIRROR_URL", w.url)
    w.write()


if __name__ == "__main__":
    main()
