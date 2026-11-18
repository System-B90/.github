[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/settings-dialog/tabs/global/iteration-settings/values](../index.md) / validateIteration

# Function: validateIteration()

> **validateIteration**(`values`): [`ValidationResult`](../../../common/UseEntityForm/type-aliases/ValidationResult.md)\<[`IterationValues`](../type-aliases/IterationValues.md)\>

Defined in: [ui/src/components/settings-dialog/tabs/global/iteration-settings/values.ts:73](https://github.com/System-B90/Bluz/blob/04ebae9cb334a01c6e7a55f885993f021e83cd92/ui/src/components/settings-dialog/tabs/global/iteration-settings/values.ts#L73)

Both fields are always required. The id is only *typed* when creating — on
an existing iteration it is populated and read-only — so there is no need
to know the form's mode here.

## Parameters

### values

[`IterationValues`](../type-aliases/IterationValues.md)

## Returns

[`ValidationResult`](../../../common/UseEntityForm/type-aliases/ValidationResult.md)\<[`IterationValues`](../type-aliases/IterationValues.md)\>
