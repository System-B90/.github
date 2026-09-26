[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/db-student-engagement](../index.md) / MAX\_ENGAGEMENT\_REPORT\_SECONDS

# Variable: MAX\_ENGAGEMENT\_REPORT\_SECONDS

> `const` **MAX\_ENGAGEMENT\_REPORT\_SECONDS**: `120` = `120`

Defined in: [ui/src/api-server/db-student-engagement.ts:12](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/api-server/db-student-engagement.ts#L12)

Largest increment a single report may carry, in seconds. The client flushes
on a fixed heartbeat, so anything much larger than one interval is either a
clock jump or a forged report — clamped rather than rejected so an honest
client with a stalled tab still records something plausible.
