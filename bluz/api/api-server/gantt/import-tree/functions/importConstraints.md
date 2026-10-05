[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/import-tree](../index.md) / importConstraints

# Function: importConstraints()

> **importConstraints**(`tx`, `constraints`, `maps`, `now`): `Promise`\<`void`\>

Defined in: [ui/src/api-server/gantt/import-tree.ts:182](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/gantt/import-tree.ts#L182)

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
