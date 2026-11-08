[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/event-dialog/utils](../index.md) / hasUnsavedChanges

# Function: hasUnsavedChanges()

> **hasUnsavedChanges**(`initial`, `current`): `boolean`

Defined in: [ui/src/components/schedule/event-dialog/utils.ts:47](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/schedule/event-dialog/utils.ts#L47)

Whether the form differs from what the dialog opened with. Blank values
(undefined, null, "", []) count as equal, so a field that only normalises
an empty value doesn't make an untouched form look edited.

## Parameters

### initial

`Partial`\<[`Event`](../../../../../api-shared/types/event/type-aliases/Event.md)\>

### current

`Partial`\<[`Event`](../../../../../api-shared/types/event/type-aliases/Event.md)\>

## Returns

`boolean`
