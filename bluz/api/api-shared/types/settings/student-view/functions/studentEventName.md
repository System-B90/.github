[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/settings/student-view](../index.md) / studentEventName

# Function: studentEventName()

> **studentEventName**(`event`, `subjectSymbol`, `settings`): `string`

Defined in: [ui/src/api-shared/types/settings/student-view.ts:109](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-shared/types/settings/student-view.ts#L109)

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
