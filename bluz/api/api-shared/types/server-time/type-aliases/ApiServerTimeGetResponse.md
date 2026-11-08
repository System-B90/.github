[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/server-time](../index.md) / ApiServerTimeGetResponse

# Type Alias: ApiServerTimeGetResponse

> **ApiServerTimeGetResponse** = `object`

Defined in: [ui/src/api-shared/types/server-time.ts:5](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-shared/types/server-time.ts#L5)

`GET /api/server-time` — the server clock, for students and staff alike.
Part of the student surface: the envelope is closed, `now` and nothing else.

## Properties

### now

> **now**: `number`

Defined in: [ui/src/api-shared/types/server-time.ts:7](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-shared/types/server-time.ts#L7)

Epoch ms when the response was built.
