from functools import reduce

import sublime
import sublime_plugin

SUPPORTED_LITERALS = {
    'template': {
        'scopes': [
            'string.template.js',
            'string.template.js.fjsx15',
        ],
        'symbol': '`',
    },
    'single_quoted_string': {
        'scopes': [
            'string.quoted.single.js',
            'string.quoted.single.js.fjsx15',
        ],
        'symbol': '\'',
    },
    'double_quoted_string': {
        'scopes': [
            'string.quoted.double.js',
            'string.quoted.double.js.fjsx15',
        ],
        'symbol': '"',
    },
}

def is_any_included_in_scope_name(scope_name, values):
    scopes = scope_name.split(' ')
    return any(sc in values for sc in scopes)

def is_supported_template_scope(scope_name):
    return if_scopes_include_one_of(scope_name, SUPPORTED_LITERALS['template']['scopes'])

def wrap_insert(view, edit, region, str):
    view.insert(edit, region.end(), str)
    view.insert(edit, region.begin(), str)

def wrap_replace_inside(view, edit, region, str):
    view.replace(edit, sublime.Region(region.begin(), region.begin() + 1), str)
    view.replace(edit, sublime.Region(region.end() - 1, region.end()), str)

def wrap_replace_outside(view, edit, region, str):
    view.replace(edit, sublime.Region(region.begin() - 1, region.begin()), str)
    view.replace(edit, sublime.Region(region.end(), region.end() + 1), str)

def convert_into_literal(literal, view, edit):
    literal_data = SUPPORTED_LITERALS[literal]
    symbol = literal_data['symbol']
    supported_scope_names = reduce(lambda acc, x: acc + x['scopes'], SUPPORTED_LITERALS.values(), [])

    selection = view.sel()

    for sel_region in selection:
        sel_begin = sel_region.begin()
        sel_end = sel_region.end()
        scope_name = view.scope_name(sel_begin)
        if sel_region.empty():
            scope_region = view.extract_scope(sel_begin)
            if is_any_included_in_scope_name(scope_name, supported_scope_names):
                wrap_replace_inside(view, edit, scope_region, symbol)
            else:
                wrap_insert(view, edit, scope_region, symbol)
            continue

        current_literal = next(filter(
            lambda x: is_any_included_in_scope_name(scope_name, SUPPORTED_LITERALS[x]['scopes']),
            SUPPORTED_LITERALS.keys()
        ))
        current_literal_data = SUPPORTED_LITERALS[current_literal]
        current_quote_symbol = current_literal_data['symbol']
        if view.substr(sel_begin - 1) == current_quote_symbol and view.substr(sel_end) == current_quote_symbol:
            wrap_replace_outside(view, edit, sel_region, symbol)
        elif view.substr(sel_begin) == current_quote_symbol and view.substr(sel_end - 1) == current_quote_symbol:
            wrap_replace_inside(view, edit, sel_region, symbol)
        else:
            wrap_insert(view, edit, sel_region, symbol)

class ConvertSelectionToTemplatePlaceholderCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        selection = self.view.sel()
        new_regions = []

        for region in selection:
            if region.empty():
                continue

            if not is_supported_template_scope(self.view.scope_name(region.begin())):
                continue

            value = self.view.substr(region)
            region_lenght = region.end() - region.begin()
            self.view.replace(edit, region, '${'+value+'}')
            new_region_start = region.begin() + 2
            new_region_end = new_region_start + region_lenght
            new_region = sublime.Region(new_region_start, new_region_end)
            new_regions.append(new_region)

        selection.clear()
        selection.add_all(new_regions)

class InsertTemplatePlaceholderCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        selection = self.view.sel()
        new_regions = []

        for region in selection:
            if not is_supported_template_scope(self.view.scope_name(region.begin())):
                continue

            self.view.insert(edit, region.begin(), '${}')
            new_region_start = region.begin() + 2
            new_region = sublime.Region(new_region_start, new_region_start)
            new_regions.append(new_region)

        selection.clear()
        selection.add_all(new_regions)

class ConvertIntoTemplateLiteralCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        convert_into_literal('template', self.view, edit)

class ConvertIntoSingleQuotedStringLiteralCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        convert_into_literal('single_quoted_string', self.view, edit)

class ConvertIntoDoubleQuotedStringLiteralCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        convert_into_literal('double_quoted_string', self.view, edit)
