[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/student-refresh-interval](../index.md) / studentRefreshSeconds

# Function: studentRefreshSeconds()

> **studentRefreshSeconds**(`raw?`): `number`

Defined in: [ui/src/api-server/student-refresh-interval.ts:16](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-server/student-refresh-interval.ts#L16)

The deployment default for how often the student board refetches, in
seconds. The board does not follow staff edits live: it refetches on this
interval (and at server midnight, and on a staff push update). Staff
override it per iteration from the student preview
(`StudentViewSettings.refreshSeconds`); see [studentRefreshSecondsFor](studentRefreshSecondsFor.md).
`0` turns the periodic refetch off.

Read at request time, so a deployment changes it in `.env` without a rebuild.

## Parameters

### raw?

`string` \| `undefined`

## Returns

`number`
