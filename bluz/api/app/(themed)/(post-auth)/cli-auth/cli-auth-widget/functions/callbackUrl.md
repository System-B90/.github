[**TypeDoc API**](../../../../../../index.md)

***

[TypeDoc API](../../../../../../index.md) / [app/(themed)/(post-auth)/cli-auth/cli-auth-widget](../index.md) / callbackUrl

# Function: callbackUrl()

> **callbackUrl**(`port`, `code`, `handoffCode`): `string`

Defined in: [ui/src/app/(themed)/(post-auth)/cli-auth/cli-auth-widget.tsx:32](https://github.com/System-B90/Bluz/blob/59b35ec547ab85fc4cb04fc9443883a2e8840381/ui/src/app/(themed)/(post-auth)/cli-auth/cli-auth-widget.tsx#L32)

The loopback callback URL. Carries the verification code (#521 -- proves
the browser talking to the CLI's server is the one this login started
from) and the single-use handoff code (#520). Never the session token
itself: the CLI exchanges the handoff code for the token in a separate
HTTPS call to the Bluz server, so the token never appears in this URL, in
browser history, or in the argv/logs of whatever answers on the loopback
port.

## Parameters

### port

`string`

### code

`string`

### handoffCode

`string`

## Returns

`string`
