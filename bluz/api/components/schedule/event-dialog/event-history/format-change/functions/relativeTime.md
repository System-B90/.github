[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/event-dialog/event-history/format-change](../index.md) / relativeTime

# Function: relativeTime()

> **relativeTime**(`iso`): `string`

Defined in: [ui/src/components/schedule/event-dialog/event-history/format-change.ts:177](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/components/schedule/event-dialog/event-history/format-change.ts#L177)

Relative wording for a timestamp ("לפני 5 דקות"), with day granularity past
a week. Kept local rather than pulling in dayjs' relativeTime plugin and a
Hebrew locale bundle for one label.

## Parameters

### iso

`string`

ISO timestamp of the change.

## Returns

`string`

A Hebrew phrase, or an absolute date once older than a week.

## Example

```typescript
relativeTime(oneMinuteAgo); // "לפני דקה"
```
