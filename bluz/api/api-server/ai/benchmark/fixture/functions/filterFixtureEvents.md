[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/benchmark/fixture](../index.md) / filterFixtureEvents

# Function: filterFixtureEvents()

> **filterFixtureEvents**(`args`): `object`[]

Defined in: [ui/src/api-server/ai/benchmark/fixture.ts:304](https://github.com/System-B90/Bluz/blob/04ebae9cb334a01c6e7a55f885993f021e83cd92/ui/src/api-server/ai/benchmark/fixture.ts#L304)

Answers `list_events` the way production does — range overlap and the
hidden/fake/name filters — so a model that reads only Tuesday sees only
Tuesday, and one that never filters sees everything.

## Parameters

### args

[`FixtureListEventsArgs`](../type-aliases/FixtureListEventsArgs.md)

## Returns

`object`[]
