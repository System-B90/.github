[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/reload](../index.md) / reloadCurriculumSchedule

# Function: reloadCurriculumSchedule()

> **reloadCurriculumSchedule**(`curriculumId`, `options?`): `Promise`\<[`ReloadOutcome`](../type-aliases/ReloadOutcome.md)\>

Defined in: [ui/src/api-server/gantt/reload.ts:195](https://github.com/System-B90/Bluz/blob/901cc8f4c754d82c12fc600337c5991c07a64502/ui/src/api-server/gantt/reload.ts#L195)

Re-cut a curriculum onto its existing schedule.

## Parameters

### curriculumId

`string`

Curriculum to reload from.

### options?

[`ReloadOptions`](../type-aliases/ReloadOptions.md) = `{}`

## Returns

`Promise`\<[`ReloadOutcome`](../type-aliases/ReloadOutcome.md)\>

## Example

```typescript
const preview = await reloadCurriculumSchedule(id, { dryRun: true });
```
