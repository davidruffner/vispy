# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) 2015, Vispy Development Team. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------
import numpy as np

from .widget import Widget
from ...visuals import ColorBarVisual


class ColorBarWidget(Widget):
    """Widget containing a ColorBar

    Parameters
    ----------
    **kwargs : dict
        Keyword arguments to pass to ColorBarVisual.
    """
    def __init__(self, **kwargs):
        self._colorbar = ColorBarVisual(**kwargs)
        Widget.__init__(self)
        self.add_subvisual(self._colorbar)
        self._set_pos()

    def on_resize(self, event):
        """Resize event handler

        Parameters
        ----------
        event : instance of Event
            The event.
        """
        self._set_pos()

    def _set_pos(self):
        self._colorbar.center_pos = self.rect.center

    @property
    def cmap(self):
        return self._colorbar.cmap

    @cmap.setter
    def cmap(self, cmap):
        self._colorbar.cmap = cmap

    @property
    def halfdim(self):
        return self._colorbar.halfdim

    @halfdim.setter
    def halfdim(self, halfdim):
        self._colorbar.halfdim = halfdim

    @property
    def label(self):
        return self._colorbar.label

    @label.setter
    def label(self, label):
        self._colorbar.label = label

    @property
    def clim(self):
        return self._colorbar.clim

    @clim.setter
    def clim(self, clim):
        self._colorbar.clim = clim
