[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/benchmark/fixture](../index.md) / isoAt

# Function: isoAt()

> **isoAt**(`dayOffset`, `hour`, `minute?`): `string`

Defined in: [ui/src/api-server/ai/benchmark/fixture.ts:60](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/ai/benchmark/fixture.ts#L60)

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
