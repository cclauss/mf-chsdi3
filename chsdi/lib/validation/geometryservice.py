# -*- coding: utf-8 -*-


from pyramid.httpexceptions import HTTPBadRequest

from chsdi.lib.validation import MapNameValidation
from chsdi.esrigeojsonencoder import loads


class GeometryServiceValidation(MapNameValidation):

    def __init__(self):
        super(GeometryServiceValidation, self).__init__()
        self._geometry = None
        self._geometryType = None
        self._returnGeometry = None
        self._layers = None
        self._groupby = None
        self._chargeable = None
        self.esriGeometryTypes = (
            'esriGeometryPolygon',
            'esriGeometryEnvelope'
        )

    @property
    def geometry(self):
        return self._geometry

    @property
    def geometryType(self):
        return self._geometryType

    @property
    def layers(self):
        return self._layers

    @property
    def groupby(self):
        return self._groupby

    @property
    def chargeable(self):
        return self._chargeable

    @geometry.setter
    def geometry(self, value):
        if value is None:
            raise HTTPBadRequest('Please provide the parameter geometry  (Required)')
        else:
            try:
                self._geometry = loads(value)
            except ValueError:
                raise HTTPBadRequest('Please provide a valid geometry')

    @geometryType.setter
    def geometryType(self, value):
        if value is None:
            raise HTTPBadRequest('Please provide the parameter geometryType  (Required)')
        if value not in self.esriGeometryTypes:
            raise HTTPBadRequest('Please provide a valid geometry type. Available: (%s)' % ', '.join(self.esriGeometryTypes))
        self._geometryType = value

    @layers.setter
    def layers(self, value):
        if value is None:
            raise HTTPBadRequest('Please provide a parameter layers')
        if value == 'all':
            self._layers = value
        else:
            try:
                layers = value.split(':')[1]
                self._layers = layers.split(',')
            except:
                HTTPBadRequest('There is an error in the parameter layers')

    @groupby.setter
    def groupby(self, value):
        if value is not None:
            self._groupby = value.split(',')

    @chargeable.setter
    def chargeable(self, value):
        if value is not None:
            if value.lower() == 'true':
                self._chargeable = True
            elif value.lower() == 'false':
                self._chargeable = False
