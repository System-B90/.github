[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/use-server-clock-sync](../index.md) / SERVER\_CLOCK\_RESYNC\_MS

# Variable: SERVER\_CLOCK\_RESYNC\_MS

> `const` **SERVER\_CLOCK\_RESYNC\_MS**: `number`

Defined in: [ui/src/components/base/use-server-clock-sync.ts:12](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/base/use-server-clock-sync.ts#L12)

Resync cadence. The monotonic clock does not drift meaningfully, but it may
pause while a device sleeps; waking resyncs at once, this is the backstop.
