[**TypeDoc API**](../../../../../../../index.md)

***

[TypeDoc API](../../../../../../../index.md) / [components/settings-dialog/tabs/global/iteration-settings/IterationListCard](../index.md) / IterationListCardProps

# Type Alias: IterationListCardProps

> **IterationListCardProps** = `Omit`\<[`ReadOnlyListCardBaseProps`](../../../common/type-aliases/ReadOnlyListCardBaseProps.md)\<[`Iteration`](../../../../../../../api-shared/types/iteration/type-aliases/Iteration.md)\>, `"selectedEntity"`\> & `object`

Defined in: [ui/src/components/settings-dialog/tabs/global/iteration-settings/IterationListCard.tsx:20](https://github.com/System-B90/Bluz/blob/dc14d71ac6f49f030d3e8da9b6d9365589260844/ui/src/components/settings-dialog/tabs/global/iteration-settings/IterationListCard.tsx#L20)

## Type Declaration

### busyId

> **busyId**: `null` \| `string`

Id of the iteration currently being switched to, if any.

### onMakeCurrent

> **onMakeCurrent**: (`iteration`) => `void`

#### Parameters

##### iteration

[`Iteration`](../../../../../../../api-shared/types/iteration/type-aliases/Iteration.md)

#### Returns

`void`
