[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/student-view/StudentDayBoard](../index.md) / StudentDayBoard

# Function: StudentDayBoard()

> **StudentDayBoard**(`__namedParameters`): `Element`

Defined in: [ui/src/components/student-view/StudentDayBoard.tsx:90](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/student-view/StudentDayBoard.tsx#L90)

The student-facing schedule board (#656).

Deliberately self-contained: it mounts none of the calendar's providers,
dialogs, context menus or the app bar, so there is no staff surface in the
tree for a student to reach — and nothing on screen implies the rest of the
app exists. It renders exactly the fields `StudentEvent` carries, and the
server guarantees it can carry no others.

## Parameters

### \_\_namedParameters

#### date?

`string`

## Returns

`Element`
