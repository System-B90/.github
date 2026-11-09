[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-shared/types/student-view](../index.md) / StudentSecurityAction

# Enumeration: StudentSecurityAction

Defined in: [ui/src/api-shared/types/student-view.ts:148](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/types/student-view.ts#L148)

Suspected malicious attempts recorded against a student's daily time record.
Each value names *what* was tried; the specifics ride in `detail`.

## Enumeration Members

### CLOCK\_TAMPERING

> **CLOCK\_TAMPERING**: `"clock-tampering"`

Defined in: [ui/src/api-shared/types/student-view.ts:172](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/types/student-view.ts#L172)

The board's device clock is more than [MAX\_STUDENT\_CLOCK\_SKEW\_MS](../variables/MAX_STUDENT_CLOCK_SKEW_MS.md)
off the server's (or the clock header is not a timestamp): a student
winding the clock to reach another day.

***

### ENGAGEMENT\_TAMPERING

> **ENGAGEMENT\_TAMPERING**: `"engagement-tampering"`

Defined in: [ui/src/api-shared/types/student-view.ts:156](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/types/student-view.ts#L156)

A malformed engagement report — a body the board cannot produce.

***

### FORGED\_SESSION\_TOKEN

> **FORGED\_SESSION\_TOKEN**: `"forged-session-token"`

Defined in: [ui/src/api-shared/types/student-view.ts:158](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/types/student-view.ts#L158)

A session cookie that fails decryption: forged or altered, not merely expired.

***

### HEADER\_TAMPERING

> **HEADER\_TAMPERING**: `"header-tampering"`

Defined in: [ui/src/api-shared/types/student-view.ts:166](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/types/student-view.ts#L166)

Headers a browser never sends — Next.js internals, verb/path overrides,
spoofed client addresses. nginx strips them and names them in
[HEADER\_TAMPERING\_HEADER](../variables/HEADER_TAMPERING_HEADER.md).

***

### INVALID\_ACCESS\_TOKEN

> **INVALID\_ACCESS\_TOKEN**: `"invalid-access-token"`

Defined in: [ui/src/api-shared/types/student-view.ts:160](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/types/student-view.ts#L160)

A bearer token that is not a live Bluz access token.

***

### PARAM\_TAMPERING

> **PARAM\_TAMPERING**: `"param-tampering"`

Defined in: [ui/src/api-shared/types/student-view.ts:154](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/types/student-view.ts#L154)

A Hanich session sent query parameters the board never sends (`?date=`, `?it=`, …).

***

### STAFF\_API\_PROBE

> **STAFF\_API\_PROBE**: `"staff-api-probe"`

Defined in: [ui/src/api-shared/types/student-view.ts:150](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/types/student-view.ts#L150)

A Hanich session called a staff-only API.

***

### UNKNOWN\_ROUTE

> **UNKNOWN\_ROUTE**: `"unknown-route"`

Defined in: [ui/src/api-shared/types/student-view.ts:152](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-shared/types/student-view.ts#L152)

A Hanich session requested an API path that does not exist (dir-busting).
