[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/server-clock](../index.md) / serverNow

# Function: serverNow()

> **serverNow**(): `number`

Defined in: [ui/src/components/base/server-clock.ts:77](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/components/base/server-clock.ts#L77)

The server's "now", epoch ms.

Before the first sync this is the device clock — a staff-calendar
convenience for its first paint only. The student board renders nothing
until [useServerClockSynced](useServerClockSynced.md) is true, so it never sees that fallback.

## Returns

`number`
