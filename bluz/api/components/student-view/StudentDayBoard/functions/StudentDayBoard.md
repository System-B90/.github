[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/student-view/StudentDayBoard](../index.md) / StudentDayBoard

# Function: StudentDayBoard()

> **StudentDayBoard**(`__namedParameters`): `Element`

Defined in: [ui/src/components/student-view/StudentDayBoard.tsx:170](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/components/student-view/StudentDayBoard.tsx#L170)

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

#### refreshSeconds?

`number` = `0`

Refetch interval until the first schedule response names the current
one (staff-set, else `BLUZ_STUDENT_REFRESH_SECONDS`); 0 = off.

## Returns

`Element`
