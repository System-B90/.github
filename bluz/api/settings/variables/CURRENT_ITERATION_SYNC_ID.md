[**TypeDoc API**](../../index.md)

***

[TypeDoc API](../../index.md) / [settings](../index.md) / CURRENT\_ITERATION\_SYNC\_ID

# Variable: CURRENT\_ITERATION\_SYNC\_ID

> `const` **CURRENT\_ITERATION\_SYNC\_ID**: `"iteration:current"` = `"iteration:current"`

Defined in: [session-server/session-common.ts:92](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/session-server/session-common.ts#L92)

Sync-object id for iteration-scoped calendar broadcasts (#525). Event
payloads carry a full `DbEventDocument`, not an id — fanning them out to
every logged-in browser regardless of which iteration it's viewing means
every user's wire receives every curriculum's complete event data. Clients
register as a sync-object listener for the iteration they're viewing
(`undefined` iterationId means "the current run"), and the server passes
the same id as `targets` on iteration-scoped broadcasts, so
`dispatchToSyncObjectListeners` only reaches sockets actually viewing that
iteration.
