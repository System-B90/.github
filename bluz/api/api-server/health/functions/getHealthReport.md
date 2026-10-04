[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/health](../index.md) / getHealthReport

# Function: getHealthReport()

> **getHealthReport**(): `Promise`\<[`HealthReport`](../type-aliases/HealthReport.md)\>

Defined in: [ui/src/api-server/health.ts:68](https://github.com/System-B90/Bluz/blob/709d9b9fea27e88c533344b0ed282111c960722f/ui/src/api-server/health.ts#L68)

Hive is an external service Bluz degrades around rather than depends on
(see the fallback in the post-auth layout), so its being down must stay
distinguishable from Bluz itself being down — it never yields "unhealthy".

## Returns

`Promise`\<[`HealthReport`](../type-aliases/HealthReport.md)\>
