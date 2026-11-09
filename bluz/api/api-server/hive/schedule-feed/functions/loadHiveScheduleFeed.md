[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/hive/schedule-feed](../index.md) / loadHiveScheduleFeed

# Function: loadHiveScheduleFeed()

> **loadHiveScheduleFeed**(`now?`): `Promise`\<[`HiveScheduleFeed`](../type-aliases/HiveScheduleFeed.md) \| `null`\>

Defined in: [ui/src/api-server/hive/schedule-feed.ts:448](https://github.com/System-B90/Bluz/blob/9a5da7a95daa31576d4bad28f2fe0e1ff1161c4a/ui/src/api-server/hive/schedule-feed.ts#L448)

The current iteration's schedule as a Hive feed, resolved with the Bluz
service account (the feed is fetched by a machine, never a browser).

## Parameters

### now?

`Date` = `...`

Centre of the published window (injectable for tests).

## Returns

`Promise`\<[`HiveScheduleFeed`](../type-aliases/HiveScheduleFeed.md) \| `null`\>

The calendar and its strong ETag, or null with no iteration yet.
