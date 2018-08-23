# JavaScriptTemplateLiteralEnhancements

Package for Sublime Text 3.

## Install

**Via Package Control**:

1. Open Command Palette &rarr; `Package Control: Add Repository` &rarr; `https://github.com/phts/JavaScriptTemplateLiteralEnhancements`
2. Open Command Palette &rarr; `Package Control: Install Package` &rarr; `JavaScriptTemplateLiteralEnhancements`

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
