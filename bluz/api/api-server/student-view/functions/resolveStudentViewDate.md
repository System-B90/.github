[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/student-view](../index.md) / resolveStudentViewDate

# Function: resolveStudentViewDate()

> **resolveStudentViewDate**(`rawDate`, `isStaff`): `string`

Defined in: [ui/src/api-server/student-view.ts:94](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-server/student-view.ts#L94)

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
