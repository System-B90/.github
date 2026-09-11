[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-iterations](../../../index.md) / [DbIterations](../index.md) / ensure

# Variable: ensure

> `const` **ensure**: () => `Promise`\<`void`\> = `ensureSeeded`

Defined in: [ui/src/api-server/db-iterations.ts:372](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/db-iterations.ts#L372)

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
