[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/gantt/state/mappings/change-bus](../index.md) / notifyMappingsChanged

# Function: notifyMappingsChanged()

> **notifyMappingsChanged**(`curriculumId`): `void`

Defined in: [ui/src/components/gantt/state/mappings/change-bus.ts:15](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/components/gantt/state/mappings/change-bus.ts#L15)

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
