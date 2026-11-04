[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/server-clock](../index.md) / serverNow

# Function: serverNow()

> **serverNow**(): `number`

Defined in: [ui/src/components/base/server-clock.ts:77](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/components/base/server-clock.ts#L77)

The server's "now", epoch ms.

Before the first sync this is the device clock — a staff-calendar
convenience for its first paint only. The student board renders nothing
until [useServerClockSynced](useServerClockSynced.md) is true, so it never sees that fallback.

## Returns

`number`
