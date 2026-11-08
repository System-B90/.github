[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/use-server-clock-sync](../index.md) / useServerClockSync

# Function: useServerClockSync()

> **useServerClockSync**(): `boolean`

Defined in: [ui/src/components/base/use-server-clock-sync.ts:36](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/base/use-server-clock-sync.ts#L36)

Reads the server clock from `/api/server-time` — on mount, whenever the tab
comes back to the foreground, and every [SERVER\_CLOCK\_RESYNC\_MS](../variables/SERVER_CLOCK_RESYNC_MS.md).
Shared by the staff calendar and the student board.

## Returns

`boolean`

Whether the server clock is known yet.
