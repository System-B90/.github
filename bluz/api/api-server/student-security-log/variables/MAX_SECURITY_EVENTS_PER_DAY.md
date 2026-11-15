[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/student-security-log](../index.md) / MAX\_SECURITY\_EVENTS\_PER\_DAY

# Variable: MAX\_SECURITY\_EVENTS\_PER\_DAY

> `const` **MAX\_SECURITY\_EVENTS\_PER\_DAY**: `200` = `200`

Defined in: [ui/src/api-server/student-security-log.ts:22](https://github.com/System-B90/Bluz/blob/d77dcf130db661461363a52910f62a34b3514ebd/ui/src/api-server/student-security-log.ts#L22)

Most recent attempts kept per user per day. A hostile client can trigger
one write per request, so the array is capped (oldest dropped) while
`securityEventCount` keeps the true total.
