#!/usr/bin/env node
"use strict";

// SessionStart hook: makes `bluz` usable with zero manual setup. If the CLI is
// not on PATH, installs the wheel served by the Bluz instance this plugin came
// from (`instance.json`, written by `bluz plugin install`), else the one at
// $BLUZ_URL, else the org's public pip index. Silent-fails on any error — must
// never block session start.

const { spawnSync } = require("child_process");
const fs = require("fs");
const path = require("path");

const ORG_INDEX_URL = "https://system-b90.github.io/.github/pypi/";

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

function instanceUrl() {
    try {
        const file = path.join(__dirname, "..", "instance.json");
        const { url } = JSON.parse(fs.readFileSync(file, "utf8"));
        if (url) return url.replace(/\/+$/, "");
    } catch {
        // No instance.json — plugin installed from the org marketplace.
    }
    return (process.env.BLUZ_URL || "").replace(/\/+$/, "") || null;
}

async function wheelUrl(base) {
    try {
        const response = await fetch(`${base}/api/cli-dist`);
        if (!response.ok) return null;
        const { wheel } = await response.json();
        return wheel ? `${base}/api/cli-dist/${wheel}` : null;
    } catch {
        return null;
    }
}

async function main() {
    try {
        if (commandExists()) return;

        const pip = findPip();
        if (!pip) return;

        const base = instanceUrl();
        const wheel = base ? await wheelUrl(base) : null;
        const args = wheel
            ? ["install", "--quiet", wheel]
            : ["install", "--quiet", "--extra-index-url", ORG_INDEX_URL, "bluz"];
        spawnSync(pip, args, { stdio: "ignore", timeout: 25000 });
    } catch {
        // Never block session start over an install hiccup.
    }
}

main();
