[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/gantt/api-layer](../index.md) / RawBaseDocument

# Type Alias: RawBaseDocument

> **RawBaseDocument** = `object`

Defined in: [ui/src/api-shared/types/gantt/api-layer.ts:27](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/api-layer.ts#L27)

A document as it comes off the wire: timestamps are still ISO strings, before
the client's date fixup turns them into Dayjs. Lives here rather than in
`api-client` because `api-shared` describes the wire shape and must not
depend on either side of it.

## Properties

### createdAt

> **createdAt**: `string`

Defined in: [ui/src/api-shared/types/gantt/api-layer.ts:28](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/api-layer.ts#L28)

***

### updatedAt

> **updatedAt**: `string`

Defined in: [ui/src/api-shared/types/gantt/api-layer.ts:29](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-shared/types/gantt/api-layer.ts#L29)
