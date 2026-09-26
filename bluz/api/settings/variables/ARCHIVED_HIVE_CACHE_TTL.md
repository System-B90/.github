[**TypeDoc API**](../../index.md)

***

[TypeDoc API](../../index.md) / [settings](../index.md) / ARCHIVED\_HIVE\_CACHE\_TTL

# Variable: ARCHIVED\_HIVE\_CACHE\_TTL

> `const` **ARCHIVED\_HIVE\_CACHE\_TTL**: `number`

Defined in: [ui/src/settings.tsx:31](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/settings.tsx#L31)

A past iteration's Hive data is frozen — its Hive instance is gone or its ids
have been reused, so the response is served from the snapshot taken at
creation. Cache it for a week; a manual "sync Hive info" is the only thing
that can change it, and that only applies to the current iteration.
