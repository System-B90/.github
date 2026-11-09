[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/student-security-log](../index.md) / MAX\_SECURITY\_EVENTS\_PER\_DAY

# Variable: MAX\_SECURITY\_EVENTS\_PER\_DAY

> `const` **MAX\_SECURITY\_EVENTS\_PER\_DAY**: `200` = `200`

Defined in: [ui/src/api-server/student-security-log.ts:22](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-server/student-security-log.ts#L22)

Most recent attempts kept per user per day. A hostile client can trigger
one write per request, so the array is capped (oldest dropped) while
`securityEventCount` keeps the true total.
