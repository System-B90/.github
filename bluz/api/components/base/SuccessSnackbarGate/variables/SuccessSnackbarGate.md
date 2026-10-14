[**TypeDoc API**](../../../../index.md)

***

[TypeDoc API](../../../../index.md) / [components/base/SuccessSnackbarGate](../index.md) / SuccessSnackbarGate

# Variable: SuccessSnackbarGate

> `const` **SuccessSnackbarGate**: `ForwardRefExoticComponent`\<`Omit`\<`CustomContentProps` & `RefAttributes`\<`HTMLDivElement`\>, `"ref"`\> & `RefAttributes`\<`HTMLDivElement`\>\>

Defined in: [ui/src/components/base/SuccessSnackbarGate.tsx:17](https://github.com/System-B90/Bluz/blob/2cdd88d3becf12eb3973de760603dde72ccbd37e/ui/src/components/base/SuccessSnackbarGate.tsx#L17)

Replaces notistack's `success` variant. Read at render time, so a toast
enqueued after the user turned the preference off renders nothing.
