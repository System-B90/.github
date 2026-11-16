[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/server-clock](../index.md) / ROLLOVER\_GRACE\_MS

# Variable: ROLLOVER\_GRACE\_MS

> `const` **ROLLOVER\_GRACE\_MS**: `1000` = `1_000`

Defined in: [ui/src/components/base/server-clock.ts:17](https://github.com/System-B90/Bluz/blob/182d51c797407c7b0ea37986b1a45ab0e64c4df0/ui/src/components/base/server-clock.ts#L17)

How long past midnight a rollover fires. Covers the sync's error (half a
round trip), so the server has really moved on to the new day.
