# -*- coding: utf-8 -*-

from sqlalchemy import Column, Text
from sqlalchemy.types import Numeric, Boolean, Integer
from geoalchemy2.types import Geometry

from chsdi.models import register, bases
from chsdi.models.vector import Vector


Base = bases['stopo']


class GeologieGeomorphologie (Base, Vector):
    __tablename__ = 'geomorphologie'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/geologie-geomorphologie.mako'
    __bodId__ = 'ch.swisstopo.geologie-geomorphologie'
    __label__ = 'ads_name'
    id = Column('bgdi_id', Integer, primary_key=True)
    ads_name = Column('ads_name', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-geomorphologie', GeologieGeomorphologie)


class DosisleistungTerrestrisch (Base, Vector):
    __tablename__ = 'dosisleistung_terrestrisch'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/dosisleistung_terrestrisch.mako'
    __bodId__ = 'ch.swisstopo.geologie-dosisleistung-terrestrisch'
    __queryable_attributes__ = ['contour']
    __label__ = 'contour'
    id = Column('bgdi_id', Integer, primary_key=True)
    contour = Column('contour', Numeric)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-dosisleistung-terrestrisch', DosisleistungTerrestrisch)


class GravimetrischerAtlasMetadata (Base, Vector):
    __tablename__ = 'gravimetrie_atlas_metadata'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/gravimetrischer_atlas_metadata.mako'
    __bodId__ = 'ch.swisstopo.geologie-gravimetrischer_atlas.metadata'
    __queryable_attributes__ = ['id', 'titel']
    __label__ = 'titel'
    id = Column('nr', Integer, primary_key=True)
    titel = Column('titel', Text)
    jahr = Column('jahr', Numeric)
    autor = Column('autor', Text)
    formate_de = Column('formate_de', Text)
    formate_fr = Column('formate_fr', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-gravimetrischer_atlas.metadata', GravimetrischerAtlasMetadata)


class Landesschwerenetz (Base, Vector):
    __tablename__ = 'landesschwerenetz'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/landesschwerenetz.mako'
    __bodId__ = 'ch.swisstopo.landesschwerenetz'
    __queryable_attributes__ = ['nr_lsn2004', 'name', 'type']
    __label__ = 'label_tt'
    id = Column('bgdi_id', Integer, primary_key=True)
    nr_lsn2004 = Column('nr_lsn2004', Text)
    name = Column('name', Text)
    label_tt = Column('label', Text)
    type = Column('type', Text)
    lat_etrs = Column('lat_etrs', Numeric)
    lon_etrs = Column('lon_etrs', Numeric)
    y_lv03 = Column('y_lv03', Numeric)
    x_lv03 = Column('x_lv03', Numeric)
    h_ln02 = Column('h_ln02', Numeric)
    gravity = Column('gravity', Numeric)
    rms = Column('rms', Numeric)
    vert_grad = Column('vert_grad', Numeric)
    link_hfp_title = Column('link_hfp_title', Text)
    link_hfp_url = Column('link_hfp_url', Text)
    link_lfp_title = Column('link_lfp_title', Text)
    link_lfp_url = Column('link_lfp_url', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.landesschwerenetz', Landesschwerenetz)


class Landesschwerenetz_Ext (Base, Vector):
    __tablename__ = 'landesschwerenetz_exz'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/landesschwerenetz.mako'
    __bodId__ = 'ch.swisstopo.landesschwerenetz'
    __queryable_attributes__ = ['nr_lsn2004', 'name', 'type']
    __maxscale__ = 3000
    __label__ = 'label_tt'
    id = Column('bgdi_id', Integer, primary_key=True)
    nr_lsn2004 = Column('nr_lsn2004', Text)
    name = Column('name', Text)
    label_tt = Column('label', Text)
    type = Column('type', Text)
    lat_etrs = Column('lat_etrs', Numeric)
    lon_etrs = Column('lon_etrs', Numeric)
    y_lv03 = Column('y_lv03', Numeric)
    x_lv03 = Column('x_lv03', Numeric)
    h_ln02 = Column('h_ln02', Numeric)
    gravity = Column('gravity', Numeric)
    rms = Column('rms', Numeric)
    vert_grad = Column('vert_grad', Numeric)
    link_hfp_title = Column('link_hfp_title', Text)
    link_hfp_url = Column('link_hfp_url', Text)
    link_lfp_title = Column('link_lfp_title', Text)
    link_lfp_url = Column('link_lfp_url', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.landesschwerenetz', Landesschwerenetz_Ext)


class GravimetrischerAtlasMesspunkte (Base, Vector):
    __tablename__ = 'gravimetrisch_messpunkte'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/gravimetrischer_atlas_messpunkte.mako'
    __bodId__ = 'ch.swisstopo.geologie-gravimetrischer_atlas.messpunkte'
    __queryable_attributes__ = ['stationnam']
    __label__ = 'stationnam'
    id = Column('bgdi_id', Integer, primary_key=True)
    stationnam = Column('stationnam', Text)
    coordhor = Column('coordhor', Numeric)
    coordver = Column('coordver', Numeric)
    altitude = Column('altitude', Numeric)
    bouguerano = Column('bouguerano', Numeric)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-gravimetrischer_atlas.messpunkte', GravimetrischerAtlasMesspunkte)


class GeologieGeowege (Base, Vector):
    __tablename__ = 'geowege'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/geologie_geowege.mako'
    __bodId__ = 'ch.swisstopo.geologie-geowege'
    id = Column('bgdi_id', Integer, primary_key=True)
    titel_1 = Column('titel_1', Text)
    titel_2 = Column('titel_2', Text)
    link = Column('link', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-geowege', GeologieGeowege)


class GeolSpezialKartenMetadata (Base, Vector):
    __tablename__ = 'kv_gsk_all'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/gsk_metadata.mako'
    __bodId__ = 'ch.swisstopo.geologie-spezialkarten_schweiz.metadata'
    __label__ = 'id'
    id = Column('nr', Integer, primary_key=True)
    titel = Column('titel', Text)
    jahr = Column('jahr', Numeric)
    author = Column('author', Text)
    format_kz = Column('format_kz', Text)
    massstab = Column('massstab', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-spezialkarten_schweiz.metadata', GeolSpezialKartenMetadata)


class SkitourenkarteMetadata(Base, Vector):
    __tablename__ = 'view_gridstand_lkski'
    __table_args__ = ({'schema': 'datenstand', 'autoload': False})
    __template__ = 'templates/htmlpopup/skitouren_metadata.mako'
    __bodId__ = 'ch.swisstopo.skitourenkarte-50.metadata'
    __label__ = 'id'
    id = Column('lknr', Text, primary_key=True)
    name = Column('name', Text)
    legendecms2007 = Column('letzte_publikation', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.skitourenkarte-50.metadata', SkitourenkarteMetadata)


class ShopProductGroupClass:
    __template__ = 'templates/htmlpopup/shop_product_group.mako'
    __label__ = 'number'
    __queryable_attributes__ = ['number', 'name', 'release']
    id = Column('pk_product', Text, primary_key=True)
    number = Column('s_map_number', Text)
    name = Column('s_title_de', Text)
    scale = Column('scale', Integer)
    price = Column('price', Integer)
    release = Column('release', Integer)
    available = Column('available', Boolean)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))


class Landeskarte25Metadata (Base, ShopProductGroupClass, Vector):
    __table_args__ = ({'schema': 'datenstand', 'autoload': False})
    __tablename__ = 'view_gridstand_lk25_shop'
    __bodId__ = 'ch.swisstopo.lk25-papierkarte.metadata'

register('ch.swisstopo.lk25-papierkarte.metadata', Landeskarte25Metadata)


class Landeskarte25zusMetadata (Base, ShopProductGroupClass, Vector):
    __table_args__ = ({'schema': 'datenstand', 'autoload': False})
    __tablename__ = 'view_gridstand_lk25zus_shop'
    __bodId__ = 'ch.swisstopo.lk25-papierkarte-zusammensetzung.metadata'

register('ch.swisstopo.lk25-papierkarte-zusammensetzung.metadata', Landeskarte25zusMetadata)


class Landeskarte50Metadata (Base, ShopProductGroupClass, Vector):
    __table_args__ = ({'schema': 'datenstand', 'autoload': False})
    __tablename__ = 'view_gridstand_lk50_shop'
    __bodId__ = 'ch.swisstopo.lk50-papierkarte.metadata'

register('ch.swisstopo.lk50-papierkarte.metadata', Landeskarte50Metadata)


class Landeskarte50zusMetadata (Base, ShopProductGroupClass, Vector):
    __table_args__ = ({'schema': 'datenstand', 'autoload': False})
    __tablename__ = 'view_gridstand_lk50zus_shop'
    __bodId__ = 'ch.swisstopo.lk50-papierkarte-zusammensetzung.metadata'

register('ch.swisstopo.lk50-papierkarte-zusammensetzung.metadata', Landeskarte50zusMetadata)


class Scale100Metadata (Base, ShopProductGroupClass, Vector):
    __tablename__ = 'view_gridstand_lk100_shop'
    __table_args__ = ({'schema': 'datenstand', 'autoload': False})


class Landeskarte100Metadata (Scale100Metadata):
    __bodId__ = 'ch.swisstopo.lk100-papierkarte.metadata'

register('ch.swisstopo.lk100-papierkarte.metadata', Landeskarte100Metadata)


class Luftfahrt100Metadata (Scale100Metadata):
    __bodId__ = 'ch.swisstopo.lhk100-papierkarte.metadata'

register('ch.swisstopo.lhk100-papierkarte.metadata', Luftfahrt100Metadata)


class Landeskarte100zusMetadata (Base, ShopProductGroupClass, Vector):
    __table_args__ = ({'schema': 'datenstand', 'autoload': False})
    __tablename__ = 'view_gridstand_lk100zus_shop'
    __bodId__ = 'ch.swisstopo.lk100-papierkarte-zusammensetzung.metadata'

register('ch.swisstopo.lk100-papierkarte-zusammensetzung.metadata', Landeskarte100zusMetadata)


class Landeskarte200Metadata (Base, ShopProductGroupClass, Vector):
    __table_args__ = ({'schema': 'datenstand', 'autoload': False})
    __tablename__ = 'view_gridstand_lk200_shop'
    __bodId__ = 'ch.swisstopo.lk200-papierkarte.metadata'

register('ch.swisstopo.lk200-papierkarte.metadata', Landeskarte200Metadata)


class Wanderkarte50Metadata (Base, ShopProductGroupClass, Vector):
    __table_args__ = ({'schema': 'datenstand', 'autoload': False})
    __tablename__ = 'view_gridstand_lkwander50_shop'
    __bodId__ = 'ch.swisstopo.wk50-papierkarte.metadata'

register('ch.swisstopo.wk50-papierkarte.metadata', Wanderkarte50Metadata)


class WanderkarteT33Metadata (Base, ShopProductGroupClass, Vector):
    __table_args__ = ({'schema': 'datenstand', 'autoload': False})
    __tablename__ = 'view_gridstand_wkt33_shop'
    __bodId__ = 'ch.swisstopo.wkt33-papierkarte.metadata'

register('ch.swisstopo.wkt33-papierkarte.metadata', WanderkarteT33Metadata)


class Wanderkarte50zusMetadata (Base, ShopProductGroupClass, Vector):
    __table_args__ = ({'schema': 'datenstand', 'autoload': False})
    __tablename__ = 'view_gridstand_lkwander50zus_shop'
    __bodId__ = 'ch.swisstopo.wk50-papierkarte-zusammensetzung.metadata'

register('ch.swisstopo.wk50-papierkarte-zusammensetzung.metadata', Wanderkarte50zusMetadata)


class Wanderkarte25zusMetadata (Base, ShopProductGroupClass, Vector):
    __table_args__ = ({'schema': 'datenstand', 'autoload': False})
    __tablename__ = 'view_gridstand_lkwander25zus_shop'
    __bodId__ = 'ch.swisstopo.wk25-papierkarte-zusammensetzung.metadata'

register('ch.swisstopo.wk25-papierkarte-zusammensetzung.metadata', Wanderkarte25zusMetadata)


class BurgenKarte200Metadata (Base, ShopProductGroupClass, Vector):
    __table_args__ = ({'schema': 'datenstand', 'autoload': False})
    __tablename__ = 'view_gridstand_bk200'
    __bodId__ = 'ch.swisstopo.bk200-papierkarte.metadata'

register('ch.swisstopo.bk200-papierkarte.metadata', BurgenKarte200Metadata)


class GeolAtlasMetadata (Base, ShopProductGroupClass, Vector):
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __tablename__ = 'view_gridstand_gas25'
    __bodId__ = 'ch.swisstopo.gas25-papierkarte.metadata'

register('ch.swisstopo.gas25-papierkarte.metadata', GeolAtlasMetadata)


class GeolSpezialKarteMetadata (Base, ShopProductGroupClass, Vector):
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __tablename__ = 'view_gridstand_gsk'
    __bodId__ = 'ch.swisstopo.gsk-papierkarte.metadata'

register('ch.swisstopo.gsk-papierkarte.metadata', GeolSpezialKarteMetadata)


class GeolGeneralKarteMetadata (Base, ShopProductGroupClass, Vector):
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __tablename__ = 'view_gridstand_ggk'
    __bodId__ = 'ch.swisstopo.ggk200-papierkarte.metadata'

register('ch.swisstopo.ggk200-papierkarte.metadata', GeolGeneralKarteMetadata)


class ShopProductClass:
    __template__ = 'templates/htmlpopup/shop_product.mako'
    __label__ = 'id'
    __queryable_attributes__ = ['release']
    id = Column('pk_product', Text, primary_key=True)
    scale = Column('scale', Integer)
    price = Column('price', Integer)
    release = Column('release', Integer)
    available = Column('available', Boolean)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))


class Generalkarte300Metadata (Base, ShopProductClass, Vector):
    __table_args__ = ({'schema': 'datenstand', 'autoload': False})
    __tablename__ = 'view_gridstand_gk300'
    __bodId__ = 'ch.swisstopo.gk300-papierkarte.metadata'

register('ch.swisstopo.gk300-papierkarte.metadata', Generalkarte300Metadata)


class Landeskarte500Metadata (Base, ShopProductClass, Vector):
    __table_args__ = ({'schema': 'datenstand', 'autoload': False})
    __tablename__ = 'view_gridstand_lk500'
    __bodId__ = 'ch.swisstopo.lk500-papierkarte.metadata'

register('ch.swisstopo.lk500-papierkarte.metadata', Landeskarte500Metadata)


class Landeskarte1000Metadata (Base, ShopProductClass, Vector):
    __table_args__ = ({'schema': 'datenstand', 'autoload': False})
    __tablename__ = 'view_gridstand_lk1000'
    __bodId__ = 'ch.swisstopo.lk1000-papierkarte.metadata'

register('ch.swisstopo.lk1000-papierkarte.metadata', Landeskarte1000Metadata)


class SegelFlug300Metadata (Base, ShopProductClass, Vector):
    __table_args__ = ({'schema': 'datenstand', 'autoload': False})
    __tablename__ = 'view_gridstand_sfk300'
    __bodId__ = 'ch.swisstopo.sfk300-papierkarte.metadata'

register('ch.swisstopo.sfk300-papierkarte.metadata', SegelFlug300Metadata)


class StrassenKarte200Metadata (Base, ShopProductClass, Vector):
    __table_args__ = ({'schema': 'datenstand', 'autoload': False})
    __tablename__ = 'view_gridstand_stk200'
    __bodId__ = 'ch.swisstopo.stk200-papierkarte.metadata'

register('ch.swisstopo.stk200-papierkarte.metadata', StrassenKarte200Metadata)


class Area250Metadata (Base, ShopProductClass, Vector):
    __table_args__ = ({'schema': 'datenstand', 'autoload': False})
    __tablename__ = 'view_gridstand_area250'
    __bodId__ = 'ch.swisstopo.area-papierkarte.metadata'

register('ch.swisstopo.area-papierkarte.metadata', Area250Metadata)


class GeolKarte500Metadata (Base, ShopProductClass, Vector):
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __tablename__ = 'view_gridstand_gkg500'
    __bodId__ = 'ch.swisstopo.gkg500-papierkarte.metadata'

register('ch.swisstopo.gkg500-papierkarte.metadata', GeolKarte500Metadata)


class TektonischeKarte500Metadata (Base, ShopProductClass, Vector):
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __tablename__ = 'view_gridstand_gkt500'
    __bodId__ = 'ch.swisstopo.gkt500-papierkarte.metadata'

register('ch.swisstopo.gkt500-papierkarte.metadata', TektonischeKarte500Metadata)


class SchwereKarte500Metadata (Base, ShopProductClass, Vector):
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __tablename__ = 'view_gridstand_gkba500'
    __bodId__ = 'ch.swisstopo.gkba500-papierkarte.metadata'

register('ch.swisstopo.gkba500-papierkarte.metadata', SchwereKarte500Metadata)


class Icao500Metadata (Base, ShopProductClass, Vector):
    __table_args__ = ({'schema': 'datenstand', 'autoload': False})
    __tablename__ = 'view_gridstand_icao500'
    __bodId__ = 'ch.swisstopo.icao-papierkarte.metadata'

register('ch.swisstopo.icao-papierkarte.metadata', Icao500Metadata)


class GrundwasserVulnerabilitaetMetadata (Base, ShopProductClass, Vector):
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __tablename__ = 'view_gridstand_gkwvul500'
    __bodId__ = 'ch.swisstopo.gkwvul500-papierkarte.metadata'

register('ch.swisstopo.gkwvul500-papierkarte.metadata', GrundwasserVulnerabilitaetMetadata)


class GrundWasserVorkommenMetadata (Base, ShopProductClass, Vector):
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __tablename__ = 'view_gridstand_gkwvor500'
    __bodId__ = 'ch.swisstopo.gkwvor500-papierkarte.metadata'

register('ch.swisstopo.gkwvor500-papierkarte.metadata', GrundWasserVorkommenMetadata)


class LetztEisMaxMetadata (Base, ShopProductClass, Vector):
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __tablename__ = 'view_gridstand_gklgm500'
    __bodId__ = 'ch.swisstopo.gklgm500-papierkarte.metadata'

register('ch.swisstopo.gklgm500-papierkarte.metadata', LetztEisMaxMetadata)


class SwissboundariesBezirk(Base, Vector):
    __tablename__ = 'swissboundaries_bezirke'
    __table_args__ = ({'schema': 'tlm', 'autoload': False})
    __template__ = 'templates/htmlpopup/swissboundaries_bezirk.mako'
    __bodId__ = 'ch.swisstopo.swissboundaries3d-bezirk-flaeche.fill'
    __queryable_attributes__ = ['name']
    __label__ = 'name'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', Text)
    flaeche = Column('flaeche', Numeric)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.swissboundaries3d-bezirk-flaeche.fill', SwissboundariesBezirk)


class SwissboundariesGemeinde(Base, Vector):
    __tablename__ = 'swissboundaries_gemeinden'
    __table_args__ = ({'schema': 'tlm', 'autoload': False})
    __template__ = 'templates/htmlpopup/swissboundaries_gemeinde.mako'
    __bodId__ = 'ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill'
    __queryable_attributes__ = ['gemname', 'id']
    __label__ = 'gemname'
    id = Column('id', Integer, primary_key=True)
    gemname = Column('gemname', Text)
    gemflaeche = Column('gemflaeche', Numeric)
    perimeter = Column('perimeter', Numeric)
    kanton = Column('kanton', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.swissboundaries3d-gemeinde-flaeche.fill', SwissboundariesGemeinde)


class SwissboundariesKanton(Base, Vector):
    __tablename__ = 'swissboundaries_kantone'
    __table_args__ = ({'schema': 'tlm', 'autoload': False})
    __template__ = 'templates/htmlpopup/swissboundaries_kanton.mako'
    __bodId__ = 'ch.swisstopo.swissboundaries3d-kanton-flaeche.fill'
    __queryable_attributes__ = ['id', 'ak', 'name']
    __label__ = 'name'
    id = Column('kantonsnr', Integer, primary_key=True)
    ak = Column('ak', Text)
    name = Column('name', Text)
    flaeche = Column('flaeche', Numeric)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.swissboundaries3d-kanton-flaeche.fill', SwissboundariesKanton)


class CadastralWebMap(Base, Vector):
    __tablename__ = 'swissboundaries_kantone'
    __table_args__ = ({'schema': 'tlm', 'autoload': False, 'extend_existing': True})
    __template__ = 'templates/htmlpopup/cadastralwebmap.mako'
    __bodId__ = 'ch.kantone.cadastralwebmap-farbe'
    __label__ = 'ak'
    id = Column('kantonsnr', Integer, primary_key=True)
    ak = Column('ak', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.kantone.cadastralwebmap-farbe', CadastralWebMap)


class Vec200Terminal(Base, Vector):
    __tablename__ = 'vec200_terminal'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/vec200_terminal.mako'
    __bodId__ = 'ch.swisstopo.vec200-transportation-oeffentliche-verkehr'
    __label__ = 'objval'
    id = Column('gtdboid', Text, primary_key=True)
    objval = Column('objval', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))


class Vec200ShipKursschiff(Base, Vector):
    __tablename__ = 'v200_ship_kursschiff_linie_tooltip'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/vec200_ship_kursschiff_linie.mako'
    __bodId__ = 'ch.swisstopo.vec200-transportation-oeffentliche-verkehr'
    __label__ = 'objval'
    id = Column('gtdboid', Text, primary_key=True)
    objval = Column('objval', Text)
    detn = Column('detn', Text)
    rsu = Column('rsu', Text)
    use = Column('use', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))


class Vec200Railway(Base, Vector):
    __tablename__ = 'vec200_railway'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/vec200_railway.mako'
    __bodId__ = 'ch.swisstopo.vec200-transportation-oeffentliche-verkehr'
    __label__ = 'objval'
    id = Column('gtdboid', Text, primary_key=True)
    objval = Column('objval', Text)
    construct = Column('construct', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.vec200-transportation-oeffentliche-verkehr', Vec200Terminal)
register('ch.swisstopo.vec200-transportation-oeffentliche-verkehr', Vec200ShipKursschiff)
register('ch.swisstopo.vec200-transportation-oeffentliche-verkehr', Vec200Railway)


class treasurehunt(Base, Vector):
    __tablename__ = 'treasurehunt'
    __table_args__ = ({'schema': 'public', 'autoload': False})
    __template__ = 'templates/htmlpopup/treasurehunt.mako'
    __maxscale__ = 2505
    __bodId__ = 'ch.swisstopo.treasurehunt'
    # Translatable labels in fr,it
    __label__ = 'title_de'
    id = Column('bgdi_id', Integer, primary_key=True)
    title_de = Column('title_de', Text)
    title_fr = Column('title_fr', Text)
    title_it = Column('title_it', Text)
    info_de = Column('info_de', Text)
    info_fr = Column('info_fr', Text)
    info_it = Column('info_it', Text)
    link_de = Column('link_de', Text)
    link_fr = Column('link_fr', Text)
    link_it = Column('link_it', Text)
    type_coord = Column('type_coord', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.treasurehunt', treasurehunt)


class Vec200Trafficinfo(Base, Vector):
    __tablename__ = 'vec200_trafficinfo'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/vec200_trafficinfo.mako'
    __bodId__ = 'ch.swisstopo.vec200-transportation-strassennetz'
    __label__ = 'objname'
    id = Column('gtdboid', Text, primary_key=True)
    objname = Column('objname', Text)
    objval = Column('objval', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))


class Vec200ShipAutofaehre(Base, Vector):
    __tablename__ = 'v200_ship_autofaehre_tooltip'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/vec200_ship_autofaehre.mako'
    __bodId__ = 'ch.swisstopo.vec200-transportation-strassennetz'
    __label__ = 'detn'
    id = Column('gtdboid', Text, primary_key=True)
    use = Column('use', Text)
    rsu = Column('rsu', Text)
    detn = Column('detn', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))


class Vec200Road(Base, Vector):
    __tablename__ = 'vec200_road'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/vec200_road.mako'
    __bodId__ = 'ch.swisstopo.vec200-transportation-strassennetz'
    __label__ = 'objval'
    id = Column('gtdboid', Text, primary_key=True)
    construct = Column('construct', Text)
    objval = Column('objval', Text)
    toll = Column('toll', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))


class Vec200Ramp(Base, Vector):
    __tablename__ = 'vec200_ramp'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/vec200_ramp.mako'
    __bodId__ = 'ch.swisstopo.vec200-transportation-strassennetz'
    __label__ = 'objval'
    id = Column('gtdboid', Text, primary_key=True)
    construct = Column('construct', Text)
    objval = Column('objval', Text)
    toll = Column('toll', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))


class Vec200Customsoffice(Base, Vector):
    __tablename__ = 'vec200_customsoffice'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/vec200_customsoffice.mako'
    __bodId__ = 'ch.swisstopo.vec200-transportation-strassennetz'
    __label__ = 'ojbname'
    id = Column('gtdboid', Text, primary_key=True)
    objname = Column('objname', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.vec200-transportation-strassennetz', Vec200Trafficinfo)
register('ch.swisstopo.vec200-transportation-strassennetz', Vec200ShipAutofaehre)
register('ch.swisstopo.vec200-transportation-strassennetz', Vec200Road)
register('ch.swisstopo.vec200-transportation-strassennetz', Vec200Ramp)
register('ch.swisstopo.vec200-transportation-strassennetz', Vec200Customsoffice)


class Vec200Protectedarea(Base, Vector):
    __tablename__ = 'vec200_protectedarea'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/vec200_protectedarea.mako'
    __bodId__ = 'ch.swisstopo.vec200-adminboundaries-protectedarea'
    __label__ = 'name'
    id = Column('gtdboid', Text, primary_key=True)
    name = Column('name', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.vec200-adminboundaries-protectedarea', Vec200Protectedarea)


class Vec200Flowingwater(Base, Vector):
    __tablename__ = 'vec200_flowingwater'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/vec200_flowingwater.mako'
    __bodId__ = 'ch.swisstopo.vec200-hydrography'
    __label__ = 'name'
    id = Column('gtdboid', Text, primary_key=True)
    name = Column('name', Text)
    exs = Column('exs', Text)
    hoc = Column('hoc', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))


class Vec200Stagnantwater(Base, Vector):
    __tablename__ = 'vec200_stagnantwater'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/vec200_stagnantwater.mako'
    __bodId__ = 'ch.swisstopo.vec200-hydrography'
    __label__ = 'name'
    id = Column('gtdboid', Text, primary_key=True)
    name = Column('name', Text)
    seesph = Column('seesph', Numeric)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.vec200-hydrography', Vec200Flowingwater)
register('ch.swisstopo.vec200-hydrography', Vec200Stagnantwater)


class Vec200Landcover(Base, Vector):
    __tablename__ = 'vec200_landcover'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/vec200_landcover.mako'
    __bodId__ = 'ch.swisstopo.vec200-landcover'
    __label__ = 'objname1'
    id = Column('gtdboid', Text, primary_key=True)
    objname1 = Column('objname1', Text)
    objval = Column('objval', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.vec200-landcover', Vec200Landcover)


class Vec200Builtupp(Base, Vector):
    __tablename__ = 'vec200_builtupp'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/vec200_builtupp.mako'
    __bodId__ = 'ch.swisstopo.vec200-miscellaneous'
    __label__ = 'objname'
    id = Column('gtdboid', Text, primary_key=True)
    objname = Column('objname', Text)
    ppi = Column('ppi', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))


class Vec200Poi(Base, Vector):
    __tablename__ = 'v200_poi_tooltip'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/vec200_poi.mako'
    __bodId__ = 'ch.swisstopo.vec200-miscellaneous'
    __label__ = 'objname'
    id = Column('gtdboid', Text, primary_key=True)
    objname = Column('objname', Text)
    objval = Column('objval', Text)
    ppc = Column('ppc', Text)
    pro = Column('pro', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))


class Vec200Supply(Base, Vector):
    __tablename__ = 'vec200_supply'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/vec200_supply.mako'
    __bodId__ = 'ch.swisstopo.vec200-miscellaneous'
    __label__ = 'fco'
    id = Column('gtdboid', Text, primary_key=True)
    fco = Column('fco', Text)
    loc = Column('loc', Text)
    pro = Column('pro', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.vec200-miscellaneous', Vec200Builtupp)
register('ch.swisstopo.vec200-miscellaneous', Vec200Poi)
register('ch.swisstopo.vec200-miscellaneous', Vec200Supply)


class Vec200Namedlocation(Base, Vector):
    __tablename__ = 'vec200_namedlocation'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/vec200_namedlocation.mako'
    __bodId__ = 'ch.swisstopo.vec200-names-namedlocation'
    __queryable_attributes__ = ['objname1', 'id']
    # Composite labels coalesce(objname1,'')||' '||coalesce(objname2,'')
    __label__ = 'objname1'
    id = Column('gtdboid', Text, primary_key=True)
    objname1 = Column('objname1', Text)
    objname2 = Column('objname2', Text)
    altitude = Column('altitude', Integer)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.vec200-names-namedlocation', Vec200Namedlocation)


class Vec25Strassennetz(Base, Vector):
    __tablename__ = 'v25_str_25_l_tooltip'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/vec25_strassennetz.mako'
    __bodId__ = 'ch.swisstopo.vec25-strassennetz'
    __label__ = 'id'
    id = Column('objectid', Integer, primary_key=True)
    length = Column('length', Numeric)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.vec25-strassennetz', Vec25Strassennetz)


class Vec25Uebrige(Base, Vector):
    __tablename__ = 'v25_uvk_25_l'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/vec25_uebrigeverk.mako'
    __bodId__ = 'ch.swisstopo.vec25-uebrigerverkehr'
    __label__ = 'length'
    id = Column('objectid', Integer, primary_key=True)
    length = Column('length', Numeric)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.vec25-uebrigerverkehr', Vec25Uebrige)


class Vec25Anlagen(Base, Vector):
    __tablename__ = 'v25_anl_25_a'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/vec25_anlagen.mako'
    __bodId__ = 'ch.swisstopo.vec25-anlagen'
    __label__ = 'area'
    id = Column('objectid', Integer, primary_key=True)
    area = Column('area', Numeric)
    perimeter = Column('perimeter', Numeric)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.vec25-anlagen', Vec25Anlagen)


class Vec25Eisenbahnnetz(Base, Vector):
    __tablename__ = 'v25_eis_25_l'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/vec25_eisenbahnnetz.mako'
    __bodId__ = 'ch.swisstopo.vec25-eisenbahnnetz'
    __label__ = 'length'
    id = Column('objectid', Integer, primary_key=True)
    length = Column('length', Numeric)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.vec25-eisenbahnnetz', Vec25Eisenbahnnetz)


class Vec25Gebaeude(Base, Vector):
    __tablename__ = 'v25_geb_25_a'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/vec25_gebaeude.mako'
    __bodId__ = 'ch.swisstopo.vec25-gebaeude'
    __label__ = 'area'
    id = Column('objectid', Integer, primary_key=True)
    area = Column('area', Numeric)
    perimeter = Column('perimeter', Numeric)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.vec25-gebaeude', Vec25Gebaeude)


class Vec25Gewaessernetz(Base, Vector):
    __tablename__ = 'v25_gwn_25_l'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/vec25_gewaessernetz.mako'
    __bodId__ = 'ch.swisstopo.vec25-gewaessernetz'
    __label__ = 'name'
    id = Column('objectid', Integer, primary_key=True)
    objectval = Column('objectval', Text)
    gewissnr = Column('gewissnr', Numeric)
    name = Column('name', Text)
    length = Column('length', Numeric)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.vec25-gewaessernetz', Vec25Gewaessernetz)


class Vec25Primaerflaechen(Base, Vector):
    __tablename__ = 'v25_pri25_a'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/vec25_primaerflaechen.mako'
    __bodId__ = 'ch.swisstopo.vec25-primaerflaechen'
    __label__ = 'area'
    id = Column('objectid', Integer, primary_key=True)
    area = Column('area', Numeric)
    perimeter = Column('perimeter', Numeric)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.vec25-primaerflaechen', Vec25Primaerflaechen)


class Vec25Einzelobjekte(Base, Vector):
    __tablename__ = 'v25_eob_25_l'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/vec25_einzelobjekte.mako'
    __bodId__ = 'ch.swisstopo.vec25-einzelobjekte'
    __label__ = 'length'
    id = Column('objectid', Integer, primary_key=True)
    length = Column('length', Numeric)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.vec25-einzelobjekte', Vec25Einzelobjekte)


class Vec25Heckenbaeume(Base, Vector):
    __tablename__ = 'v25_heb_25_l'
    __table_args__ = ({'autoload': False})
    __template__ = 'templates/htmlpopup/vec25_heckenbaeume.mako'
    __bodId__ = 'ch.swisstopo.vec25-heckenbaeume'
    __label__ = 'length'
    id = Column('objectid', Integer, primary_key=True)
    length = Column('length', Numeric)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.vec25-heckenbaeume', Vec25Heckenbaeume)


class Dreiecksvermaschung(Base, Vector):
    __tablename__ = 'dreiecksvermaschung'
    __table_args__ = ({'schema': 'geodaesie', 'autoload': False})
    __template__ = 'templates/htmlpopup/dreiecksvermaschung.mako'
    __bodId__ = 'ch.swisstopo.dreiecksvermaschung'
    __label__ = 'nom'
    id = Column('bgdi_id', Integer, primary_key=True)
    nom = Column('nom', Text)
    num = Column('num', Text)
    type = Column('type', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.dreiecksvermaschung', Dreiecksvermaschung)


class GridstandPk25(Base, Vector):
    __tablename__ = 'view_gridstand_datenhaltung_pk25_tilecache'
    __table_args__ = ({'schema': 'datenstand', 'autoload': False})
    __template__ = 'templates/htmlpopup/pk25_metadata.mako'
    __bodId__ = 'ch.swisstopo.pixelkarte-farbe-pk25.noscale'
    __label__ = 'lk_name'
    id = Column('kbnum', Text, primary_key=True)
    lk_name = Column('lk_name', Text)
    release = Column('release', Integer)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.pixelkarte-farbe-pk25.noscale', GridstandPk25)


class GridstandPk25Meta(GridstandPk25):
    __bodId__ = 'ch.swisstopo.pixelkarte-pk25.metadata'

register('ch.swisstopo.pixelkarte-pk25.metadata', GridstandPk25Meta)


class GridstandPk50(Base, Vector):
    __tablename__ = 'view_gridstand_datenhaltung_pk50_tilecache'
    __table_args__ = ({'schema': 'datenstand', 'autoload': False})
    __template__ = 'templates/htmlpopup/pk50_metadata.mako'
    __bodId__ = 'ch.swisstopo.pixelkarte-farbe-pk50.noscale'
    __label__ = 'lk_name'
    id = Column('kbnum', Text, primary_key=True)
    lk_name = Column('lk_name', Text)
    release = Column('release', Integer)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.pixelkarte-farbe-pk50.noscale', GridstandPk50)


class GridstandPk50Meta(GridstandPk50):
    __bodId__ = 'ch.swisstopo.pixelkarte-pk50.metadata'

register('ch.swisstopo.pixelkarte-pk50.metadata', GridstandPk50Meta)


class GridstandPk100(Base, Vector):
    __tablename__ = 'view_gridstand_datenhaltung_pk100_tilecache'
    __table_args__ = ({'schema': 'datenstand', 'autoload': False})
    __template__ = 'templates/htmlpopup/pk100_metadata.mako'
    __bodId__ = 'ch.swisstopo.pixelkarte-farbe-pk100.noscale'
    __label__ = 'lk_name'
    id = Column('kbnum', Text, primary_key=True)
    lk_name = Column('lk_name', Text)
    release = Column('release', Integer)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.pixelkarte-farbe-pk100.noscale', GridstandPk100)


class GridstandPk100Meta(GridstandPk100):
    __bodId__ = 'ch.swisstopo.pixelkarte-pk100.metadata'

register('ch.swisstopo.pixelkarte-pk100.metadata', GridstandPk100Meta)


class GridstandPk200(Base, Vector):
    __tablename__ = 'view_gridstand_datenhaltung_pk200_tilecache'
    __table_args__ = ({'schema': 'datenstand', 'autoload': False})
    __template__ = 'templates/htmlpopup/pk200_metadata.mako'
    __bodId__ = 'ch.swisstopo.pixelkarte-farbe-pk200.noscale'
    __label__ = 'lk_name'
    id = Column('kbnum', Text, primary_key=True)
    lk_name = Column('lk_name', Text)
    release = Column('release', Integer)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.pixelkarte-farbe-pk200.noscale', GridstandPk200)


class GridstandPk200Meta(GridstandPk200):
    __bodId__ = 'ch.swisstopo.pixelkarte-pk200.metadata'

register('ch.swisstopo.pixelkarte-pk200.metadata', GridstandPk200Meta)


class GridstandPk500(Base, Vector):
    __tablename__ = 'view_gridstand_datenhaltung_pk500_tilecache'
    __table_args__ = ({'schema': 'datenstand', 'autoload': False})
    __template__ = 'templates/htmlpopup/pk500_metadata.mako'
    __bodId__ = 'ch.swisstopo.pixelkarte-farbe-pk500.noscale'
    __label__ = 'lk_name'
    id = Column('kbnum', Text, primary_key=True)
    lk_name = Column('lk_name', Text)
    release = Column('release', Integer)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.pixelkarte-farbe-pk500.noscale', GridstandPk500)


class GridstandPk500Meta(GridstandPk500):
    __bodId__ = 'ch.swisstopo.pixelkarte-pk500.metadata'

register('ch.swisstopo.pixelkarte-pk500.metadata', GridstandPk500Meta)


class GridstandSwissimage(Base, Vector):
    __tablename__ = 'view_gridstand_datenhaltung_swissimage_tilecache'
    __table_args__ = ({'schema': 'datenstand', 'autoload': False})
    __template__ = 'templates/htmlpopup/images_metadata.mako'
    __bodId__ = 'ch.swisstopo.images-swissimage.metadata'
    __label__ = 'lk25_name'
    id = Column('tilenumber', Text, primary_key=True)
    lk25_name = Column('lk25_name', Text)
    datenstand = Column('datenstand', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.images-swissimage.metadata', GridstandSwissimage)


class SwissimageProduct(Base, Vector):
    __tablename__ = 'view_gridstand_datenhaltung_swissimage_tilecache'
    __table_args__ = ({'schema': 'datenstand', 'autoload': False, 'extend_existing': True})
    __template__ = 'templates/htmlpopup/images_metadata.mako'
    __bodId__ = 'ch.swisstopo.swissimage-product'
    __label__ = 'id'
    id = Column('tilenumber', Text, primary_key=True)
    lk25_name = Column('lk25_name', Text)
    datenstand = Column('datenstand', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.swissimage-product', SwissimageProduct)


class GeolGeocoverMetadata(Base, Vector):
    __tablename__ = 'kv_geocover'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/geocover_metadata.mako'
    __bodId__ = 'ch.swisstopo.geologie-geocover.metadata'
    __label__ = 'nr'
    id = Column('gid', Integer, primary_key=True)
    nr = Column('nr', Text)
    titel = Column('titel', Text)
    basis = Column('basis', Text)
    vektorisierung_jahr = Column('vektorisierung_jahr', Integer)
    grat25 = Column('grat25', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-geocover.metadata', GeolGeocoverMetadata)


class GeolGenKarteGGK200(Base, Vector):
    __tablename__ = 'kv_ggk_pk'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/generalkarte_ggk200.mako'
    __bodId__ = 'ch.swisstopo.geologie-generalkarte-ggk200'
    __label__ = 'titel'
    id = Column('gid', Integer, primary_key=True)
    nr = Column('nr', Integer)
    titel = Column('titel', Text)
    url_legend = Column('url_legend', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-generalkarte-ggk200', GeolGenKarteGGK200)


class GeolGenKarteGGK200Meta(Base, Vector):
    __tablename__ = 'kv_ggk_pk'
    __table_args__ = ({'schema': 'geol', 'autoload': False, 'extend_existing': True})
    __template__ = 'templates/htmlpopup/generalkarte_ggk200.metadata.mako'
    __bodId__ = 'ch.swisstopo.geologie-generalkarte-ggk200.metadata'
    __queryable_attributes__ = ['titel', 'jahr', 'author', 'nr']
    __label__ = 'prod_id'
    id = Column('gid', Text, primary_key=True)
    nr = Column('nr', Integer)
    prod_id = Column('prod_id', Text)
    titel = Column('titel', Text)
    autor = Column('autor', Text)
    jahr = Column('jahr', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-generalkarte-ggk200.metadata', GeolGenKarteGGK200Meta)


class GeolKarten500Metadata(Base, Vector):
    __tablename__ = 'gk500'
    __table_args__ = ({'schema': 'public', 'autoload': False})
    __template__ = 'templates/htmlpopup/geolkarten500_metadata.mako'
    __bodId__ = 'ch.swisstopo.geologie-geolkarten500.metadata'
    __label__ = 'id'
    id = Column('bgdi_id', Integer, primary_key=True)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-geolkarten500.metadata', GeolKarten500Metadata)


class GeologischeKarteLine(Base, Vector):
    __tablename__ = 'geologische_karte_line'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/geologische_karte_line.mako'
    __bodId__ = 'ch.swisstopo.geologie-geologische_karte'
    # Translatable labels in fr
    __label__ = 'type_de'
    id = Column('fid', Text, primary_key=True)
    gid = Column('id', Integer)
    type_de = Column('type_de', Text)
    type_fr = Column('type_fr', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))


class GeologischeKartePlg(Base, Vector):
    __tablename__ = 'geologische_karte_plg'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/geologische_karte_plg.mako'
    __bodId__ = 'ch.swisstopo.geologie-geologische_karte'
    __label__ = 'leg_geol_d'
    id = Column('id', Text, primary_key=True)
    leg_geol_d = Column('leg_geol_d', Text)
    leg_geol_f = Column('leg_geol_f', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-geologische_karte', GeologischeKarteLine)
register('ch.swisstopo.geologie-geologische_karte', GeologischeKartePlg)


class GeologieMineralischeRohstoffe200(Base, Vector):
    __tablename__ = 'geotechnik_mineralische_rohstoffe200'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/geotechnik_mineralische_rohstoffe200.mako'
    __bodId__ = 'ch.swisstopo.geologie-geotechnik-mineralische_rohstoffe200'
    __label__ = 'area_name'
    id = Column('bgdi_id', Integer, primary_key=True)
    legend = Column('legend', Text)
    area_name = Column('area_name', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-geotechnik-mineralische_rohstoffe200', GeologieMineralischeRohstoffe200)


class GeologieGeotechnikGk200(Base, Vector):
    __tablename__ = 'geotechnik_gk200_lgd'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/geotechnik_gk200.mako'
    __bodId__ = 'ch.swisstopo.geologie-geotechnik-gk200'
    __label__ = 'file_name'
    id = Column('bgdi_id', Integer, primary_key=True)
    file_name = Column('file_name', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-geotechnik-gk200', GeologieGeotechnikGk200)


class Gk500_Gensese (Base, Vector):
    __tablename__ = 'gk500_genese'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/gk500-genese.mako'
    __bodId__ = 'ch.swisstopo.geologie-geotechnik-gk500-genese'
    # Translatable labels in fr, it, rm, it
    __label__ = 'genese_de'
    id = Column('bgdi_id', Integer, primary_key=True)
    genese_de = Column('genese_de', Text)
    genese_fr = Column('genese_fr', Text)
    genese_en = Column('genese_en', Text)
    genese_it = Column('genese_it', Text)
    genese_rm = Column('genese_rm', Text)
    bgdi_tooltip_color = Column('bgdi_tooltip_color', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-geotechnik-gk500-genese', Gk500_Gensese)


class Gk500_Gesteinsklassierung (Base, Vector):
    __tablename__ = 'gk500_gesteinsklassierung'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/gk500-gesteinsklassierung.mako'
    __bodId__ = 'ch.swisstopo.geologie-geotechnik-gk500-gesteinsklassierung'
    __label__ = 'gestkl_de'
    id = Column('bgdi_id', Integer, primary_key=True)
    # Translatable labels in fr, it, rm, it
    __label__ = 'gestkl_de'
    gestkl_de = Column('gestkl_de', Text)
    gestkl_fr = Column('gestkl_fr', Text)
    gestkl_en = Column('gestkl_en', Text)
    gestkl_it = Column('gestkl_it', Text)
    gestkl_rm = Column('gestkl_rm', Text)
    bgdi_tooltip_color = Column('bgdi_tooltip_color', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-geotechnik-gk500-gesteinsklassierung', Gk500_Gesteinsklassierung)


class Gk500_lithologie_hauptgruppen(Base, Vector):
    __tablename__ = 'gk500_lithologie_hauptgruppen'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/lithologie_hauptgruppen.mako'
    __bodId__ = 'ch.swisstopo.geologie-geotechnik-gk500-lithologie_hauptgruppen'
    # Translatable labels in fr, it, rm, it
    __label__ = 'bgdi_tooltip_de'
    id = Column('bgdi_id', Integer, primary_key=True)
    bgdi_tooltip_de = Column('bgdi_tooltip_de', Text)
    bgdi_tooltip_fr = Column('bgdi_tooltip_fr', Text)
    bgdi_tooltip_en = Column('bgdi_tooltip_en', Text)
    bgdi_tooltip_it = Column('bgdi_tooltip_it', Text)
    bgdi_tooltip_rm = Column('bgdi_tooltip_rm', Text)
    bgdi_tooltip_color = Column('bgdi_tooltip_color', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-geotechnik-gk500-lithologie_hauptgruppen', Gk500_lithologie_hauptgruppen)


class GeologieGeotechnikSteinbrueche1915(Base, Vector):
    __tablename__ = 'geotechnik_steinbrueche_1915'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/steinbrueche_1915.mako'
    __bodId__ = 'ch.swisstopo.geologie-geotechnik-steinbrueche_1915'
    __label__ = 'gesteinsgr'
    id = Column('id', Integer, primary_key=True)
    gesteinsgr = Column('gesteinsgr', Text)
    gestein = Column('gestein', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-geotechnik-steinbrueche_1915', GeologieGeotechnikSteinbrueche1915)


class GeologieGeotechnikSteinbrueche1965(Base, Vector):
    __tablename__ = 'geotechnik_steinbrueche_1965'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/steinbrueche_1965.mako'
    __bodId__ = 'ch.swisstopo.geologie-geotechnik-steinbrueche_1965'
    __label__ = 'gesteinsgr'
    id = Column('id', Integer, primary_key=True)
    gesteinsgr = Column('gesteinsgr', Text)
    gestein = Column('gestein', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-geotechnik-steinbrueche_1965', GeologieGeotechnikSteinbrueche1965)


class GeologieGeotechnikSteinbrueche1980(Base, Vector):
    __tablename__ = 'geotechnik_steinbrueche_1980'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/steinbrueche_1980.mako'
    __bodId__ = 'ch.swisstopo.geologie-geotechnik-steinbrueche_1980'
    __label__ = 'gesteinsgr'
    id = Column('id', Integer, primary_key=True)
    gesteinsgr = Column('gesteinsgr', Text)
    gestein = Column('gestein', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-geotechnik-steinbrueche_1980', GeologieGeotechnikSteinbrueche1980)


class GeologieGeotechnikSteinbrueche1995(Base, Vector):
    __tablename__ = 'geotechnik_steinbrueche_1995'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/steinbrueche_1995.mako'
    __bodId__ = 'ch.swisstopo.geologie-geotechnik-steinbrueche_1995'
    __label__ = 'gesteinsgr'
    id = Column('id', Integer, primary_key=True)
    gesteinsgr = Column('gesteinsgr', Text)
    gestein = Column('gestein', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-geotechnik-steinbrueche_1995', GeologieGeotechnikSteinbrueche1995)


class GeologieGeotechnikZementindustrie1965(Base, Vector):
    __tablename__ = 'geotechnik_zementindustrie'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/zementindustrie_1965.mako'
    __bodId__ = 'ch.swisstopo.geologie-geotechnik-zementindustrie_1965'
    __label__ = 'stoff'
    id = Column('id', Integer, primary_key=True)
    stoff = Column('stoff', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-geotechnik-zementindustrie_1965', GeologieGeotechnikZementindustrie1965)


class GeologieGeotechnikZementindustrie1995(Base, Vector):
    __tablename__ = 'geotechnik_zementindustrie'
    __table_args__ = ({'schema': 'geol', 'autoload': False, 'extend_existing': True})
    __template__ = 'templates/htmlpopup/zementindustrie_1995.mako'
    __bodId__ = 'ch.swisstopo.geologie-geotechnik-zementindustrie_1995'
    __label__ = 'stoff'
    id = Column('id', Integer, primary_key=True)
    stoff = Column('stoff', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-geotechnik-zementindustrie_1995', GeologieGeotechnikZementindustrie1995)


class GeologieGeotechnikZiegeleien1907(Base, Vector):
    __tablename__ = 'geotechnik_ziegeleien_1907'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/ziegeleien_1907.mako'
    __bodId__ = 'ch.swisstopo.geologie-geotechnik-ziegeleien_1907'
    __queryable_attributes__ = ['ziegelei_2']
    __label__ = 'ziegelei_2'
    id = Column('id', Integer, primary_key=True)
    ziegelei_2 = Column('ziegelei_2', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-geotechnik-ziegeleien_1907', GeologieGeotechnikZiegeleien1907)


class GeologieGeotechnikZiegeleien1965(Base, Vector):
    __tablename__ = 'geotechnik_ziegeleien_1965'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/ziegeleien_1965.mako'
    __bodId__ = 'ch.swisstopo.geologie-geotechnik-ziegeleien_1965'
    __queryable_attributes__ = ['ziegelei']
    __label__ = 'ziegelei'
    id = Column('id', Integer, primary_key=True)
    ziegelei = Column('ziegelei', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-geotechnik-ziegeleien_1965', GeologieGeotechnikZiegeleien1965)


class GeologieGeotechnikZiegeleien1995(Base, Vector):
    __tablename__ = 'geotechnik_ziegeleien_1995'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/ziegeleien_1995.mako'
    __bodId__ = 'ch.swisstopo.geologie-geotechnik-ziegeleien_1995'
    __queryable_attributes__ = ['ziegeleien']
    __label__ = 'ziegeleien'
    id = Column('id', Integer, primary_key=True)
    ziegeleien = Column('ziegeleien', Text)
    produkt = Column('produkt', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-geotechnik-ziegeleien_1995', GeologieGeotechnikZiegeleien1995)


class GeologieHydroKarteGrundwasservorkommen(Base, Vector):
    __tablename__ = 'grundwasservorkommen'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/grundwasservorkommen.mako'
    __bodId__ = 'ch.swisstopo.geologie-hydrogeologische_karte-grundwasservorkommen'
    # Translatable labels in fr
    __label__ = 'type_de'
    id = Column('bgdi_id', Integer, primary_key=True)
    type_de = Column('type_de', Text)
    type_fr = Column('type_fr', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-hydrogeologische_karte-grundwasservorkommen', GeologieHydroKarteGrundwasservorkommen)


class GeologieHydroKarteGrundwasservulneabilitaet(Base, Vector):
    __tablename__ = 'grundwasservorkommen_plg'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/grundwasservulnerabilitaet.mako'
    __bodId__ = 'ch.swisstopo.geologie-hydrogeologische_karte-grundwasservulnerabilitaet'
    # Translatable labels in fr
    __label__ = 'type_de'
    id = Column('bgdi_id', Integer, primary_key=True)
    type_de = Column('type_de', Text)
    type_fr = Column('type_fr', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-hydrogeologische_karte-grundwasservulnerabilitaet', GeologieHydroKarteGrundwasservulneabilitaet)


class GeologieGeothermie(Base, Vector):
    __tablename__ = 'geophysik_geothermie'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/geothermie.mako'
    __bodId__ = 'ch.swisstopo.geologie-geophysik-geothermie'
    __label__ = 'contour'
    id = Column('gid', Integer, primary_key=True)
    fid = Column('id', Integer)
    contour = Column('contour', Numeric)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-geophysik-geothermie', GeologieGeothermie)


class Geologischer_Deklination(Base, Vector):
    __tablename__ = 'geophysik_deklination'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/deklination.mako'
    __bodId__ = 'ch.swisstopo.geologie-geophysik-deklination'
    __label__ = 'magne'
    id = Column('gid', Integer, primary_key=True)
    magne = Column('magne', Numeric)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-geophysik-deklination', Geologischer_Deklination)


class Geologischer_Inklination(Base, Vector):
    __tablename__ = 'geophysik_inklination'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/inklination.mako'
    __bodId__ = 'ch.swisstopo.geologie-geophysik-inklination'
    __label__ = 'contour'
    id = Column('gid', Integer, primary_key=True)
    contour = Column('contour', Numeric)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-geophysik-inklination', Geologischer_Inklination)


class Geologischer_Aeromagnetik_Jura(Base, Vector):
    __tablename__ = 'gravimetrie_aeromagnetik_jura'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/aeromagnetik_jura.mako'
    __bodId__ = 'ch.swisstopo.geologie-geophysik-aeromagnetische_karte_jura'
    __label__ = 'et_fromatt'
    id = Column('gid', Integer, primary_key=True)
    fid = Column('id', Integer)
    et_fromatt = Column('et_fromatt', Numeric)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-geophysik-aeromagnetische_karte_jura', Geologischer_Aeromagnetik_Jura)


class Geologischer_Aeromagnetik_CH(Base, Vector):
    __tablename__ = 'gravimetrie_aeromagnetik_ch'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/aeromagnetik_schweiz.mako'
    __bodId__ = 'ch.swisstopo.geologie-geophysik-aeromagnetische_karte_schweiz'
    __label__ = 'fid'
    id = Column('gid', Integer, primary_key=True)
    fid = Column('id', Integer)
    et_fromatt = Column('et_fromatt', Numeric)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-geophysik-aeromagnetische_karte_schweiz', Geologischer_Aeromagnetik_CH)


class GeologieIsostatischeAnomalien(Base, Vector):
    __tablename__ = 'schwerekarte_isostatische_anomalien'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/isostatische_anomalien.mako'
    __bodId__ = 'ch.swisstopo.geologie-geodaesie-isostatische_anomalien'
    __label__ = 'et_fromatt'
    id = Column('gid', Integer, primary_key=True)
    fid = Column('id', Integer)
    et_fromatt = Column('et_fromatt', Numeric)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-geodaesie-isostatische_anomalien', GeologieIsostatischeAnomalien)


class GeologieBouguerAnomalien(Base, Vector):
    __tablename__ = 'geodaesie_bouguer_anomalien'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/bouguer_anomalien.mako'
    __bodId__ = 'ch.swisstopo.geologie-geodaesie-bouguer_anomalien'
    __label__ = 'et_fromatt'
    id = Column('gid', Integer, primary_key=True)
    et_fromatt = Column('et_fromatt', Numeric)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-geodaesie-bouguer_anomalien', GeologieBouguerAnomalien)


class GeologieGeophysikTotalintensitaet(Base, Vector):
    __tablename__ = 'geophysik_totalintensitaet'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/totalintensitaet.mako'
    __bodId__ = 'ch.swisstopo.geologie-geophysik-totalintensitaet'
    __label__ = 'contour'
    id = Column('gid', Integer, primary_key=True)
    fid = Column('id', Integer)
    contour = Column('contour', Numeric)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-geophysik-totalintensitaet', GeologieGeophysikTotalintensitaet)


class GeologieRohstoffeIndustrieminerale(Base, Vector):
    __tablename__ = 'rohstoffe_industrieminerale'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/rohstoffe_industrieminerale.mako'
    __bodId__ = 'ch.swisstopo.geologie-rohstoffe-industrieminerale'
    __queryable_attributes__ = ['name_ads']
    __label__ = 'name_ads'
    id = Column('id', Integer, primary_key=True)
    rohstoff = Column('rohstoff', Text)
    name_ads = Column('name_ads', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-rohstoffe-industrieminerale', GeologieRohstoffeIndustrieminerale)


class GeologieRohstoffeKohlenBitumenErdgas(Base, Vector):
    __tablename__ = 'rohstoffe_kohlen_bitumen_erdgas'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/rohstoffe_kohlen_bitumen_erdgas.mako'
    __bodId__ = 'ch.swisstopo.geologie-rohstoffe-kohlen_bitumen_erdgas'
    __queryable_attributes__ = ['name_ads']
    __label__ = 'name_ads'
    id = Column('id', Integer, primary_key=True)
    rohstoff = Column('rohstoff', Text)
    name_ads = Column('name_ads', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-rohstoffe-kohlen_bitumen_erdgas', GeologieRohstoffeKohlenBitumenErdgas)


class GeologieRohstoffeVererzungen(Base, Vector):
    __tablename__ = 'rohstoffe_vererzungen'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/rohstoffe_vererzungen.mako'
    __bodId__ = 'ch.swisstopo.geologie-rohstoffe-vererzungen'
    __queryable_attributes__ = ['name_ads']
    __label__ = 'name_ads'
    id = Column('id', Integer, primary_key=True)
    rohstoff = Column('rohstoff', Text)
    name_ads = Column('name_ads', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-rohstoffe-vererzungen', GeologieRohstoffeVererzungen)


class GeologieTektonischeKarteLine(Base, Vector):
    __tablename__ = 'tektonische_karte_line'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/tektonische_karte_line.mako'
    __bodId__ = 'ch.swisstopo.geologie-tektonische_karte'
    # Translatable labels in fr
    __label__ = 'type_de'
    id = Column('fid', Integer, primary_key=True)
    line_id = Column('line_id', Integer)
    type_de = Column('type_de', Text)
    type_fr = Column('type_fr', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))


class GeologieTektonischeKartePoly(Base, Vector):
    __tablename__ = 'tektonische_karte_flaechen'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/tektonische_karte_poly.mako'
    __bodId__ = 'ch.swisstopo.geologie-tektonische_karte'
    # Translatable labels in fr
    __label__ = 'type_de'
    id = Column('fid', Integer, primary_key=True)
    t2_id = Column('t2_id', Integer)
    type_de = Column('type_de', Text)
    type_fr = Column('type_fr', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-tektonische_karte', GeologieTektonischeKarteLine)
register('ch.swisstopo.geologie-tektonische_karte', GeologieTektonischeKartePoly)


class GeologieEiszeitLgm(Base, Vector):
    __tablename__ = 'eiszeit_lgm500'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/eiszeit_lgm.mako'
    __bodId__ = 'ch.swisstopo.geologie-eiszeit-lgm'
    __label__ = 'ads_name'
    id = Column('bgdi_id', Integer, primary_key=True)
    ads_name = Column('ads_name', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY', dimension=2, srid=21781))

register('ch.swisstopo.geologie-eiszeit-lgm', GeologieEiszeitLgm)


class Swisstlm3dWanderwege(Base, Vector):
    __tablename__ = 'wanderwege_swissmap'
    __table_args__ = ({'schema': 'karto', 'autoload': False})
    __template__ = 'templates/htmlpopup/swissmap_online_wanderwege.mako'
    __bodId__ = 'ch.swisstopo.swisstlm3d-wanderwege'
    __label__ = 'id'
    id = Column('nr', Integer, primary_key=True)
    hikingtype = Column('hikingtype', Text)
    bridgetype = Column('bridgetype', Text)
    tunneltype = Column('tunneltype', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.swisstlm3d-wanderwege', Swisstlm3dWanderwege)


class VerschiebungsvektorenTsp1(Base, Vector):
    __tablename__ = 'verschiebungsvektoren_tsp1'
    __table_args__ = ({'schema': 'geodaesie', 'autoload': False})
    __template__ = 'templates/htmlpopup/verschiebungsvektoren_tps1.mako'
    __bodId__ = 'ch.swisstopo.verschiebungsvektoren-tsp1'
    __queryable_attributes__ = ['name']
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    fid = Column('id', Integer)
    name = Column('name', Text)
    type = Column('type', Text)
    e_lv03 = Column('e_lv03', Numeric)
    e_lv95 = Column('e_lv95', Numeric)
    n_lv03 = Column('n_lv03', Numeric)
    n_lv95 = Column('n_lv95', Numeric)
    de = Column('de', Numeric)
    dn = Column('dn', Numeric)
    fs = Column('fs', Numeric)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.verschiebungsvektoren-tsp1', VerschiebungsvektorenTsp1)


class VerschiebungsvektorenTsp2(Base, Vector):
    __tablename__ = 'verschiebungsvektoren_tsp2'
    __table_args__ = ({'schema': 'geodaesie', 'autoload': False})
    __template__ = 'templates/htmlpopup/verschiebungsvektoren_tps2.mako'
    __bodId__ = 'ch.swisstopo.verschiebungsvektoren-tsp2'
    __queryable_attributes__ = ['name', 'id']
    __label__ = 'name'
    id = Column('bgdi_id', Integer, primary_key=True)
    fid = Column('id', Integer)
    name = Column('name', Text)
    type = Column('type', Text)
    e_lv03 = Column('e_lv03', Numeric)
    e_lv95 = Column('e_lv95', Numeric)
    n_lv03 = Column('n_lv03', Numeric)
    n_lv95 = Column('n_lv95', Numeric)
    de = Column('de', Numeric)
    dn = Column('dn', Numeric)
    fs = Column('fs', Numeric)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.verschiebungsvektoren-tsp2', VerschiebungsvektorenTsp2)


class SwissmapOnlineWanderwege(Base, Vector):
    __tablename__ = 'wanderwege_swissmap'
    __table_args__ = ({'schema': 'karto', 'autoload': False, 'extend_existing': True})
    __template__ = 'templates/htmlpopup/swissmap_online_wanderwege.mako'
    __bodId__ = 'ch.swisstopo-karto.wanderwege'
    __label__ = 'id'
    id = Column('nr', Integer, primary_key=True)
    hikingtype = Column('hikingtype', Text)
    bridgetype = Column('bridgetype', Text)
    tunneltype = Column('tunneltype', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo-karto.wanderwege', SwissmapOnlineWanderwege)


class PLZOrtschaften(Base, Vector):
    __tablename__ = 'gabmo_plz'
    __table_args__ = ({'schema': 'vd', 'autoload': False})
    __template__ = 'templates/htmlpopup/gabmo_plz.mako'
    __bodId__ = 'ch.swisstopo-vd.ortschaftenverzeichnis_plz'
    __queryable_attributes__ = ['plz', 'langtext']
    __label__ = 'plz'
    id = Column('os_uuid', Text, primary_key=True)
    plz = Column('plz', Integer)
    zusziff = Column('zusziff', Text)
    langtext = Column('langtext', Text)
    bgdi_created = Column('bgdi_created', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo-vd.ortschaftenverzeichnis_plz', PLZOrtschaften)


class geometaStandAV(Base, Vector):
    __tablename__ = 'amogr_standav'
    __table_args__ = ({'schema': 'vd', 'autoload': False})
    __template__ = 'templates/htmlpopup/standav.mako'
    __bodId__ = 'ch.swisstopo-vd.geometa-standav'
    __label__ = 'frame'
    __returnedGeometry__ = 'the_geom_gen50'
    id = Column('gid', Integer, primary_key=True)
    fid = Column('id', Integer)
    quality = Column('quality', Text)
    frame = Column('frame', Text)
    the_geom = Column('the_geom', Geometry(geometry_type='GEOMETRY',
                                           dimension=2, srid=21781))
    the_geom_gen50 = Column('the_geom_gen50', Geometry(geometry_type='GEOMETRY',
                                                       dimension=2, srid=21781))

register('ch.swisstopo-vd.geometa-standav', geometaStandAV)


class geometaPNF(Base, Vector):
    __tablename__ = 'amopnf_pnf'
    __table_args__ = ({'schema': 'vd', 'autoload': False})
    __template__ = 'templates/htmlpopup/metadata_pnf.mako'
    __bodId__ = 'ch.swisstopo-vd.geometa-periodische_nachfuehrung'
    __label__ = 'description'
    id = Column('bgdi_id', Integer, primary_key=True)
    canton = Column('canton', Text)
    description = Column('description', Text)
    year = Column('year', Integer)
    the_geom = Column('the_geom', Geometry(geometry_type='GEOMETRY',
                                           dimension=2, srid=21781))

register('ch.swisstopo-vd.geometa-periodische_nachfuehrung', geometaPNF)


class geometaLos(Base, Vector):
    __tablename__ = 'amogr_los'
    __table_args__ = ({'schema': 'vd', 'autoload': False})
    __template__ = 'templates/htmlpopup/los.mako'
    __bodId__ = 'ch.swisstopo-vd.geometa-los'
    __label__ = 'operatsname'
    __returnedGeometry__ = 'the_geom_gen50'
    id = Column('gid', Integer, primary_key=True)
    fid = Column('id', Integer)
    neu_id = Column('neu_id', Text)
    operatsname = Column('operatsname', Text)
    losnr = Column('losnr', Text)
    taetigkeit_d = Column('taetigkeit_d', Text)
    taetigkeit_f = Column('taetigkeit_f', Text)
    taetigkeit_i = Column('taetigkeit_i', Text)
    quality = Column('quality', Text)
    flaeche_vertrag = Column('flaeche_vertrag', Text)
    frame = Column('frame', Text)
    bgdi_created = Column('bgdi_created', Text)
    the_geom = Column('the_geom', Geometry(geometry_type='GEOMETRY',
                                           dimension=2, srid=21781))
    the_geom_gen50 = Column('the_geom_gen50', Geometry(geometry_type='GEOMETRY',
                                                       dimension=2, srid=21781))

register('ch.swisstopo-vd.geometa-los', geometaLos)

# link sur le pdf ne fontionne pas...


class geometaGemeinde(Base, Vector):
    __tablename__ = 'amogr_gemeinde'
    __table_args__ = ({'schema': 'vd', 'autoload': False})
    __template__ = 'templates/htmlpopup/gemeinde.mako'
    __bodId__ = 'ch.swisstopo-vd.geometa-gemeinde'
    __label__ = 'gemeindename'
    __returnedGeometry__ = 'the_geom_gen50'
    id = Column('gid', Integer, primary_key=True)
    fid = Column('id', Integer)
    gemeindename = Column('gemeindename', Text)
    kanton = Column('kanton', Text)
    flaeche_ha = Column('flaeche_ha', Text)
    bfs_nr = Column('bfs_nr', Integer)
    pdf_liste = Column('pdf_liste', Text)
    abgabestelle = Column('abgabestelle', Text)
    bgdi_created = Column('bgdi_created', Text)
    the_geom = Column('the_geom', Geometry(geometry_type='GEOMETRY',
                                           dimension=2, srid=21781))
    the_geom_gen50 = Column('the_geom_gen50', Geometry(geometry_type='GEOMETRY',
                                                       dimension=2, srid=21781))

register('ch.swisstopo-vd.geometa-gemeinde', geometaGemeinde)


class geometaGrundbuch(Base, Vector):
    __tablename__ = 'amogr_grundbuch'
    __table_args__ = ({'schema': 'vd', 'autoload': False})
    __template__ = 'templates/htmlpopup/grundbuch.mako'
    __bodId__ = 'ch.swisstopo-vd.geometa-grundbuch'
    __label__ = 'ortsteil_grundbuch'
    __returnedGeometry__ = 'the_geom_gen50'
    id = Column('gid', Integer, primary_key=True)
    fid = Column('id', Integer)
    ortsteil_grundbuch = Column('ortsteil_grundbuch', Text)
    grundbuchfuehrung_d = Column('grundbuchfuehrung_d', Text)
    grundbuchfuehrung_f = Column('grundbuchfuehrung_f', Text)
    grundbuchfuehrung_i = Column('grundbuchfuehrung_i', Text)
    grundbuchkreis = Column('grundbuchkreis', Text)
    adresse = Column('adresse', Text)
    telefon = Column('telefon', Text)
    email = Column('email', Text)
    bgdi_created = Column('bgdi_created', Text)
    the_geom = Column('the_geom', Geometry(geometry_type='GEOMETRY',
                                           dimension=2, srid=21781))
    the_geom_gen50 = Column('the_geom_gen50', Geometry(geometry_type='GEOMETRY',
                                                       dimension=2, srid=21781))

register('ch.swisstopo-vd.geometa-grundbuch', geometaGrundbuch)


class geometaNfgeom(Base, Vector):
    __tablename__ = 'amogr_nfgeom'
    __table_args__ = ({'schema': 'vd', 'autoload': False})
    __template__ = 'templates/htmlpopup/nfgeom.mako'
    __bodId__ = 'ch.swisstopo-vd.geometa-nfgeom'
    __label__ = 'name'
    __returnedGeometry__ = 'the_geom_gen50'
    id = Column('gid', Integer, primary_key=True)
    name = Column('name', Text)
    firmenname = Column('firmenname', Text)
    adresse = Column('adresse', Text)
    telefon = Column('telefon', Text)
    email = Column('email', Text)
    bgdi_created = Column('bgdi_created', Text)
    the_geom = Column('the_geom', Geometry(geometry_type='GEOMETRY',
                                           dimension=2, srid=21781))
    the_geom_gen50 = Column('the_geom_gen50', Geometry(geometry_type='GEOMETRY',
                                                       dimension=2, srid=21781))

register('ch.swisstopo-vd.geometa-nfgeom', geometaNfgeom)


class oerebkataster(Base, Vector):
    __tablename__ = 'view_oereb_nfgeom'
    __table_args__ = ({'schema': 'vd', 'autoload': False})
    __template__ = 'templates/htmlpopup/oerebkataster.mako'
    __bodId__ = 'ch.swisstopo-vd.stand-oerebkataster'
    __label__ = 'gemeindename'
    id = Column('gid', Integer, primary_key=True)
    fid = Column('id', Integer)
    gemeindename = Column('gemeindename', Text)
    kanton = Column('kanton', Text)
    oereb_status_de = Column('oereb_status_de', Text)
    oereb_status_fr = Column('oereb_status_fr', Text)
    oereb_status_it = Column('oereb_status_it', Text)
    oereb_status_rm = Column('oereb_status_rm', Text)
    oereb_status_en = Column('oereb_status_en', Text)
    bfs_nr = Column('bfs_nr', Integer)
    firmenname = Column('firmenname', Text)
    adresszeile = Column('adresszeile', Text)
    plz = Column('plz', Integer)
    ort = Column('ort', Text)
    telefon = Column('telefon', Text)
    email = Column('email', Text)
    url_oereb = Column('url_oereb', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo-vd.stand-oerebkataster', oerebkataster)


class transformationBezugsrahmenHoehePunkte(Base, Vector):
    __tablename__ = 'bezugsrahmen_hoehe_pkt'
    __table_args__ = ({'schema': 'geodaesie', 'autoload': False})
    __template__ = 'templates/htmlpopup/transformation_bezugsrahmen_hoehe.mako'
    __bodId__ = 'ch.swisstopo.transformation-bezugsrahmen_hoehe'
    __label__ = 'name'
    __queryable_attributes__ = ['name']
    id = Column('bgdi_id', Integer, primary_key=True)
    name = Column('name', Text)
    y = Column('y', Numeric)
    x = Column('x', Numeric)
    or_ln02_cm = Column('or_ln02_cm', Numeric)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))


class transformationBezugsrahmenHoeheLine5cm(Base, Vector):
    __tablename__ = 'bezugsrahmen_hoehe_line_5cm'
    __table_args__ = ({'schema': 'geodaesie', 'autoload': False})
    __template__ = 'templates/htmlpopup/transformation_bezugsrahmen_hoehe.mako'
    __bodId__ = 'ch.swisstopo.transformation-bezugsrahmen_hoehe'
    __label__ = 'contour'
    __maxscale__ = 500000
    id = Column('bgdi_id', Integer, primary_key=True)
    contour = Column('contour', Numeric)
    layer = Column('layer', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))


class transformationBezugsrahmenHoeheLine10cm(Base, Vector):
    __tablename__ = 'bezugsrahmen_hoehe_line_10cm'
    __table_args__ = ({'schema': 'geodaesie', 'autoload': False})
    __template__ = 'templates/htmlpopup/transformation_bezugsrahmen_hoehe.mako'
    __bodId__ = 'ch.swisstopo.transformation-bezugsrahmen_hoehe'
    __label__ = 'contour'
    __minscale__ = 500000
    id = Column('bgdi_id', Integer, primary_key=True)
    contour = Column('contour', Numeric)
    layer = Column('layer', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.transformation-bezugsrahmen_hoehe', transformationBezugsrahmenHoehePunkte)
register('ch.swisstopo.transformation-bezugsrahmen_hoehe', transformationBezugsrahmenHoeheLine5cm)
register('ch.swisstopo.transformation-bezugsrahmen_hoehe', transformationBezugsrahmenHoeheLine10cm)


class HebungsratenLine(Base, Vector):
    __tablename__ = 'hebungsraten_line'
    __table_args__ = ({'schema': 'geodaesie', 'autoload': False})
    __template__ = 'templates/htmlpopup/hebungsraten.mako'
    __bodId__ = 'ch.swisstopo.hebungsraten'
    __queryable_attributes__ = []
    __label__ = 'contour'
    id = Column('bgdi_id', Integer, primary_key=True)
    contour = Column('contour', Numeric)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))


class HebungsratenPunkt(Base, Vector):
    __tablename__ = 'hebungsraten_pkt'
    __table_args__ = ({'schema': 'geodaesie', 'autoload': False})
    __template__ = 'templates/htmlpopup/hebungsraten.mako'
    __bodId__ = 'ch.swisstopo.hebungsraten'
    __queryable_attributes__ = ['ord_nr', 'ort']
    __label__ = 'ord_nr'
    id = Column('bgdi_id', Integer, primary_key=True)
    ord_nr = Column('ord_nr', Text)
    ort = Column('ort', Text)
    v = Column('v', Numeric)
    mfv = Column('mfv', Numeric)
    klasse = Column('klasse', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.hebungsraten', HebungsratenLine)
register('ch.swisstopo.hebungsraten', HebungsratenPunkt)


class spannungsarmeGebiete(Base, Vector):
    __tablename__ = 'spannungsarme_gebiete'
    __table_args__ = ({'schema': 'vd', 'autoload': False})
    __template__ = 'templates/htmlpopup/spannungsarme_gebiete.mako'
    __bodId__ = 'ch.swisstopo.transformationsgenauigkeit'
    __label__ = 'sg_name'
    id = Column('identifier', Text, primary_key=True)
    sg_name = Column('sg_name', Text)
    vali_date = Column('vali_date', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.transformationsgenauigkeit', spannungsarmeGebiete)


class spannungsarmeGebieteVD(spannungsarmeGebiete):
    __bodId__ = 'ch.swisstopo-vd.spannungsarme-gebiete'

register('ch.swisstopo-vd.spannungsarme-gebiete', spannungsarmeGebieteVD)


class geologieGeotopePunkte(Base, Vector):
    __tablename__ = 'geotope_pkt'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/geotope.mako'
    __bodId__ = 'ch.swisstopo.geologie-geotope'
    __label__ = 'nom'
    id = Column('objectid', Integer, primary_key=True)
    nom = Column('nom', Text)
    fix_id = Column('fix_id', Text)
    nummer = Column('nummer', Integer)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))


class geologieGeotopeFlaechen(Base, Vector):
    __tablename__ = 'geotope_plg'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/geotope.mako'
    __bodId__ = 'ch.swisstopo.geologie-geotope'
    __label__ = 'nom'
    id = Column('objectid', Integer, primary_key=True)
    nom = Column('nom', Text)
    fix_id = Column('fix_id', Text)
    nummer = Column('nummer', Integer)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-geotope', geologieGeotopePunkte)
register('ch.swisstopo.geologie-geotope', geologieGeotopeFlaechen)


class steine_hist_bauwerke(Base, Vector):
    __tablename__ = 'geotechnik_steine_historische_bauwerke'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/geol_steine_hist_bauwerke.mako'
    __bodId__ = 'ch.swisstopo.geologie-geotechnik-steine_historische_bauwerke'
    __extended_info__ = True
    __label__ = 'objekt'
    id = Column('bgdi_id', Integer, primary_key=True)
    objekt = Column('objekt', Text)
    obtyp = Column('obtyp', Text)
    ort = Column('ort', Text)
    objektteil = Column('objektteil', Text)
    age = Column('age', Text)
    gestart = Column('gestart', Text)
    referenz = Column('referenz', Text)
    hyperlink = Column('hyperlink', Text)
    abbauort = Column('abbauort', Text)
    bemerkung = Column('bemerkung', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-geotechnik-steine_historische_bauwerke', steine_hist_bauwerke)


class gisgeol_punkte(Base, Vector):
    __tablename__ = 'view_gisgeol_points'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/gisgeol.mako'
    __bodId__ = 'ch.swisstopo.geologie-gisgeol-punkte'
    __queryable_attributes__ = ['sgd_nr']
    __label__ = 'title'
    id = Column('gid', Integer, primary_key=True)
    sgd_nr = Column('sgd_nr', Integer)
    title = Column('title', Text)
    orig_id = Column('original_document_id', Text)
    author = Column('author', Text)
    report_structure = Column('report_structure', Text)
    aux_info = Column('auxiliary_information', Text)
    doccreation = Column('doccreation_date', Text)
    copy_avail = Column('copy_avail', Text)
    view_avail = Column('view_avail', Text)
    pdf_url = Column('pdf_url', Text)
    bgdi_data_status = Column('bgdi_data_status', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-gisgeol-punkte', gisgeol_punkte)


class gisgeol_linien(Base, Vector):
    __tablename__ = 'view_gisgeol_lines'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/gisgeol.mako'
    __bodId__ = 'ch.swisstopo.geologie-gisgeol-linien'
    __queryable_attributes__ = ['sgd_nr']
    __label__ = 'title'
    id = Column('gid', Integer, primary_key=True)
    sgd_nr = Column('sgd_nr', Integer)
    title = Column('title', Text)
    orig_id = Column('original_document_id', Text)
    author = Column('author', Text)
    report_structure = Column('report_structure', Text)
    aux_info = Column('auxiliary_information', Text)
    doccreation = Column('doccreation_date', Text)
    copy_avail = Column('copy_avail', Text)
    view_avail = Column('view_avail', Text)
    pdf_url = Column('pdf_url', Text)
    bgdi_data_status = Column('bgdi_data_status', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-gisgeol-linien', gisgeol_linien)


class gisgeol_flaechen_1x1km(Base, Vector):
    __tablename__ = 'view_gisgeol_surfaces_1x1km'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/gisgeol.mako'
    __bodId__ = 'ch.swisstopo.geologie-gisgeol-flaechen-1x1km'
    __queryable_attributes__ = ['sgd_nr']
    __label__ = 'title'
    id = Column('gid', Integer, primary_key=True)
    sgd_nr = Column('sgd_nr', Integer)
    title = Column('title', Text)
    orig_id = Column('original_document_id', Text)
    author = Column('author', Text)
    report_structure = Column('report_structure', Text)
    aux_info = Column('auxiliary_information', Text)
    doccreation = Column('doccreation_date', Text)
    copy_avail = Column('copy_avail', Text)
    view_avail = Column('view_avail', Text)
    pdf_url = Column('pdf_url', Text)
    bgdi_data_status = Column('bgdi_data_status', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-gisgeol-flaechen-1x1km', gisgeol_flaechen_1x1km)


class gisgeol_flaechen_10x10km(Base, Vector):
    __tablename__ = 'view_gisgeol_surfaces_10x10km'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/gisgeol.mako'
    __bodId__ = 'ch.swisstopo.geologie-gisgeol-flaechen-10x10km'
    __queryable_attributes__ = ['sgd_nr']
    __label__ = 'title'
    id = Column('gid', Integer, primary_key=True)
    sgd_nr = Column('sgd_nr', Integer)
    title = Column('title', Text)
    orig_id = Column('original_document_id', Text)
    author = Column('author', Text)
    report_structure = Column('report_structure', Text)
    aux_info = Column('auxiliary_information', Text)
    doccreation = Column('doccreation_date', Text)
    copy_avail = Column('copy_avail', Text)
    view_avail = Column('view_avail', Text)
    pdf_url = Column('pdf_url', Text)
    bgdi_data_status = Column('bgdi_data_status', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-gisgeol-flaechen-10x10km', gisgeol_flaechen_10x10km)


class gisgeol_flaechen_10to100km2(Base, Vector):
    __tablename__ = 'view_gisgeol_surfaces_10to100km2'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/gisgeol.mako'
    __bodId__ = 'ch.swisstopo.geologie-gisgeol-flaechen-10to100km2'
    __queryable_attributes__ = ['sgd_nr']
    __label__ = 'title'
    id = Column('gid', Integer, primary_key=True)
    sgd_nr = Column('sgd_nr', Integer)
    title = Column('title', Text)
    orig_id = Column('original_document_id', Text)
    author = Column('author', Text)
    report_structure = Column('report_structure', Text)
    aux_info = Column('auxiliary_information', Text)
    doccreation = Column('doccreation_date', Text)
    copy_avail = Column('copy_avail', Text)
    view_avail = Column('view_avail', Text)
    pdf_url = Column('pdf_url', Text)
    bgdi_data_status = Column('bgdi_data_status', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))


class gisgeol_flaechen_100to1000km2(Base, Vector):
    __tablename__ = 'view_gisgeol_surfaces_100to1000km2'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/gisgeol.mako'
    __bodId__ = 'ch.swisstopo.geologie-gisgeol-flaechen-100to1000km2'
    __queryable_attributes__ = ['sgd_nr']
    __label__ = 'title'
    id = Column('gid', Integer, primary_key=True)
    sgd_nr = Column('sgd_nr', Integer)
    title = Column('title', Text)
    orig_id = Column('original_document_id', Text)
    author = Column('author', Text)
    report_structure = Column('report_structure', Text)
    aux_info = Column('auxiliary_information', Text)
    doccreation = Column('doccreation_date', Text)
    copy_avail = Column('copy_avail', Text)
    view_avail = Column('view_avail', Text)
    pdf_url = Column('pdf_url', Text)
    bgdi_data_status = Column('bgdi_data_status', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))


class gisgeol_flaechen_1000to21000km2(Base, Vector):
    __tablename__ = 'view_gisgeol_surfaces_1000to21000km2'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/gisgeol.mako'
    __bodId__ = 'ch.swisstopo.geologie-gisgeol-flaechen-1000to21000km2'
    __queryable_attributes__ = ['sgd_nr']
    __label__ = 'title'
    id = Column('gid', Integer, primary_key=True)
    sgd_nr = Column('sgd_nr', Integer)
    title = Column('title', Text)
    orig_id = Column('original_document_id', Text)
    author = Column('author', Text)
    report_structure = Column('report_structure', Text)
    aux_info = Column('auxiliary_information', Text)
    doccreation = Column('doccreation_date', Text)
    copy_avail = Column('copy_avail', Text)
    view_avail = Column('view_avail', Text)
    pdf_url = Column('pdf_url', Text)
    bgdi_data_status = Column('bgdi_data_status', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-gisgeol-flaechen-10to100km2', gisgeol_flaechen_10to100km2)
register('ch.swisstopo.geologie-gisgeol-flaechen-100to1000km2', gisgeol_flaechen_100to1000km2)
register('ch.swisstopo.geologie-gisgeol-flaechen-1000to21000km2', gisgeol_flaechen_1000to21000km2)


class gisgeol_flaechen_gt21000km2(Base, Vector):
    __tablename__ = 'view_gisgeol_surfaces_gt21000km2'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/gisgeol.mako'
    __bodId__ = 'ch.swisstopo.geologie-gisgeol-flaechen-gt21000km2'
    __queryable_attributes__ = ['sgd_nr']
    __label__ = 'title'
    id = Column('gid', Integer, primary_key=True)
    sgd_nr = Column('sgd_nr', Integer)
    title = Column('title', Text)
    orig_id = Column('original_document_id', Text)
    author = Column('author', Text)
    report_structure = Column('report_structure', Text)
    aux_info = Column('auxiliary_information', Text)
    doccreation = Column('doccreation_date', Text)
    copy_avail = Column('copy_avail', Text)
    view_avail = Column('view_avail', Text)
    pdf_url = Column('pdf_url', Text)
    bgdi_data_status = Column('bgdi_data_status', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-gisgeol-flaechen-gt21000km2', gisgeol_flaechen_gt21000km2)


class gisgeol_flaechen_lt10km2(Base, Vector):
    __tablename__ = 'view_gisgeol_surfaces_lt10km2'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/gisgeol.mako'
    __bodId__ = 'ch.swisstopo.geologie-gisgeol-flaechen-lt10km2'
    __queryable_attributes__ = ['sgd_nr']
    __label__ = 'title'
    id = Column('gid', Integer, primary_key=True)
    sgd_nr = Column('sgd_nr', Integer)
    title = Column('title', Text)
    orig_id = Column('original_document_id', Text)
    author = Column('author', Text)
    report_structure = Column('report_structure', Text)
    aux_info = Column('auxiliary_information', Text)
    doccreation = Column('doccreation_date', Text)
    copy_avail = Column('copy_avail', Text)
    view_avail = Column('view_avail', Text)
    pdf_url = Column('pdf_url', Text)
    bgdi_data_status = Column('bgdi_data_status', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-gisgeol-flaechen-lt10km2', gisgeol_flaechen_lt10km2)


class geocover_line_aux(Base, Vector):
    __tablename__ = 'view_geocover_line_aux'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/geocover_line_aux.mako'
    __bodId__ = 'ch.swisstopo.geologie-geocover'
    __label__ = 'description'
    id = Column('bgdi_id', Integer, primary_key=True)
    basisdatensatz = Column('basisdatensatz', Text)
    description = Column('description', Text)
    spec_description = Column('spec_description', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-geocover', geocover_line_aux)


class geocover_point_hydro(Base, Vector):
    __tablename__ = 'view_geocover_point_hydro'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/geocover_point_hydro.mako'
    __bodId__ = 'ch.swisstopo.geologie-geocover'
    __label__ = 'description'
    id = Column('bgdi_id', Integer, primary_key=True)
    basisdatensatz = Column('basisdatensatz', Text)
    description = Column('description', Text)
    spec_description = Column('spec_description', Text)
    azimut = Column('azimut', Text)
    depth = Column('depth', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-geocover', geocover_point_hydro)


class geocover_point_geol(Base, Vector):
    __tablename__ = 'view_geocover_point_geol'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/geocover_point_hydro.mako'
    __bodId__ = 'ch.swisstopo.geologie-geocover'
    __label__ = 'description'
    id = Column('bgdi_id', Integer, primary_key=True)
    basisdatensatz = Column('basisdatensatz', Text)
    description = Column('description', Text)
    spec_description = Column('spec_description', Text)
    azimut = Column('azimut', Text)
    depth = Column('depth', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-geocover', geocover_point_geol)


class geocover_point_drill(Base, Vector):
    __tablename__ = 'view_geocover_point_drill'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/geocover_point_drill.mako'
    __bodId__ = 'ch.swisstopo.geologie-geocover'
    __label__ = 'description'
    id = Column('bgdi_id', Integer, primary_key=True)
    basisdatensatz = Column('basisdatensatz', Text)
    description = Column('description', Text)
    spec_description = Column('spec_description', Text)
    azimut = Column('azimut', Text)
    depth_1 = Column('depth_1', Text)
    description_1 = Column('description_1', Text)
    depth_2 = Column('depth_2', Text)
    description_2 = Column('description_2', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-geocover', geocover_point_drill)


class geocover_point_info(Base, Vector):
    __tablename__ = 'view_geocover_point_info'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/geocover_point_info.mako'
    __bodId__ = 'ch.swisstopo.geologie-geocover'
    __label__ = 'description'
    id = Column('bgdi_id', Integer, primary_key=True)
    basisdatensatz = Column('basisdatensatz', Text)
    description = Column('description', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-geocover', geocover_point_info)


class geocover_point_struct(Base, Vector):
    __tablename__ = 'view_geocover_point_struct'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/geocover_point_struct.mako'
    __bodId__ = 'ch.swisstopo.geologie-geocover'
    __label__ = 'description'
    id = Column('bgdi_id', Integer, primary_key=True)
    basisdatensatz = Column('basisdatensatz', Text)
    description = Column('description', Text)
    spec_description = Column('spec_description', Text)
    azimut = Column('azimut', Text)
    dip = Column('dip', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-geocover', geocover_point_struct)


class geocover_polygon_aux_1(Base, Vector):
    __tablename__ = 'view_geocover_polygon_aux_1'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/geocover_polygon.mako'
    __bodId__ = 'ch.swisstopo.geologie-geocover'
    __label__ = 'description'
    id = Column('bgdi_id', Integer, primary_key=True)
    basisdatensatz = Column('basisdatensatz', Text)
    description = Column('description', Text)
    tecto = Column('tecto', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-geocover', geocover_polygon_aux_1)


class geocover_polygon_aux_2(Base, Vector):
    __tablename__ = 'view_geocover_polygon_aux_2'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/geocover_polygon.mako'
    __bodId__ = 'ch.swisstopo.geologie-geocover'
    __label__ = 'description'
    id = Column('bgdi_id', Integer, primary_key=True)
    basisdatensatz = Column('basisdatensatz', Text)
    description = Column('description', Text)
    tecto = Column('tecto', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-geocover', geocover_polygon_aux_2)


class geocover_polygon_main(Base, Vector):
    __tablename__ = 'view_geocover_polygon_main'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/geocover_polygon.mako'
    __bodId__ = 'ch.swisstopo.geologie-geocover'
    __label__ = 'description'
    id = Column('bgdi_id', Integer, primary_key=True)
    basisdatensatz = Column('basisdatensatz', Text)
    description = Column('description', Text)
    tecto = Column('tecto', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-geocover', geocover_polygon_main)


class ga25_line_aux(Base, Vector):
    __tablename__ = 'view_ga25_line_aux'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/ga25_line_aux.mako'
    __bodId__ = 'ch.swisstopo.geologie-geologischer_atlas'
    __label__ = 'description'
    id = Column('bgdi_id', Integer, primary_key=True)
    basisdatensatz = Column('basisdatensatz', Text)
    description = Column('description', Text)
    spec_description = Column('spec_description', Text)
    url_legend = Column('url_legende', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-geologischer_atlas', ga25_line_aux)


class ga25_point_hydro(Base, Vector):
    __tablename__ = 'view_ga25_point_hydro'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/ga25_point_hydro.mako'
    __bodId__ = 'ch.swisstopo.geologie-geologischer_atlas'
    __label__ = 'description'
    id = Column('bgdi_id', Integer, primary_key=True)
    basisdatensatz = Column('basisdatensatz', Text)
    description = Column('description', Text)
    spec_description = Column('spec_description', Text)
    azimut = Column('azimut', Text)
    depth = Column('depth', Text)
    url_legend = Column('url_legende', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-geologischer_atlas', ga25_point_hydro)


class ga25_point_geol(Base, Vector):
    __tablename__ = 'view_ga25_point_geol'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/ga25_point_hydro.mako'
    __bodId__ = 'ch.swisstopo.geologie-geologischer_atlas'
    __label__ = 'description'
    id = Column('bgdi_id', Integer, primary_key=True)
    basisdatensatz = Column('basisdatensatz', Text)
    description = Column('description', Text)
    spec_description = Column('spec_description', Text)
    azimut = Column('azimut', Text)
    depth = Column('depth', Text)
    url_legend = Column('url_legende', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-geologischer_atlas', ga25_point_geol)


class ga25_point_drill(Base, Vector):
    __tablename__ = 'view_ga25_point_drill'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/ga25_point_drill.mako'
    __bodId__ = 'ch.swisstopo.geologie-geologischer_atlas'
    __label__ = 'description'
    id = Column('bgdi_id', Integer, primary_key=True)
    basisdatensatz = Column('basisdatensatz', Text)
    description = Column('description', Text)
    spec_description = Column('spec_description', Text)
    azimut = Column('azimut', Text)
    depth_1 = Column('depth_1', Text)
    description_1 = Column('description_1', Text)
    depth_2 = Column('depth_2', Text)
    description_2 = Column('description_2', Text)
    url_legend = Column('url_legende', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-geologischer_atlas', ga25_point_drill)


class ga25_point_info(Base, Vector):
    __tablename__ = 'view_ga25_point_info'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/ga25_point_info.mako'
    __bodId__ = 'ch.swisstopo.geologie-geologischer_atlas'
    __label__ = 'description'
    id = Column('bgdi_id', Integer, primary_key=True)
    basisdatensatz = Column('basisdatensatz', Text)
    description = Column('description', Text)
    url_legend = Column('url_legende', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-geologischer_atlas', ga25_point_info)


class ga25_point_struct(Base, Vector):
    __tablename__ = 'view_ga25_point_struct'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/ga25_point_struct.mako'
    __bodId__ = 'ch.swisstopo.geologie-geologischer_atlas'
    __label__ = 'description'
    id = Column('bgdi_id', Integer, primary_key=True)
    basisdatensatz = Column('basisdatensatz', Text)
    description = Column('description', Text)
    spec_description = Column('spec_description', Text)
    azimut = Column('azimut', Text)
    dip = Column('dip', Text)
    url_legend = Column('url_legende', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-geologischer_atlas', ga25_point_struct)


class ga25_polygon_aux_1(Base, Vector):
    __tablename__ = 'view_ga25_polygon_aux_1'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/ga25_polygon.mako'
    __bodId__ = 'ch.swisstopo.geologie-geologischer_atlas'
    __label__ = 'description'
    id = Column('bgdi_id', Integer, primary_key=True)
    basisdatensatz = Column('basisdatensatz', Text)
    description = Column('description', Text)
    tecto = Column('tecto', Text)
    url_legend = Column('url_legende', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-geologischer_atlas', ga25_polygon_aux_1)


class ga25_polygon_aux_2(Base, Vector):
    __tablename__ = 'view_ga25_polygon_aux_2'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/ga25_polygon.mako'
    __bodId__ = 'ch.swisstopo.geologie-geologischer_atlas'
    __label__ = 'description'
    id = Column('bgdi_id', Integer, primary_key=True)
    basisdatensatz = Column('basisdatensatz', Text)
    description = Column('description', Text)
    tecto = Column('tecto', Text)
    url_legend = Column('url_legende', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-geologischer_atlas', ga25_polygon_aux_2)


class ga25_polygon_main(Base, Vector):
    __tablename__ = 'view_ga25_polygon_main'
    __table_args__ = ({'schema': 'geol', 'autoload': False})
    __template__ = 'templates/htmlpopup/ga25_polygon.mako'
    __bodId__ = 'ch.swisstopo.geologie-geologischer_atlas'
    __label__ = 'description'
    id = Column('bgdi_id', Integer, primary_key=True)
    basisdatensatz = Column('basisdatensatz', Text)
    description = Column('description', Text)
    tecto = Column('tecto', Text)
    url_legend = Column('url_legende', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))

register('ch.swisstopo.geologie-geologischer_atlas', ga25_polygon_main)


class Swissnames3d:
    __table_args__ = ({'schema': 'tlm', 'autoload': False})
    __label__ = 'name'
    __template__ = 'templates/htmlpopup/swissnames3d.mako'
    __bodId__ = 'ch.swisstopo.swissnames3d'
    id = Column('bgdi_id', Integer, primary_key=True)
    objektart = Column('objektart', Text)
    objektklasse = Column('objektklasse', Text)
    name = Column('name', Text)
    sprachcode = Column('sprachcode', Text)
    namen_typ = Column('namen_typ', Text)
    the_geom = Column(Geometry(geometry_type='GEOMETRY',
                               dimension=2, srid=21781))


class Swissnames3dRaster00(Base, Swissnames3d, Vector):
    __tablename__ = 'swissnames3d_raster_00'
    __maxscale__ = 25000000
    __minscale__ = 2100000


class Swissnames3dRaster01(Base, Swissnames3d, Vector):
    __tablename__ = 'swissnames3d_raster_01'
    __maxscale__ = 2100000
    __minscale__ = 1700000


class Swissnames3dRaster02(Base, Swissnames3d, Vector):
    __tablename__ = 'swissnames3d_raster_02'
    __maxscale__ = 1700000
    __minscale__ = 940000


class Swissnames3dRaster03(Base, Swissnames3d, Vector):
    __tablename__ = 'swissnames3d_raster_03'
    __maxscale__ = 940000
    __minscale__ = 370000


class Swissnames3dRaster04(Base, Swissnames3d, Vector):
    __tablename__ = 'swissnames3d_raster_04'
    __maxscale__ = 370000
    __minscale__ = 180000


class Swissnames3dRaster05(Base, Swissnames3d, Vector):
    __tablename__ = 'swissnames3d_raster_05'
    __maxscale__ = 180000
    __minscale__ = 75000


class Swissnames3dRaster06(Base, Swissnames3d, Vector):
    __tablename__ = 'swissnames3d_raster_06'
    __maxscale__ = 75000
    __minscale__ = 35000


class Swissnames3dRaster07(Base, Swissnames3d, Vector):
    __tablename__ = 'swissnames3d_raster_07'
    __maxscale__ = 35000
    __minscale__ = 18000


class Swissnames3dRaster08(Base, Swissnames3d, Vector):
    __tablename__ = 'swissnames3d_raster_08'
    __maxscale__ = 18000
    __minscale__ = 9000


class Swissnames3dRaster09(Base, Swissnames3d, Vector):
    __tablename__ = 'swissnames3d_raster_09'
    __maxscale__ = 9000
    __minscale__ = 7000


class Swissnames3dRaster10(Base, Swissnames3d, Vector):
    __tablename__ = 'swissnames3d_raster_10'
    __maxscale__ = 7000
    __minscale__ = 3500


class Swissnames3dRaster11(Base, Swissnames3d, Vector):
    __tablename__ = 'swissnames3d_raster_11'
    __maxscale__ = 3500
    __minscale__ = 1800


class Swissnames3dRaster12(Base, Swissnames3d, Vector):
    __tablename__ = 'swissnames3d_raster_12'
    __maxscale__ = 1800
    __minscale__ = 900


class Swissnames3dRaster13(Base, Swissnames3d, Vector):
    __tablename__ = 'swissnames3d_raster_13'
    __maxscale__ = 900
    __minscale__ = 1


register('ch.swisstopo.swissnames3d', Swissnames3dRaster00)
register('ch.swisstopo.swissnames3d', Swissnames3dRaster01)
register('ch.swisstopo.swissnames3d', Swissnames3dRaster02)
register('ch.swisstopo.swissnames3d', Swissnames3dRaster03)
register('ch.swisstopo.swissnames3d', Swissnames3dRaster04)
register('ch.swisstopo.swissnames3d', Swissnames3dRaster05)
register('ch.swisstopo.swissnames3d', Swissnames3dRaster06)
register('ch.swisstopo.swissnames3d', Swissnames3dRaster07)
register('ch.swisstopo.swissnames3d', Swissnames3dRaster08)
register('ch.swisstopo.swissnames3d', Swissnames3dRaster09)
register('ch.swisstopo.swissnames3d', Swissnames3dRaster10)
register('ch.swisstopo.swissnames3d', Swissnames3dRaster11)
register('ch.swisstopo.swissnames3d', Swissnames3dRaster12)
register('ch.swisstopo.swissnames3d', Swissnames3dRaster13)
