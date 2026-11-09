[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/gantt/reload-diff](../index.md) / buildReloadDiff

# Function: buildReloadDiff()

> **buildReloadDiff**(`input`): [`ReloadDiff`](../../../types/gantt/reload/type-aliases/ReloadDiff.md)

Defined in: [ui/src/api-shared/gantt/reload-diff.ts:115](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/gantt/reload-diff.ts#L115)

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
