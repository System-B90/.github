[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [components/settings-dialog/tabs/global/common](../index.md) / ReadOnlyListCardBaseProps

# Type Alias: ReadOnlyListCardBaseProps\<TEntity\>

> **ReadOnlyListCardBaseProps**\<`TEntity`\> = `Omit`\<[`ListCardBaseProps`](ListCardBaseProps.md)\<`TEntity`\>, `"handleDelete"`\>

Defined in: [ui/src/components/settings-dialog/tabs/global/common/index.tsx:23](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/components/settings-dialog/tabs/global/common/index.tsx#L23)

List-card props for a tab whose entities cannot be deleted — iterations own
a database each, so they are created and edited but never removed here.

## Type Parameters

### TEntity

`TEntity`
