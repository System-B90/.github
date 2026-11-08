[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/settings-dialog/tabs/global/common](../index.md) / ReadOnlyListCardBaseProps

# Type Alias: ReadOnlyListCardBaseProps\<TEntity\>

> **ReadOnlyListCardBaseProps**\<`TEntity`\> = `Omit`\<[`ListCardBaseProps`](ListCardBaseProps.md)\<`TEntity`\>, `"handleDelete"`\>

Defined in: [ui/src/components/settings-dialog/tabs/global/common/index.tsx:23](https://github.com/System-B90/Bluz/blob/71d1184149e053a7a1461d3b70913493e6ec8833/ui/src/components/settings-dialog/tabs/global/common/index.tsx#L23)

List-card props for a tab whose entities cannot be deleted — iterations own
a database each, so they are created and edited but never removed here.

## Type Parameters

### TEntity

`TEntity`
