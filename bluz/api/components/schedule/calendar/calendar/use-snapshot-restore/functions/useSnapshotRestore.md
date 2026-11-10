[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/calendar/calendar/use-snapshot-restore](../index.md) / useSnapshotRestore

# Function: useSnapshotRestore()

> **useSnapshotRestore**(): (`snapshotId`, `eventIds?`) => `Promise`\<`boolean`\>

Defined in: [ui/src/components/schedule/calendar/calendar/use-snapshot-restore.ts:16](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/schedule/calendar/calendar/use-snapshot-restore.ts#L16)

Runs a server-side snapshot restore — all of it, or just `eventIds` — and
returns to the live schedule to show the result. The calendar is refetched
rather than set locally: a local set would become an undo step, and undoing
it would push the pre-restore schedule back to the server.

## Returns

Restores; resolves to whether it succeeded (failures are reported).

(`snapshotId`, `eventIds?`) => `Promise`\<`boolean`\>
