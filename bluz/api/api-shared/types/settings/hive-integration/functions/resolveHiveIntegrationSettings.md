[**TypeDoc API**](../../../../../index.md)

***

[TypeDoc API](../../../../../index.md) / [api-shared/types/settings/hive-integration](../index.md) / resolveHiveIntegrationSettings

# Function: resolveHiveIntegrationSettings()

> **resolveHiveIntegrationSettings**(`value`): [`HiveIntegrationSettings`](../type-aliases/HiveIntegrationSettings.md)

Defined in: [ui/src/api-shared/types/settings/hive-integration.ts:124](https://github.com/System-B90/Bluz/blob/1023d781d8ebc75af95baadcabc62a9e9bf002f3/ui/src/api-shared/types/settings/hive-integration.ts#L124)

A stored setting made safe to act on: a missing or corrupt driver falls
back to the activator (behaviour before the setting), an unusable
calendar path is dropped so the sidecar keeps its own default, and an
unusable window falls back to ±24h.

## Parameters

### value

`Partial`\<[`HiveIntegrationSettings`](../type-aliases/HiveIntegrationSettings.md)\> \| `null` \| `undefined`

The stored value, or null when nothing was saved yet.

## Returns

[`HiveIntegrationSettings`](../type-aliases/HiveIntegrationSettings.md)

The settings to act on.
