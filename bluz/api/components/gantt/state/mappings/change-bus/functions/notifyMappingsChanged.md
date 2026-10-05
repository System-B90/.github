[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/gantt/state/mappings/change-bus](../index.md) / notifyMappingsChanged

# Function: notifyMappingsChanged()

> **notifyMappingsChanged**(`curriculumId`): `void`

Defined in: [ui/src/components/gantt/state/mappings/change-bus.ts:15](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/components/gantt/state/mappings/change-bus.ts#L15)

Lets a mapping write made *outside* `GanttMappingProvider` (the event
dialog's שבוע/יום picker, which mounts at the curriculum root) tell a
mounted provider to refetch. Without it the רצף זמן tab kept drawing the
old placement until a reload, so a mapping changed from the dialog looked
like it had not taken.

## Parameters

### curriculumId

`string`

The curriculum whose mappings changed.

## Returns

`void`
