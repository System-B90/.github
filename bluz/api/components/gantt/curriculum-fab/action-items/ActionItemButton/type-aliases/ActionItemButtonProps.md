[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/gantt/curriculum-fab/action-items/ActionItemButton](../index.md) / ActionItemButtonProps

# Type Alias: ActionItemButtonProps

> **ActionItemButtonProps** = `object` & `Omit`\<`IconButtonProps`, `"onClick"` \| `"size"` \| `"sx"`\>

Defined in: [ui/src/components/gantt/curriculum-fab/action-items/ActionItemButton.tsx:10](https://github.com/System-B90/Bluz/blob/29b32f987e27f991aca78ed635c3b34fa6d4c458/ui/src/components/gantt/curriculum-fab/action-items/ActionItemButton.tsx#L10)

## Type Declaration

### command?

> `optional` **command?**: `Pick`\<`Command`, `"id"` \| `"keywords"` \| `"subtitle"`\>

Mirror this button in the command palette. Title, icon, enabled state
and handler all come from the button itself.

### loading?

> `optional` **loading?**: `boolean`

### onClick?

> `optional` **onClick?**: (`event?`) => `void`

#### Parameters

##### event?

`MouseEvent`\<`HTMLButtonElement`\>

#### Returns

`void`

### startIcon?

> `optional` **startIcon?**: `React.ReactNode`

### tooltipTitle

> **tooltipTitle**: `string`
