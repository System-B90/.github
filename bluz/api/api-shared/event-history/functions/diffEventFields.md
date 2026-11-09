[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-shared/event-history](../index.md) / diffEventFields

# Function: diffEventFields()

> **diffEventFields**(`before`, `after`): [`EventFieldChange`](../../types/event-history/type-aliases/EventFieldChange.md)[]

Defined in: [ui/src/api-shared/event-history.ts:65](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/event-history.ts#L65)

Field-level diff between two versions of an event document.

## Parameters

### before

`Record`\<`string`, `unknown`\> \| `null`

The stored document, or null for a creation.

### after

`Record`\<`string`, `unknown`\>

The document being written.

## Returns

[`EventFieldChange`](../../types/event-history/type-aliases/EventFieldChange.md)[]

One entry per differing field; empty when nothing changed.

## Example

```typescript
const changes = diffEventFields(stored, incoming); // [{ field: "startTime", … }]
```
