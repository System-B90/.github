[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-iterations](../../../index.md) / [DbIterations](../index.md) / ensure

# Variable: ensure

> `const` **ensure**: () => `Promise`\<`void`\> = `ensureSeeded`

Defined in: [ui/src/api-server/db-iterations.ts:374](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/db-iterations.ts#L374)

One-off migration for installs that predate the registry: the existing `bluz`
database is registered as the first, current iteration so its data stays
reachable. No documents are moved.

A *fresh* install is deliberately left with an empty registry (#471) — an
auto-created "current" iteration has no real name or id, and its literal id
collided with the `/api/iterations/current` route segment (#472). The UI
prompts for a real iteration instead.

Uses upsert to avoid a TOCTOU race on concurrent cold starts.

## Returns

`Promise`\<`void`\>
