[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-client/common](../index.md) / SafeApiFetcherOptions

# Type Alias: SafeApiFetcherOptions

> **SafeApiFetcherOptions** = `object`

Defined in: [ui/src/api-client/common.ts:45](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-client/common.ts#L45)

Per-call overrides for [safeApiFetcher](../functions/safeApiFetcher.md).

## Properties

### timeoutMs?

> `optional` **timeoutMs?**: `number`

Defined in: [ui/src/api-client/common.ts:51](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-client/common.ts#L51)

Overrides the default request ceiling. Only raise it for an endpoint
whose work genuinely takes longer than DEFAULT\_API\_TIMEOUT\_MS;
it is not a way to paper over a slow route.
