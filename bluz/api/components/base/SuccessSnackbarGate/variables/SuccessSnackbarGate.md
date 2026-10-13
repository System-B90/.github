[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/SuccessSnackbarGate](../index.md) / SuccessSnackbarGate

# Variable: SuccessSnackbarGate

> `const` **SuccessSnackbarGate**: `ForwardRefExoticComponent`\<`Omit`\<`CustomContentProps` & `RefAttributes`\<`HTMLDivElement`\>, `"ref"`\> & `RefAttributes`\<`HTMLDivElement`\>\>

Defined in: [ui/src/components/base/SuccessSnackbarGate.tsx:18](https://github.com/System-B90/Bluz/blob/624fadadf2fc828abebeab4f5f0c3cf73dcb1351/ui/src/components/base/SuccessSnackbarGate.tsx#L18)

Replaces notistack's `success` variant. Read at render time, so a toast
enqueued after the user turned the preference off renders nothing.
