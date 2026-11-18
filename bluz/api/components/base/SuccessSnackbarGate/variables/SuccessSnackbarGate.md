[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/SuccessSnackbarGate](../index.md) / SuccessSnackbarGate

# Variable: SuccessSnackbarGate

> `const` **SuccessSnackbarGate**: `ForwardRefExoticComponent`\<`Omit`\<`CustomContentProps` & `RefAttributes`\<`HTMLDivElement`\>, `"ref"`\> & `RefAttributes`\<`HTMLDivElement`\>\>

Defined in: [ui/src/components/base/SuccessSnackbarGate.tsx:18](https://github.com/System-B90/Bluz/blob/04ebae9cb334a01c6e7a55f885993f021e83cd92/ui/src/components/base/SuccessSnackbarGate.tsx#L18)

Replaces notistack's `success` variant. Read at render time, so a toast
enqueued after the user turned the preference off renders nothing.
