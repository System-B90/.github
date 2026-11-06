[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/student-clock-skew](../index.md) / checkStudentClockSkew

# Function: checkStudentClockSkew()

> **checkStudentClockSkew**(`userId`, `headers`, `serverNow?`): `number` \| `null`

Defined in: [ui/src/api-server/student-clock-skew.ts:44](https://github.com/System-B90/Bluz/blob/90114c31e10132d84c8c3bab079c25588fbe0459/ui/src/api-server/student-clock-skew.ts#L44)

Compares a student board's device clock (the [STUDENT\_CLIENT\_TIME\_HEADER](../../../api-shared/types/student-view/variables/STUDENT_CLIENT_TIME_HEADER.md)
it sends) with the server's, and records a `clock-tampering` attempt when
they are more than [MAX\_STUDENT\_CLOCK\_SKEW\_MS](../../../api-shared/types/student-view/variables/MAX_STUDENT_CLOCK_SKEW_MS.md) apart, or the header is
not a timestamp at all.

Detection only: the response never depends on the header. The server serves
its own day whatever the device claims, and the board renders off the
response's `serverNow`. A missing header is not logged — a board loaded
before this shipped does not send one.

## Parameters

### userId

`string`

### headers

`Headers`

### serverNow?

`number` = `...`

## Returns

`number` \| `null`

The measured skew in ms (client − server), or null when unmeasurable.
