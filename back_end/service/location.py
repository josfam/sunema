#!/usr/bin/env python3
"""Module: location """
import requests


def get_location_by_ip(ip_addr: str) -> dict:
    """Get location information by IP address"""
    location_info = requests.get(f'https://ipapi.co/{ip_addr}/json/').json()
    return location_info
