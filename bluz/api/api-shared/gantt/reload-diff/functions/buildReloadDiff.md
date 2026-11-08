[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/reload-diff](../index.md) / buildReloadDiff

# Function: buildReloadDiff()

> **buildReloadDiff**(`input`): [`ReloadDiff`](../../../types/gantt/reload/type-aliases/ReloadDiff.md)

Defined in: [ui/src/api-shared/gantt/reload-diff.ts:115](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-shared/gantt/reload-diff.ts#L115)

Classify every occurrence into add / update / remove / conflict / unchanged.
Manual edits win: a drifted event that a human touched becomes a conflict
instead of an update, unless its id is in `overrideEventIds`.

## Parameters

### input

[`ReloadDiffInput`](../type-aliases/ReloadDiffInput.md)

## Returns

[`ReloadDiff`](../../../types/gantt/reload/type-aliases/ReloadDiff.md)

## Example

```typescript
const diff = buildReloadDiff({ desired, actual, manuallyEditedIds });
```
