import geojson


def toJsonFeature(carwash):
    # pair = list(reversed([float(i) for i in carwash.location.split(',')]))
    if not carwash.location: return None
    return geojson.Feature(geometry=geojson.Point(carwash.location))

def getFeatureCollection(model):
    all = [toJsonFeature(i) for i in model.objects.all() if i.location]
    return geojson.FeatureCollection(all)
