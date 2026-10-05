[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/prayer](../index.md) / updatePrayerEvents

# Function: updatePrayerEvents()

> **updatePrayerEvents**(`__namedParameters`): `Promise`\<`void`\>

Defined in: [ui/src/api-server/prayer.ts:213](https://github.com/System-B90/Bluz/blob/d3e66c57dbea172998b0f35d995d47c87fad995d/ui/src/api-server/prayer.ts#L213)

## Parameters

### \_\_namedParameters

#### controller?

[`DatabaseController`](../../mongo-db-controller/classes/DatabaseController.md) = `databaseController`

Iteration DB the prayer events live in - must match the settings write.

#### iterationId?

`string`

#### newConfig

[`PrayerSettings`](../../../api-shared/types/settings/prayer/type-aliases/PrayerSettings.md)

#### startDate

`Date`

## Returns

`Promise`\<`void`\>
