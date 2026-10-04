[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/db-base](../index.md) / DrizzleOperationsBuilderProps

# Type Alias: DrizzleOperationsBuilderProps\<TTable\>

> **DrizzleOperationsBuilderProps**\<`TTable`\> = `object`

Defined in: [ui/src/api-server/gantt/db-base.ts:218](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-server/gantt/db-base.ts#L218)

## Type Parameters

### TTable

`TTable` *extends* `PgTableWithColumns`\<`any`\>

## Properties

### idPrefix

> **idPrefix**: `"c"` \| `"d"` \| `"e"` \| `"m"` \| `"s"` \| `"w"`

Defined in: [ui/src/api-server/gantt/db-base.ts:225](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-server/gantt/db-base.ts#L225)

***

### junction?

> `optional` **junction?**: [`JunctionConfig`](JunctionConfig.md)[] \| [`JunctionConfig`](JunctionConfig.md)

Defined in: [ui/src/api-server/gantt/db-base.ts:223](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-server/gantt/db-base.ts#L223)

***

### labelColumn?

> `optional` **labelColumn?**: `AnyPgColumn`

Defined in: [ui/src/api-server/gantt/db-base.ts:228](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-server/gantt/db-base.ts#L228)

***

### parentJunction?

> `optional` **parentJunction?**: [`ParentJunctionConfig`](ParentJunctionConfig.md)

Defined in: [ui/src/api-server/gantt/db-base.ts:224](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-server/gantt/db-base.ts#L224)

***

### table

> **table**: `TTable`

Defined in: [ui/src/api-server/gantt/db-base.ts:221](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-server/gantt/db-base.ts#L221)

***

### typeName

> **typeName**: `string`

Defined in: [ui/src/api-server/gantt/db-base.ts:222](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/api-server/gantt/db-base.ts#L222)
