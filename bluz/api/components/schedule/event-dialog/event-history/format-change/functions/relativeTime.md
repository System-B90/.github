[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/schedule/event-dialog/event-history/format-change](../index.md) / relativeTime

# Function: relativeTime()

> **relativeTime**(`iso`): `string`

Defined in: [ui/src/components/schedule/event-dialog/event-history/format-change.ts:177](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/components/schedule/event-dialog/event-history/format-change.ts#L177)

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
