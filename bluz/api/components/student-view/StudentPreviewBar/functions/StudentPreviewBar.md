[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/student-view/StudentPreviewBar](../index.md) / StudentPreviewBar

# Function: StudentPreviewBar()

> **StudentPreviewBar**(`__namedParameters`): `Element`

Defined in: [ui/src/components/student-view/StudentPreviewBar.tsx:41](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/components/student-view/StudentPreviewBar.tsx#L41)

Staff-only banner over the student view: says plainly that this is a
preview, offers a way back, lets staff step to another day, and can push an
update that reloads every open student board (this preview included), and
sets how often the boards refresh on their own — they do not follow edits
live, so this interval is how staff changes reach students.

Rendered only when the *server* has confirmed Segel/Admin clearance — see
the page component. It is not a client-side gate.

## Parameters

### \_\_namedParameters

#### date?

`string`

#### defaultRefreshSeconds

`number`

The deployment default (`BLUZ_STUDENT_REFRESH_SECONDS`), shown until staff set one.

## Returns

`Element`
