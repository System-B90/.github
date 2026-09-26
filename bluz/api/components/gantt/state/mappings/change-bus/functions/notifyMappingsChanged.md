[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/gantt/state/mappings/change-bus](../index.md) / notifyMappingsChanged

# Function: notifyMappingsChanged()

> **notifyMappingsChanged**(`curriculumId`): `void`

Defined in: [ui/src/components/gantt/state/mappings/change-bus.ts:15](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/gantt/state/mappings/change-bus.ts#L15)

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
