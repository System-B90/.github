[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/benchmark/fixture](../index.md) / isoAt

# Function: isoAt()

> **isoAt**(`dayOffset`, `hour`, `minute?`): `string`

Defined in: [ui/src/api-server/ai/benchmark/fixture.ts:60](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/api-server/ai/benchmark/fixture.ts#L60)

Places a fixture event relative to [FIXTURE\_NOW](../variables/FIXTURE_NOW.md).

Goes through the app's dayjs setup rather than raw `Date` arithmetic: these
are school hours, which means Israel wall-clock, and only `APP_TIMEZONE`
gets that right on both sides of a DST transition.

## Parameters

### dayOffset

`number`

### hour

`number`

### minute?

`number` = `0`

## Returns

`string`
