[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/event-dialog/utils](../index.md) / hasUnsavedChanges

# Function: hasUnsavedChanges()

> **hasUnsavedChanges**(`initial`, `current`): `boolean`

Defined in: [ui/src/components/schedule/event-dialog/utils.ts:47](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/components/schedule/event-dialog/utils.ts#L47)

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
