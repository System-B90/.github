[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/SuccessSnackbarGate](../index.md) / SuccessSnackbarGate

# Variable: SuccessSnackbarGate

> `const` **SuccessSnackbarGate**: `ForwardRefExoticComponent`\<`Omit`\<`CustomContentProps` & `RefAttributes`\<`HTMLDivElement`\>, `"ref"`\> & `RefAttributes`\<`HTMLDivElement`\>\>

Defined in: [ui/src/components/base/SuccessSnackbarGate.tsx:17](https://github.com/System-B90/Bluz/blob/9293ec523a02fdbe59b9479de6b3caee2f4be11c/ui/src/components/base/SuccessSnackbarGate.tsx#L17)

Replaces notistack's `success` variant. Read at render time, so a toast
enqueued after the user turned the preference off renders nothing.
