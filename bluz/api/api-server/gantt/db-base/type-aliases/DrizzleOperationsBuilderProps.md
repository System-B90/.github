[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/db-base](../index.md) / DrizzleOperationsBuilderProps

# Type Alias: DrizzleOperationsBuilderProps\<TTable\>

> **DrizzleOperationsBuilderProps**\<`TTable`\> = `object`

Defined in: [ui/src/api-server/gantt/db-base.ts:214](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/gantt/db-base.ts#L214)

## Type Parameters

### TTable

`TTable` *extends* `PgTableWithColumns`\<`any`\>

## Properties

### idPrefix

> **idPrefix**: `"c"` \| `"d"` \| `"e"` \| `"m"` \| `"s"` \| `"w"`

Defined in: [ui/src/api-server/gantt/db-base.ts:221](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/gantt/db-base.ts#L221)

***

### junction?

> `optional` **junction?**: [`JunctionConfig`](JunctionConfig.md)[] \| [`JunctionConfig`](JunctionConfig.md)

Defined in: [ui/src/api-server/gantt/db-base.ts:219](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/gantt/db-base.ts#L219)

***

### labelColumn?

> `optional` **labelColumn?**: `AnyPgColumn`

Defined in: [ui/src/api-server/gantt/db-base.ts:224](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/gantt/db-base.ts#L224)

***

### parentJunction?

> `optional` **parentJunction?**: [`ParentJunctionConfig`](ParentJunctionConfig.md)

Defined in: [ui/src/api-server/gantt/db-base.ts:220](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/gantt/db-base.ts#L220)

***

### table

> **table**: `TTable`

Defined in: [ui/src/api-server/gantt/db-base.ts:217](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/gantt/db-base.ts#L217)

***

### typeName

> **typeName**: `string`

Defined in: [ui/src/api-server/gantt/db-base.ts:218](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/gantt/db-base.ts#L218)
