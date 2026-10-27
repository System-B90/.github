#!/usr/bin/env node
"use strict";

// SessionStart hook: makes `pyhive` usable with zero manual setup. Installs
// PyHiveLMS from the org's public pip index (System-B90/.github, PEP 503
// static index served over GitHub Pages — no auth required) when the CLI is
// missing, or too old to have `pyhive docs`, which the skill relies on.
// Silent-fails on any error — must never block session start.
//
// --extra-index-url, not --index-url: the org index hosts only org packages,
// so PyHive's own dependencies (httpx, pydantic, typer, ...) come from PyPI.
// PyPI's PyHiveLMS stops at an old release, so pip still picks the org's.

const { spawnSync } = require("child_process");

const INDEX_URL = "https://system-b90.github.io/.github/pypi/";

function upToDate() {
    const probe = spawnSync("pyhive", ["docs", "path"], { stdio: "ignore" });
    return probe.status === 0;
}

function findPip() {
    for (const candidate of ["pip", "pip3"]) {
        const probe = spawnSync(candidate, ["--version"], { stdio: "ignore" });
        if (probe.status === 0) return candidate;
    }
    return null;
}

function main() {
    try {
        if (upToDate()) return;

        const pip = findPip();
        if (!pip) return;

        spawnSync(
            pip,
            ["install", "--quiet", "--upgrade", "--extra-index-url", INDEX_URL, "PyHiveLMS"],
            { stdio: "ignore", timeout: 25000 },
        );
    } catch {
        // Never block session start over an install hiccup.
    }
}

main();
