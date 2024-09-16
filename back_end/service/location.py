#!/usr/bin/env python3
"""Module: location """
import requests


class LocationService:

    @staticmethod
    def get_public_ip():
        """Get the public IP address using an external service"""
        response = requests.get('https://api.ipify.org?format=json')
        return response.json().get('ip')

    @staticmethod
    def get_location_info(ip_addr: str) -> dict | str:
        """Get location information by IP address"""
        data = requests.get(f'https://ipapi.co/{ip_addr}/json/').json()

        if data.get('error'):
            return data.get('reason')
        else:
            return {
                'city': data.get('city'),
                'country': data.get('country'),
                'latitude': data.get('latitude'),
                'longitude': data.get('longitude')
            }