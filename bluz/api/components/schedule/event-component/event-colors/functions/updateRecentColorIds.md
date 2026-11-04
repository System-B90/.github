[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [components/schedule/event-component/event-colors](../index.md) / updateRecentColorIds

# Function: updateRecentColorIds()

> **updateRecentColorIds**(`prev`, `newId`, `max?`): `string`[]

Defined in: [ui/src/components/schedule/event-component/event-colors.ts:82](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/components/schedule/event-component/event-colors.ts#L82)

Moves `newId` to the front of the recent-colors list, dedupes it, and caps
the list at `max` entries.

## Parameters

### prev

`string`[]

### newId

`string`

### max?

`number` = `MAX_RECENT_COLORS`

## Returns

`string`[]
