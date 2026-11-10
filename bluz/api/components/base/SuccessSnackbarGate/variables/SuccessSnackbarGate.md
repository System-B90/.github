[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/SuccessSnackbarGate](../index.md) / SuccessSnackbarGate

# Variable: SuccessSnackbarGate

> `const` **SuccessSnackbarGate**: `ForwardRefExoticComponent`\<`Omit`\<`CustomContentProps` & `RefAttributes`\<`HTMLDivElement`\>, `"ref"`\> & `RefAttributes`\<`HTMLDivElement`\>\>

Defined in: [ui/src/components/base/SuccessSnackbarGate.tsx:18](https://github.com/System-B90/Bluz/blob/8b8a83c5f7e9b6a85cfab9741a183d82b8eeaea9/ui/src/components/base/SuccessSnackbarGate.tsx#L18)

Replaces notistack's `success` variant. Read at render time, so a toast
enqueued after the user turned the preference off renders nothing.
