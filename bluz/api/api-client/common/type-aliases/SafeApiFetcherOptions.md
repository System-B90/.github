[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-client/common](../index.md) / SafeApiFetcherOptions

# Type Alias: SafeApiFetcherOptions

> **SafeApiFetcherOptions** = `object`

Defined in: [ui/src/api-client/common.ts:37](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-client/common.ts#L37)

Per-call overrides for [safeApiFetcher](../functions/safeApiFetcher.md).

## Properties

### timeoutMs?

> `optional` **timeoutMs?**: `number`

Defined in: [ui/src/api-client/common.ts:43](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-client/common.ts#L43)

Overrides the default request ceiling. Only raise it for an endpoint
whose work genuinely takes longer than DEFAULT\_API\_TIMEOUT\_MS;
it is not a way to paper over a slow route.
