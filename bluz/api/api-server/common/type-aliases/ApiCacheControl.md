[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/common](../index.md) / ApiCacheControl

# Type Alias: ApiCacheControl

> **ApiCacheControl** = `"immutable"` \| `"must-revalidate"` \| `"no-cache"` \| `"no-store"` \| \{ `immutable?`: `boolean`; `maxAge`: `number`; `scope`: `"private"` \| `"public"`; \} \| `number`

Defined in: [ui/src/api-server/common.ts:30](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/api-server/common.ts#L30)

The object form is explicit, for responses that must not land in a shared
cache. Every API route sits behind Hive SSO, so anything user- or
tenant-visible has to be `private` — a proxy holding a `public` copy would
serve it on.
