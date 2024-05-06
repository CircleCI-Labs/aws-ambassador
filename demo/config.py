import os
basedir = os.path.abspath(os.path.dirname(__file__))


# Creates base config
class Config:
    # Used to set need variables like database connection if the application calls for it

    @staticmethod
    def init_app(app):
        pass


# For develop config
class DevelopmentConfig(Config):
    DEBUG = True


# For testing config
class TestingConfig(Config):
    TESTING = True
    DEBUG = True


# For production config
class ProductionConfig(Config):
    TESTING = False
    DEBUG = False


# Allows use to pass in a name and get back the right config based on the name
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': ProductionConfig
}
