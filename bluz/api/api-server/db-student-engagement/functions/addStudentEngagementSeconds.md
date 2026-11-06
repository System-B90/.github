[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/db-student-engagement](../index.md) / addStudentEngagementSeconds

# Function: addStudentEngagementSeconds()

> **addStudentEngagementSeconds**(`userId`, `date`, `seconds`, `ip?`): `Promise`\<`number`\>

Defined in: [ui/src/api-server/db-student-engagement.ts:33](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-server/db-student-engagement.ts#L33)

Adds focused-time to a student's counter for one day (#656).

The caller's identity comes from the session, never from the request body —
a student must not be able to write to another student's counter. The
increment is clamped on the way in and the running total is capped, so a
scripted client can inflate its own number only up to a day's length.

## Parameters

### userId

`string`

Session-derived user id.

### date

`string`

`yyyy-MM-dd` in the app timezone.

### seconds

`number`

Reported focused seconds since the last report.

### ip?

`string`

The reporting address (from nginx, never the body), added to the
          day's `ips`, so an unattributable attempt in the security log can
          be matched to whoever used that address.

## Returns

`Promise`\<`number`\>

The seconds actually recorded.
