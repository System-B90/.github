[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/student-view](../index.md) / StudentSecurityAction

# Enumeration: StudentSecurityAction

Defined in: [ui/src/api-shared/types/student-view.ts:129](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/api-shared/types/student-view.ts#L129)

Suspected malicious attempts recorded against a student's daily time record.
Each value names *what* was tried; the specifics ride in `detail`.

## Enumeration Members

### CLOCK\_TAMPERING

> **CLOCK\_TAMPERING**: `"clock-tampering"`

Defined in: [ui/src/api-shared/types/student-view.ts:153](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/api-shared/types/student-view.ts#L153)

The board's device clock is more than [MAX\_STUDENT\_CLOCK\_SKEW\_MS](../variables/MAX_STUDENT_CLOCK_SKEW_MS.md)
off the server's (or the clock header is not a timestamp): a student
winding the clock to reach another day.

***

### ENGAGEMENT\_TAMPERING

> **ENGAGEMENT\_TAMPERING**: `"engagement-tampering"`

Defined in: [ui/src/api-shared/types/student-view.ts:137](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/api-shared/types/student-view.ts#L137)

A malformed engagement report — a body the board cannot produce.

***

### FORGED\_SESSION\_TOKEN

> **FORGED\_SESSION\_TOKEN**: `"forged-session-token"`

Defined in: [ui/src/api-shared/types/student-view.ts:139](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/api-shared/types/student-view.ts#L139)

A session cookie that fails decryption: forged or altered, not merely expired.

***

### HEADER\_TAMPERING

> **HEADER\_TAMPERING**: `"header-tampering"`

Defined in: [ui/src/api-shared/types/student-view.ts:147](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/api-shared/types/student-view.ts#L147)

Headers a browser never sends — Next.js internals, verb/path overrides,
spoofed client addresses. nginx strips them and names them in
[HEADER\_TAMPERING\_HEADER](../variables/HEADER_TAMPERING_HEADER.md).

***

### INVALID\_ACCESS\_TOKEN

> **INVALID\_ACCESS\_TOKEN**: `"invalid-access-token"`

Defined in: [ui/src/api-shared/types/student-view.ts:141](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/api-shared/types/student-view.ts#L141)

A bearer token that is not a live Bluz access token.

***

### PARAM\_TAMPERING

> **PARAM\_TAMPERING**: `"param-tampering"`

Defined in: [ui/src/api-shared/types/student-view.ts:135](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/api-shared/types/student-view.ts#L135)

A Hanich session sent query parameters the board never sends (`?date=`, `?it=`, …).

***

### STAFF\_API\_PROBE

> **STAFF\_API\_PROBE**: `"staff-api-probe"`

Defined in: [ui/src/api-shared/types/student-view.ts:131](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/api-shared/types/student-view.ts#L131)

A Hanich session called a staff-only API.

***

### UNKNOWN\_ROUTE

> **UNKNOWN\_ROUTE**: `"unknown-route"`

Defined in: [ui/src/api-shared/types/student-view.ts:133](https://github.com/System-B90/Bluz/blob/74a052ee6650922fac951de899a2c2178970d1c0/ui/src/api-shared/types/student-view.ts#L133)

A Hanich session requested an API path that does not exist (dir-busting).
