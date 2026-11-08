[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [api-server/hive/session-client](../index.md) / createHiveClient

# Function: createHiveClient()

> **createHiveClient**(`hiveUrl?`): `Promise`\<[`HiveClient`](../../client/classes/HiveClient.md)\>

Defined in: [ui/src/api-server/hive/session-client.ts:31](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/api-server/hive/session-client.ts#L31)

A Hive client acting as the current caller, with the caller's own Hive SSO
tokens — so Hive applies that user's permissions, never broader ones.

Personal access tokens carry no Hive credentials and are refused. Never
fall back to the service account here: it would hand a token holder the
service account's Hive view instead of their own. (Delegating the user's
Hive refresh token does not work either: it is short-lived and rotates, so
a 90-day access token would lose Hive within a day.)

## Parameters

### hiveUrl?

`string`

## Returns

`Promise`\<[`HiveClient`](../../client/classes/HiveClient.md)\>

## Throws

HiveSessionRequiredError for an access-token caller.

## Throws

UserNotLoggedInError when there is no caller at all.
