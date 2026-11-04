[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/import-tree](../index.md) / importConstraints

# Function: importConstraints()

> **importConstraints**(`tx`, `constraints`, `maps`, `now`): `Promise`\<`void`\>

Defined in: [ui/src/api-server/gantt/import-tree.ts:189](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-server/gantt/import-tree.ts#L189)

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
