[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/benchmark/fixture](../index.md) / filterFixtureEvents

# Function: filterFixtureEvents()

> **filterFixtureEvents**(`args`): `object`[]

Defined in: [ui/src/api-server/ai/benchmark/fixture.ts:302](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/api-server/ai/benchmark/fixture.ts#L302)

Answers `list_events` the way production does — range overlap and the
hidden/fake/name filters — so a model that reads only Tuesday sees only
Tuesday, and one that never filters sees everything.

## Parameters

### args

[`FixtureListEventsArgs`](../type-aliases/FixtureListEventsArgs.md)

## Returns

`object`[]
