[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/web-socket-utils](../index.md) / NotifyStudentsOfCalendarChange

# Function: NotifyStudentsOfCalendarChange()

> **NotifyStudentsOfCalendarChange**(`iterationId?`): `void`

Defined in: [ui/src/api-server/web-socket-utils.ts:190](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/web-socket-utils.ts#L190)

Tells student boards that the current iteration's calendar changed, so they
refetch (#656).

Deliberately payload-free. Students may not receive event data over the
wire at all; the refetch goes through `/api/student-view/schedule`, which is
where the whole student projection — the field allow-list, the hidden-event
exclusion, the single-day window — is applied. Sending the changed event
here instead would put every one of those guarantees on the wrong side of
the boundary.

Only current-iteration writes ping: a student's board is pinned to the
current iteration server-side and has no concept of any other.

## Parameters

### iterationId?

`string`

The iteration that was written to, if any.

## Returns

`void`
