[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/benchmark/fixture](../index.md) / FIXTURE\_ROOMS

# Variable: FIXTURE\_ROOMS

> `const` **FIXTURE\_ROOMS**: `FixtureRoom`[]

Defined in: [ui/src/api-server/ai/benchmark/fixture.ts:86](https://github.com/System-B90/Bluz/blob/23625511d59d71bc9679adc341fb0bcb28897208/ui/src/api-server/ai/benchmark/fixture.ts#L86)

One room of each kind on purpose. Hive room ids are numbers, custom room ids
are strings, and a model that assumes every id is numeric round-trips a
custom room into a broken update — so the fixture makes it handle both.
