[**TypeDoc API**](../../index.md)

***

[TypeDoc API](../../index.md) / [settings](../index.md) / STUDENT\_SYNC\_ID

# Variable: STUDENT\_SYNC\_ID

> `const` **STUDENT\_SYNC\_ID**: `"students:current"` = `"students:current"`

Defined in: [session-server/session-common.ts:128](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/session-server/session-common.ts#L128)

Sync-object id for the student refresh channel.

Students must never receive a calendar payload, so nothing is broadcast on
this id but an *empty* ping: the board refetches through
`/api/student-view/schedule`, which applies the whole student projection
server-side. It is also the only sync object a Hanich socket may register
for, which is what keeps iterations invisible to students — there is no
per-iteration student channel to subscribe to, and their fetch is pinned to
the current iteration server-side regardless.
