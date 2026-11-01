[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/use-server-clock-sync](../index.md) / useServerClockSync

# Function: useServerClockSync()

> **useServerClockSync**(): `boolean`

Defined in: [ui/src/components/base/use-server-clock-sync.ts:36](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/components/base/use-server-clock-sync.ts#L36)

Reads the server clock from `/api/server-time` — on mount, whenever the tab
comes back to the foreground, and every [SERVER\_CLOCK\_RESYNC\_MS](../variables/SERVER_CLOCK_RESYNC_MS.md).
Shared by the staff calendar and the student board.

## Returns

`boolean`

Whether the server clock is known yet.
