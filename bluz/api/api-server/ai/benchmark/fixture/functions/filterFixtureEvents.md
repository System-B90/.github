[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/benchmark/fixture](../index.md) / filterFixtureEvents

# Function: filterFixtureEvents()

> **filterFixtureEvents**(`args`): `object`[]

Defined in: [ui/src/api-server/ai/benchmark/fixture.ts:304](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-server/ai/benchmark/fixture.ts#L304)

Answers `list_events` the way production does — range overlap and the
hidden/fake/name filters — so a model that reads only Tuesday sees only
Tuesday, and one that never filters sees everything.

## Parameters

### args

[`FixtureListEventsArgs`](../type-aliases/FixtureListEventsArgs.md)

## Returns

`object`[]
