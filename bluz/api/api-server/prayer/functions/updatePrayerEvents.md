[**TypeDoc API**](../../../index.md)

***

[TypeDoc API](../../../index.md) / [api-server/prayer](../index.md) / updatePrayerEvents

# Function: updatePrayerEvents()

> **updatePrayerEvents**(`__namedParameters`): `Promise`\<`void`\>

Defined in: [ui/src/api-server/prayer.ts:216](https://github.com/System-B90/Bluz/blob/4901ffa77007f6f1d99198a04d841ed11708dad0/ui/src/api-server/prayer.ts#L216)

## Parameters

### \_\_namedParameters

#### controller?

[`DatabaseController`](../../mongo-db-controller/classes/DatabaseController.md) = `databaseController`

Iteration DB the prayer events live in - must match the settings write.

#### createMissing?

`boolean` = `true`

Create a day's prayers when it has none; false only retimes (#997).

#### iterationId?

`string`

#### newConfig

[`PrayerSettings`](../../../api-shared/types/settings/prayer/type-aliases/PrayerSettings.md)

#### startDate

`Date`

## Returns

`Promise`\<`void`\>
