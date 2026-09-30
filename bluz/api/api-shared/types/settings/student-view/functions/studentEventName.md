[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/settings/student-view](../index.md) / studentEventName

# Function: studentEventName()

> **studentEventName**(`event`, `subjectSymbol`, `settings`): `string`

Defined in: [ui/src/api-shared/types/settings/student-view.ts:81](https://github.com/System-B90/Bluz/blob/56c5d2ae92c3656a1c138795785f74f52c53a737/ui/src/api-shared/types/settings/student-view.ts#L81)

The name a student sees for an event. In symbol mode the real name is only
used for break/prayer; everything else is built from the type label and the
subject symbol, and degrades to the label (or a generic word) rather than
falling back to the real name.

## Parameters

### event

#### name

`string`

#### type

[`EventType`](../../../event/enumerations/EventType.md)

### subjectSymbol

`string` \| `null` \| `undefined`

### settings

[`StudentViewSettings`](../type-aliases/StudentViewSettings.md)

## Returns

`string`
