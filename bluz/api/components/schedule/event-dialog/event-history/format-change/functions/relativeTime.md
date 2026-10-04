[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/event-dialog/event-history/format-change](../index.md) / relativeTime

# Function: relativeTime()

> **relativeTime**(`iso`): `string`

Defined in: [ui/src/components/schedule/event-dialog/event-history/format-change.ts:165](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/components/schedule/event-dialog/event-history/format-change.ts#L165)

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
