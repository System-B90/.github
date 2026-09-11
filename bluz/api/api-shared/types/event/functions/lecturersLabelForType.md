[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/event](../index.md) / lecturersLabelForType

# Function: lecturersLabelForType()

> **lecturersLabelForType**(`type`): `string`

Defined in: [ui/src/api-shared/types/event.ts:198](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-shared/types/event.ts#L198)

The display label for the `lecturers` field of a given event type:
workshops (סדנה) have "מנהלים" while lectures have "מרצים". The selection
source (instructors and outsiders) is identical.

## Parameters

### type

[`EventType`](../enumerations/EventType.md)

The EventType whose label is needed.

## Returns

`string`

The Hebrew field label.
