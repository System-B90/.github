[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/tools/page](../index.md) / PAGE\_PARAMS

# Variable: PAGE\_PARAMS

> `const` **PAGE\_PARAMS**: `object`

Defined in: [ui/src/api-server/ai/tools/page.ts:12](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/ai/tools/page.ts#L12)

Schema fragment every paginated list tool spreads into its properties.

## Type Declaration

### limit

> **limit**: `object`

#### limit.description

> **description**: `string`

#### limit.maximum

> **maximum**: `number` = `MAX_PAGE_SIZE`

#### limit.minimum

> **minimum**: `number` = `1`

#### limit.type

> **type**: `string` = `"integer"`

### offset

> **offset**: `object`

#### offset.description

> **description**: `string` = `"מאיזה פריט להתחיל (לעמוד הבא — הערך nextOffset מהתשובה הקודמת)."`

#### offset.minimum

> **minimum**: `number` = `0`

#### offset.type

> **type**: `string` = `"integer"`
