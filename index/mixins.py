class MenuLinkMixin(object):
    """
    mixin utiliazado para mantener la clase css 'active' al item activo en el menu principal
    @user_context_var es usado en las CBV para no tener q tipear 'menu_link_active' en el contexto
    """
    menu_link_active = 'home'
    use_context_var = 'menu_link_active'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_link_active'] = self.menu_link_active
        return context
