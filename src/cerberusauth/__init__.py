"""
Cerberus - Authentication and authorisation microservice.
"""

from . import registration


def create_cerberus():
    return CerberusAuth(
        registration_service=registration.RegistrationService()
    )


class CerberusAuth(object):
    """
    Provides authentication and authorisation as a microservice.
    """

    def __init__(self, registration_service):
        """Initialise an instance."""
        self.registration = registration_service
