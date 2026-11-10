[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/gantt/event-dialog/EventShuffleGroupField](../index.md) / describeGroupChange

# Function: describeGroupChange()

> **describeGroupChange**(`current`, `selected`, `memberCount`): \{ `destructive`: `boolean`; `text`: `string`; \} \| `null`

Defined in: [ui/src/components/gantt/event-dialog/EventShuffleGroupField.tsx:52](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/gantt/event-dialog/EventShuffleGroupField.tsx#L52)

What applying `selected` does to the group, in the server's terms (see
`applyShuffleGroup`): fewer than two names only drops the group marker and
keeps every event, while a group of two or more deletes the members whose
shuffle was deselected. Null when there is nothing worth warning about.

## Parameters

### current

`Set`\<`string`\>

### selected

`Set`\<`string`\>

### memberCount

`number`

## Returns

\{ `destructive`: `boolean`; `text`: `string`; \} \| `null`
