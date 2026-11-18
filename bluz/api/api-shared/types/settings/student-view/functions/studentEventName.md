[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/settings/student-view](../index.md) / studentEventName

# Function: studentEventName()

> **studentEventName**(`event`, `subjectSymbol`, `settings`): `string`

Defined in: [ui/src/api-shared/types/settings/student-view.ts:111](https://github.com/System-B90/Bluz/blob/04ebae9cb334a01c6e7a55f885993f021e83cd92/ui/src/api-shared/types/settings/student-view.ts#L111)

The name a student sees for an event. A staff-set `studentName` wins in
every mode (#966). Otherwise, in symbol mode the real name is only used for
break/prayer; everything else is built from the type label and the subject
symbol, and degrades to the label (or a generic word) rather than falling
back to the real name. Words students must never see are scrubbed from
every result, the staff override included.

## Parameters

### event

#### name

`string`

#### studentName?

`string`

#### type

[`EventType`](../../../event/enumerations/EventType.md)

### subjectSymbol

`string` \| `null` \| `undefined`

### settings

[`StudentViewSettings`](../type-aliases/StudentViewSettings.md)

## Returns

`string`
