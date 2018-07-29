import sublime
import sublime_plugin

class ConvertSelectionToTemplatePlaceholderCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        selection = self.view.sel()
        new_regions = []

        for region in selection:
            if region.empty():
                continue

            scopes = self.view.scope_name(region.begin()).split(' ')
            if 'string.template.js' not in scopes:
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
            scopes = self.view.scope_name(region.begin()).split(' ')
            if 'string.template.js' not in scopes:
                continue

            self.view.insert(edit, region.begin(), '${}')
            new_region_start = region.begin() + 2
            new_region = sublime.Region(new_region_start, new_region_start)
            new_regions.append(new_region)

        selection.clear()
        selection.add_all(new_regions)
