[**TypeDoc API**](../../index.md)

***

[TypeDoc API](../../index.md) / [settings](../index.md) / ARCHIVED\_HIVE\_CACHE\_TTL

# Variable: ARCHIVED\_HIVE\_CACHE\_TTL

> `const` **ARCHIVED\_HIVE\_CACHE\_TTL**: `number`

Defined in: [ui/src/settings.tsx:31](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/settings.tsx#L31)

A past iteration's Hive data is frozen — its Hive instance is gone or its ids
have been reused, so the response is served from the snapshot taken at
creation. Cache it for a week; a manual "sync Hive info" is the only thing
that can change it, and that only applies to the current iteration.
