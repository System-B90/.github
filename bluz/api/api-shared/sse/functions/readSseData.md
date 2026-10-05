[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/sse](../index.md) / readSseData

# Function: readSseData()

> **readSseData**(`body`): `AsyncGenerator`\<`string`\>

Defined in: [ui/src/api-shared/sse.ts:31](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-shared/sse.ts#L31)

Yields the payload of each `data:` line in an SSE body.

The tail of a chunk is buffered until a newline completes it. Comment lines
(`:` prefix, used by some backends as a keep-alive while a request queues)
are skipped, and the stream ends at [SSE\_DONE\_SENTINEL](../variables/SSE_DONE_SENTINEL.md).

## Parameters

### body

`ReadableStream`\<`Uint8Array`\<`ArrayBufferLike`\>\>

A response body stream.

## Returns

`AsyncGenerator`\<`string`\>

## Example

```ts
for await (const payload of readSseData(response.body)) {
    handle(JSON.parse(payload));
}
```
