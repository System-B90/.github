[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/cli-dist](../index.md) / CliDistManifest

# Type Alias: CliDistManifest

> **CliDistManifest** = `object`

Defined in: [ui/src/api-shared/types/cli-dist.ts:8](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/api-shared/types/cli-dist.ts#L8)

Response of `GET /api/cli-dist` — a bare object, not the API envelope.

## Properties

### plugin

> **plugin**: `null` \| `string`

Defined in: [ui/src/api-shared/types/cli-dist.ts:12](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/api-shared/types/cli-dist.ts#L12)

Plugin archive file name, null when not built.

***

### wheel

> **wheel**: `null` \| `string`

Defined in: [ui/src/api-shared/types/cli-dist.ts:10](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/api-shared/types/cli-dist.ts#L10)

Wheel file name (`bluz-<version>-py3-none-any.whl`), null when not built.
