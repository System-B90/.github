[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/student-refresh-interval](../index.md) / studentRefreshSeconds

# Function: studentRefreshSeconds()

> **studentRefreshSeconds**(`raw?`): `number`

Defined in: [ui/src/api-server/student-refresh-interval.ts:12](https://github.com/System-B90/Bluz/blob/2fa23325da73d58527b069b0943f3bd1e838efee/ui/src/api-server/student-refresh-interval.ts#L12)

How often the student board refetches on its own, in seconds. The live
ping already covers staff edits; this is the safety net for a missed ping
(dropped socket, a write path that does not ping) and for the day rolling
over on a wall display. `0` turns it off.

Read at request time, so a deployment changes it in `.env` without a rebuild.

## Parameters

### raw?

`string` \| `undefined`

## Returns

`number`
