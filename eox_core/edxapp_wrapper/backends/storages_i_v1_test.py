#!/usr/bin/env python
# -*- coding: utf-8 -*-
from eox_core.test_utils import TestStorage


def get_edxapp_production_staticfiles_storage():
    """
    Return the edx-platform production staticfiles storage
    """
    try:
        from openedx.core.storage import ProductionStorage
    except ImportError:
        ProductionStorage = TestStorage
    return ProductionStorage


def get_edxapp_development_staticfiles_storage():
    """
    Return the edx-platform development staticfiles storage
    """
    try:
        from openedx.core.storage import DevelopmentStorage
    except ImportError:
        DevelopmentStorage = TestStorage
    return DevelopmentStorage
