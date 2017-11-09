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


class ModelMetaView(object):
    """
    Push metadata in the context using as_meta method.
    as_meta method es del pkg django-meta y se agrega a los modelos q implementan el dict _metadata
    """
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['meta'] = self.get_object().as_meta(self.request)
        return context
