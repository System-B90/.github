[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/clearance](../index.md) / CHECKER\_DENIED\_API\_PREFIXES

# Variable: CHECKER\_DENIED\_API\_PREFIXES

> `const` **CHECKER\_DENIED\_API\_PREFIXES**: `ReadonlyArray`\<`string`\>

Defined in: [ui/src/api-shared/clearance.ts:42](https://github.com/System-B90/Bluz/blob/04ebae9cb334a01c6e7a55f885993f021e83cd92/ui/src/api-shared/clearance.ts#L42)

API prefixes a Checker may not reach even for reads: the gantt, minting
credentials, AI (its tools act as the caller), per-user integrations, the
CLI handshake, the student board (which a Checker is not part of) and the
student monitor (who watched how long, and who probed what).
