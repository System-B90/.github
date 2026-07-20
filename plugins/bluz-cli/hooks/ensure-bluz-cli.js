#!/usr/bin/env node
"use strict";

// SessionStart hook: makes `bluz` usable with zero manual setup, without
// needing any Bluz source checkout. Checks whether the CLI is on PATH; if
// not, installs it from the org's public pip index (System-B90/.github,
// PEP 503 static index served over GitHub Pages — no auth required, same
// pattern as pyhive). raw.githubusercontent.com does NOT work here: it has
// no directory-index fallback, so pip's request for the bare package
// directory 404s. Silent-fails on any error — must never block session
// start.

const { spawnSync } = require("child_process");

const INDEX_URL = "https://system-b90.github.io/.github/pypi/";

function commandExists() {
    const probe = spawnSync("bluz", ["--version"], { stdio: "ignore" });
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
        if (commandExists()) return;

        const pip = findPip();
        if (!pip) return;

        spawnSync(
            pip,
            ["install", "--quiet", "--index-url", INDEX_URL, "bluz-cli"],
            { stdio: "ignore", timeout: 25000 },
        );
    } catch {
        // Never block session start over an install hiccup.
    }
}

main();
