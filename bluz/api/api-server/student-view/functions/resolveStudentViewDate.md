[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/student-view](../index.md) / resolveStudentViewDate

# Function: resolveStudentViewDate()

> **resolveStudentViewDate**(`rawDate`, `isStaff`): `string`

Defined in: [ui/src/api-server/student-view.ts:68](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/student-view.ts#L68)

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
