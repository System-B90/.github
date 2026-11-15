[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/import-tree](../index.md) / importConstraints

# Function: importConstraints()

> **importConstraints**(`tx`, `constraints`, `maps`, `now`): `Promise`\<`void`\>

Defined in: [ui/src/api-server/gantt/import-tree.ts:189](https://github.com/System-B90/Bluz/blob/d77dcf130db661461363a52910f62a34b3514ebd/ui/src/api-server/gantt/import-tree.ts#L189)

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
