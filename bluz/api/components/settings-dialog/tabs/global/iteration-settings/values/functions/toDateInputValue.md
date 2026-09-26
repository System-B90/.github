[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/settings-dialog/tabs/global/iteration-settings/values](../index.md) / toDateInputValue

# Function: toDateInputValue()

> **toDateInputValue**(`value`): `string`

Defined in: [ui/src/components/settings-dialog/tabs/global/iteration-settings/values.ts:14](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/components/settings-dialog/tabs/global/iteration-settings/values.ts#L14)

Date/string → yyyy-mm-dd for a native date input; "" when unset/invalid.

Formatted in the venue timezone, not UTC. A date-only picker stores local
midnight, and Asia/Jerusalem is UTC+2/+3, so slicing `toISOString()` reported
every iteration as starting the previous day.

## Parameters

### value

`string` \| `Date` \| `null` \| `undefined`

## Returns

`string`
