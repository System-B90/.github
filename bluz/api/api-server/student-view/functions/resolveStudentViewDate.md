[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/student-view](../index.md) / resolveStudentViewDate

# Function: resolveStudentViewDate()

> **resolveStudentViewDate**(`rawDate`, `isStaff`): `string`

Defined in: [ui/src/api-server/student-view.ts:95](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-server/student-view.ts#L95)

Resolves which day to serve. Students always get the *server's* current day
in the app timezone; a client-supplied date is not merely ignored for them
but rejected, so a probe for another day is a hard error rather than a
silently-succeeding request. Staff may pass one to preview another day.

## Parameters

### rawDate

`string` \| `null`

### isStaff

`boolean`

## Returns

`string`
