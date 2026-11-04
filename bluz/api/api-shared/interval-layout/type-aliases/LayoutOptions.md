[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/interval-layout](../index.md) / LayoutOptions

# Type Alias: LayoutOptions

> **LayoutOptions** = `object`

Defined in: [ui/src/api-shared/interval-layout.ts:19](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-shared/interval-layout.ts#L19)

## Properties

### minSegmentMs?

> `optional` **minSegmentMs?**: `number`

Defined in: [ui/src/api-shared/interval-layout.ts:26](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-shared/interval-layout.ts#L26)

Shortest piece worth drawing. A run of free time shorter than this is
skipped over rather than emitted as an unreadable sliver — the working
time it would have carried is deferred to the next piece, so the total
is unaffected.
