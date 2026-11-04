[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-server/ai/benchmark/fixture](../index.md) / FIXTURE\_ROOMS

# Variable: FIXTURE\_ROOMS

> `const` **FIXTURE\_ROOMS**: `FixtureRoom`[]

Defined in: [ui/src/api-server/ai/benchmark/fixture.ts:87](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-server/ai/benchmark/fixture.ts#L87)

One room of each kind on purpose. Hive room ids are numbers, custom room ids
are strings, and a model that assumes every id is numeric round-trips a
custom room into a broken update — so the fixture makes it handle both.
