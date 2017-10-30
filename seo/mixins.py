class SeoMeta(object):
    meta_keywords = "comma, separate, values"  # deprecated by google
    meta_description = "General description of the site here"  # about 150 chars
    title = ""  # about 55 chars

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['meta_keywords'] = self.meta_keywords
        context['meta_description'] = self.meta_description
        context['title'] = self.title
        return context
