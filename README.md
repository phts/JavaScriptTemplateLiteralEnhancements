# JSTemplateStringEnhancements

Plugin for Sublime Text 3.

## Install

**Via Package Control**:

1. `ctrl+shift+p` &rarr; `Package Control: Add Repository` &rarr; `https://github.com/phts/JSTemplateStringEnhancements.git`
2. `ctrl+shift+p` &rarr; `Package Control: Install Package` &rarr; `JSTemplateStringEnhancements`

## Usage

### Convert selected text into template placeholder

Select text inside a template string:

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

If nothing is selected type `$` inside template string to insert a placeholder:

```js
const str = `This is ${}`
```
