import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    """ Base config
    """

    # Threads config
    THREADS_PER_PAGE = 2

class ProductionConfig(Config):
    """ Production config
    Args:
        Config (class): base config
    """
    pass

class DevelopmentConfig(Config):
    """ Development config
    Args:
        Config (class): base config
    """
    DEBUG = True

config = {
    'production': ProductionConfig,
    'development': DevelopmentConfig
}
