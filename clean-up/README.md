# Clean Up

Clean Up simplifies an existing interface by removing unnecessary UI, tightening copy, and improving local layout while preserving behavior, accessibility, and the product's visual identity.

## Install

```sh
npx skills add marksummer/skills
```

Choose **Clean Up** and **Codex**. Requires Node.js.

You can also copy this `clean-up` folder into `~/.codex/skills/` manually.

## Use

```text
$clean-up Clean up this upload screen. Keep the existing visual identity and behavior.
```

For copy-only work:

```text
$clean-up Simplify the copy on this screen. Keep all layout, styling, and behavior unchanged.
```

Provide the screen, source, or relevant project context. Clean Up honors explicit scope constraints and shows a compact before/after comparison with the verification performed.

## Optional Impeccable guidance

When Impeccable is already installed and available, Clean Up reads that installed skill and follows its **distill** guidance, plus **layout** guidance when arrangement contributes to clutter. Impeccable is not bundled or installed automatically. Clean Up also works without it.

## Example: upload screen

This example is a **local prototype with simulated transfers**. It illustrates interface cleanup; it does not demonstrate a production upload service.

The after example uses Clean Up with Impeccable available.

The revised screen groups the filename with its size and file limits, moves the change action beside the file, and gives the upload action more emphasis. Destination selection and sharing information remain visible.

### Before

![Before: upload form with separate destination, file details, and two adjacent buttons](../assets/clean-up/before-light.jpg)

### After

![After: grouped file details, inline Change action, and full-width Upload file button](../assets/clean-up/after-light.jpg)

<details>
<summary>Dark appearance</summary>

### Before

![Before upload screen in dark appearance](../assets/clean-up/before-dark.jpg)

### After

![After upload screen in dark appearance](../assets/clean-up/after-dark.jpg)

</details>
