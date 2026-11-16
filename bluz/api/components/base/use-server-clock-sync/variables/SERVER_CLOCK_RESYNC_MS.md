[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/use-server-clock-sync](../index.md) / SERVER\_CLOCK\_RESYNC\_MS

# Variable: SERVER\_CLOCK\_RESYNC\_MS

> `const` **SERVER\_CLOCK\_RESYNC\_MS**: `number`

Defined in: [ui/src/components/base/use-server-clock-sync.ts:12](https://github.com/System-B90/Bluz/blob/182d51c797407c7b0ea37986b1a45ab0e64c4df0/ui/src/components/base/use-server-clock-sync.ts#L12)

Resync cadence. The monotonic clock does not drift meaningfully, but it may
pause while a device sleeps; waking resyncs at once, this is the backstop.
