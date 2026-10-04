[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/import-tree](../index.md) / importConstraints

# Function: importConstraints()

> **importConstraints**(`tx`, `constraints`, `maps`, `now`): `Promise`\<`void`\>

Defined in: [ui/src/api-server/gantt/import-tree.ts:182](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-server/gantt/import-tree.ts#L182)

Re-creates `constraints` against the ids in `maps`. A constraint whose owner
was not imported is dropped; a target outside the import is cleared.

## Parameters

### tx

`PgTransaction`

### constraints

`unknown`

### maps

[`ImportIdMaps`](../type-aliases/ImportIdMaps.md)

### now

`Date`

## Returns

`Promise`\<`void`\>
