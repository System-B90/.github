[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/cli-dist](../index.md) / CliDistManifest

# Type Alias: CliDistManifest

> **CliDistManifest** = `object`

Defined in: [ui/src/api-shared/types/cli-dist.ts:8](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/api-shared/types/cli-dist.ts#L8)

Response of `GET /api/cli-dist` — a bare object, not the API envelope.

## Properties

### plugin

> **plugin**: `null` \| `string`

Defined in: [ui/src/api-shared/types/cli-dist.ts:12](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/api-shared/types/cli-dist.ts#L12)

Plugin archive file name, null when not built.

***

### wheel

> **wheel**: `null` \| `string`

Defined in: [ui/src/api-shared/types/cli-dist.ts:10](https://github.com/System-B90/Bluz/blob/9da30d3fe7bc9583b86fb81afc4a7774c580c249/ui/src/api-shared/types/cli-dist.ts#L10)

Wheel file name (`bluz-<version>-py3-none-any.whl`), null when not built.
