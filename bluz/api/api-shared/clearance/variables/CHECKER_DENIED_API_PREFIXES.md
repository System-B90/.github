[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/clearance](../index.md) / CHECKER\_DENIED\_API\_PREFIXES

# Variable: CHECKER\_DENIED\_API\_PREFIXES

> `const` **CHECKER\_DENIED\_API\_PREFIXES**: `ReadonlyArray`\<`string`\>

Defined in: [ui/src/api-shared/clearance.ts:41](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/clearance.ts#L41)

API prefixes a Checker may not reach even for reads: the gantt, minting
credentials, AI (its tools act as the caller), per-user integrations, the
CLI handshake and the student board (which a Checker is not part of).
