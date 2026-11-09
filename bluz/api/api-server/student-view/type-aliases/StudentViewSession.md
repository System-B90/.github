[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/student-view](../index.md) / StudentViewSession

# Type Alias: StudentViewSession

> **StudentViewSession** = `object`

Defined in: [ui/src/api-server/student-view.ts:52](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-server/student-view.ts#L52)

## Properties

### clearance

> **clearance**: `Clearance`

Defined in: [ui/src/api-server/student-view.ts:53](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-server/student-view.ts#L53)

***

### isChecker

> **isChecker**: `boolean`

Defined in: [ui/src/api-server/student-view.ts:57](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-server/student-view.ts#L57)

Checker (read-only staff-shell viewer). Only with `allowChecker`.

***

### isStaff

> **isStaff**: `boolean`

Defined in: [ui/src/api-server/student-view.ts:55](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-server/student-view.ts#L55)

Staff (Segel/Admin) get the preview affordances; students never do.

***

### userId

> **userId**: `string`

Defined in: [ui/src/api-server/student-view.ts:59](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-server/student-view.ts#L59)

Session-derived user id. Never taken from a request body.
