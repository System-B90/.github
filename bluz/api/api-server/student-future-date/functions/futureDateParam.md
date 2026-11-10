[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/student-future-date](../index.md) / futureDateParam

# Function: futureDateParam()

> **futureDateParam**(`searchParams`, `now?`): `string` \| `null`

Defined in: [ui/src/api-server/student-future-date.ts:13](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/api-server/student-future-date.ts#L13)

The first `?date=` value that points more than [FUTURE\_DATE\_PROBE\_MS](../../../api-shared/types/student-view/variables/FUTURE_DATE_PROBE_MS.md)
past `now`, or null. A bare `yyyy-MM-dd` means the start of that day in
Jerusalem, so tomorrow (under 24h away) passes and the day after does not;
anything else is parsed as a timestamp. Unparseable values are ignored —
the routes that read `date` already refuse them.

## Parameters

### searchParams

`URLSearchParams`

### now?

`number` = `...`

## Returns

`string` \| `null`
