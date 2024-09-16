from back_end.views import app_views
from back_end.service.location import LocationService
from flask import request, jsonify


@app_views.route('/location', methods=['GET'], strict_slashes=False)
def get_location():
    """ Get location information by IP address """
    ip_addr = request.remote_addr
    # use get_public_ip only for local testing, it will be removed in production
    if ip_addr == '127.0.0.1':
        ip_addr = LocationService.get_public_ip()

    location_info = LocationService.get_location_info(ip_addr)
    if location_info is None:
        return jsonify({"message": location_info}), 404
    return jsonify(location_info)