[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/settings/student-view](../index.md) / studentEventName

# Function: studentEventName()

> **studentEventName**(`event`, `subjectSymbol`, `settings`): `string`

Defined in: [ui/src/api-shared/types/settings/student-view.ts:84](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/api-shared/types/settings/student-view.ts#L84)

The name a student sees for an event. A staff-set `studentName` wins in
every mode (#966). Otherwise, in symbol mode the real name is only used for
break/prayer; everything else is built from the type label and the subject
symbol, and degrades to the label (or a generic word) rather than falling
back to the real name.

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
