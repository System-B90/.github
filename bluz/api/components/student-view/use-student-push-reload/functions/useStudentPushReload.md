[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/student-view/use-student-push-reload](../index.md) / useStudentPushReload

# Function: useStudentPushReload()

> **useStudentPushReload**(`onReload?`): `void`

Defined in: [ui/src/components/student-view/use-student-push-reload.ts:38](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/components/student-view/use-student-push-reload.ts#L38)

The student board's one socket subscription (#656): the staff "push update".

The board does not follow staff edits live. It refetches on its own
interval (staff-set from the student preview), at server midnight, and when
staff push an update — which arrives here as `STUDENT_RELOAD` and reloads
the whole page, so a new deploy reaches every screen too. Each board waits a
random slice of [RELOAD\_JITTER\_MS](../variables/RELOAD_JITTER_MS.md) first, so a room full of boards
does not hit the server in the same instant.

The server still sends a content-free `STUDENT_REFRESH` ping on every
calendar change on the same channel; it is deliberately ignored, so edits
reach students at the next interval rather than as they are typed.

The socket's ticket is scoped `hanich` for a student, so the session server
refuses to register it as a session (which would put it on the untargeted
broadcast) and refuses every sync object but `STUDENT_SYNC_ID`. There is
deliberately no per-iteration student channel, so nothing here can reveal
that iterations exist.

## Parameters

### onReload?

() => `void`

Called on a push update. Defaults to a jittered page reload.

## Returns

`void`
