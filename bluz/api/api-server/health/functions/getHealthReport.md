[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/health](../index.md) / getHealthReport

# Function: getHealthReport()

> **getHealthReport**(): `Promise`\<[`HealthReport`](../type-aliases/HealthReport.md)\>

Defined in: [ui/src/api-server/health.ts:78](https://github.com/System-B90/Bluz/blob/d025a8d42fb581c0b03907e922b963d1295ddc4b/ui/src/api-server/health.ts#L78)

Hive is an external service Bluz degrades around rather than depends on
(see the fallback in the post-auth layout), so its being down must stay
distinguishable from Bluz itself being down — it never yields "unhealthy".

## Returns

`Promise`\<[`HealthReport`](../type-aliases/HealthReport.md)\>
