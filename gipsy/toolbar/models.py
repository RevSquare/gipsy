from ..models import GipsyMenu


class GipsyToolbarMenu(GipsyMenu):
    @property
    def children(self):
        return GipsyToolbarMenu.objects.filter(parent=self.pk)
