[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/student-view/use-student-live-refresh](../index.md) / useStudentLiveRefresh

# Function: useStudentLiveRefresh()

> **useStudentLiveRefresh**(`onChange`, `onReload?`): `void`

Defined in: [ui/src/components/student-view/use-student-live-refresh.ts:40](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/components/student-view/use-student-live-refresh.ts#L40)

Keeps the student board live (#656).

The socket carries no calendar data to students: the only thing that arrives
on `STUDENT_SYNC_ID` is a content-free "something changed" ping, and the
board answers it by refetching `/api/student-view/schedule`, where the whole
student projection is applied. That keeps every guarantee — the field
allow-list, hidden events, the single-day window — server-side, which is the
only place it can be enforced.

The socket's ticket is scoped `hanich` for a student, so the session server
refuses to register it as a session (which would put it on the untargeted
broadcast) and refuses every sync object but this one. There is deliberately
no per-iteration student channel, so nothing here can reveal that iterations
exist.

A staff "push update" (`STUDENT_RELOAD`) reloads the whole page instead, so
a new deploy reaches every screen. Each board waits a random slice of
[RELOAD\_JITTER\_MS](../variables/RELOAD_JITTER_MS.md) first, so a room full of boards does not hit the
server in the same instant.

## Parameters

### onChange

() => `void`

Called when the schedule may have changed. Must be stable.

### onReload?

() => `void`

Called on a push update. Defaults to a jittered page reload.

## Returns

`void`
