[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/health](../index.md) / getHealthReport

# Function: getHealthReport()

> **getHealthReport**(): `Promise`\<[`HealthReport`](../type-aliases/HealthReport.md)\>

Defined in: [ui/src/api-server/health.ts:78](https://github.com/System-B90/Bluz/blob/92e9db4014b408fc300f0c61d7bd7e8f4dbbac3f/ui/src/api-server/health.ts#L78)

Hive is an external service Bluz degrades around rather than depends on
(see the fallback in the post-auth layout), so its being down must stay
distinguishable from Bluz itself being down — it never yields "unhealthy".

## Returns

`Promise`\<[`HealthReport`](../type-aliases/HealthReport.md)\>
