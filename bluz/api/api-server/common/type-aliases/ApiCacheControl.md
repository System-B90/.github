[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/common](../index.md) / ApiCacheControl

# Type Alias: ApiCacheControl

> **ApiCacheControl** = `"immutable"` \| `"must-revalidate"` \| `"no-cache"` \| `"no-store"` \| \{ `immutable?`: `boolean`; `maxAge`: `number`; `scope`: `"private"` \| `"public"`; \} \| `number`

Defined in: [ui/src/api-server/common.ts:22](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/common.ts#L22)

The object form is explicit, for responses that must not land in a shared
cache. Every API route sits behind Hive SSO, so anything user- or
tenant-visible has to be `private` — a proxy holding a `public` copy would
serve it on.
