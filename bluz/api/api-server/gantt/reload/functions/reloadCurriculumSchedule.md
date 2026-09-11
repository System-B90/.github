[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/gantt/reload](../index.md) / reloadCurriculumSchedule

# Function: reloadCurriculumSchedule()

> **reloadCurriculumSchedule**(`curriculumId`, `options?`): `Promise`\<[`ReloadOutcome`](../type-aliases/ReloadOutcome.md)\>

Defined in: [ui/src/api-server/gantt/reload.ts:153](https://github.com/System-B90/Bluz/blob/f13390751945b58bf7813b0aca9fcb12d9e18cf5/ui/src/api-server/gantt/reload.ts#L153)

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
