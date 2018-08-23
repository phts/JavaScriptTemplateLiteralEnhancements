# JavaScriptTemplateLiteralEnhancements

[![Package Control](https://img.shields.io/packagecontrol/dt/JavaScriptTemplateLiteralEnhancements.svg)](https://packagecontrol.io/packages/JavaScriptTemplateLiteralEnhancements)

Package for Sublime Text 3.
Improve experience with template literals in JavaScript.

## Install

**Via Package Control**:

Open Command Palette &rarr; `Package Control: Install Package` &rarr; `JavaScriptTemplateLiteralEnhancements`

## Usage

### Convert selected text into template placeholder

Select text inside a template literal:

```js
                     ▼▼▼▼▼
const str = `This is value`
                     ▲▲▲▲▲
```

Type `$` and selection will be converted into template placeholder:

```js
const str = `This is ${value}`
```

### Insert template placeholder

If nothing is selected type `$` inside template literal to insert a placeholder:

```js
const str = `This is ${}`
```

### Convert into template/string literal

There are a few commands for converting string or template literal under the cursor or selection into single/double quoted string or template literal.

**Example:**

Put a cursor into a string literal:

```js
                           ▼
const str = 'This is my str|ing'
                           ▲
```

Open Command Palette and run command `JavaScriptTemplateLiteralEnhancements: Convert into template literal`.
This string will be converted into template literal:

```js
                           ▼
const str = `This is my str|ing`
                           ▲
```
