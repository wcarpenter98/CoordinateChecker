from turfpy.measurement import boolean_point_in_polygon
from geojson import Point, Polygon, Feature

point = Feature(geometry=Point((-46.6318, -23.5523)))
polygon = Polygon(
    [
        [
            (-46.653, -23.543),
            (-46.634, -23.5346),
            (-46.613, -23.543),
            (-46.614, -23.559),
            (-46.631, -23.567),
            (-46.653, -23.560),
            (-46.653, -23.543),
        ]
    ]
)


#boolean_point_in_polygon(point, polygon)
print(boolean_point_in_polygon(point, polygon))
