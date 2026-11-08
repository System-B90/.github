[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/db-iterations](../../../index.md) / [DbIterations](../index.md) / ensure

# Variable: ensure

> `const` **ensure**: () => `Promise`\<`void`\> = `ensureSeeded`

Defined in: [ui/src/api-server/db-iterations.ts:449](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-server/db-iterations.ts#L449)

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
