[**TypeDoc API**](../../index.md)

***

[TypeDoc API](../../index.md) / [settings](../index.md) / STUDENT\_SYNC\_ID

# Variable: STUDENT\_SYNC\_ID

> `const` **STUDENT\_SYNC\_ID**: `"students:current"` = `"students:current"`

Defined in: [session-server/session-common.ts:130](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/session-server/session-common.ts#L130)

Sync-object id for the student refresh channel.

Students must never receive a calendar payload, so nothing is broadcast on
this id but an *empty* ping: the board refetches through
`/api/student-view/schedule`, which applies the whole student projection
server-side. It is also the only sync object a Hanich socket may register
for, which is what keeps iterations invisible to students — there is no
per-iteration student channel to subscribe to, and their fetch is pinned to
the current iteration server-side regardless.
