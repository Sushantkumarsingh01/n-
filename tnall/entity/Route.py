class Route:
    def __init__(self, route_id=None, start_destination=None, end_destination=None, distance=None):
        self._route_id = route_id
        self._start_destination = start_destination
        self._end_destination = end_destination
        self._distance = distance

    def get_route_id(self):
        return self._route_id

    def get_start_destination(self):
        return self._start_destination

    def get_end_destination(self):
        return self._end_destination

    def get_distance(self):
        return self._distance

    def set_route_id(self, route_id):
        self._route_id = route_id

    def set_start_destination(self, start_destination):
        self._start_destination = start_destination

    def set_end_destination(self, end_destination):
        self._end_destination = end_destination

    def set_distance(self, distance):
        self._distance = distance

    def __str__(self):
        return f"Route(ID: {self._route_id}, Start: {self._start_destination}, End: {self._end_destination}, Distance: {self._distance})"




