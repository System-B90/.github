[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/event](../index.md) / lecturersLabelForType

# Function: lecturersLabelForType()

> **lecturersLabelForType**(`type`): `string`

Defined in: [ui/src/api-shared/types/event.ts:203](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/api-shared/types/event.ts#L203)

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
