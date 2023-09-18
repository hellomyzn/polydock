
"""common.google_spreadsheet.gss_accessor"""
#########################################################
# Builtin packages
#########################################################

#########################################################
# 3rd party packages
#########################################################
import spotipy
from spotipy.oauth2 import SpotifyOAuth

#########################################################
# Own packages
#########################################################
from utils import Singleton
from common.config import Config
from common.logging import (
    info,
    error_stack_trace
)


class SpotifyAccessor(Singleton):
    """
        Usage:
            1. put config below in src/common/config/config.ini
                - SPOTIPY_CLIENT_ID
                - SPOTIPY_CLIENT_SECRET
            2. put redirect url after running script and pasting url shown
    """
    # Shared connection
    __connection = None

    def __init__(self):
        self.__connection = SpotifyAccessor.initialize()

    @property
    def get_connection(self):
        """Getter for __connection"""
        return self.__connection

    @classmethod
    def initialize(cls) -> spotipy.client.Spotify:
        """ Connect spotify api by SpotifyOAuth.

        Scope reference:    https://developer.spotify.com/documentation/general/guides/authorization/scopes/
            user-library-read
            playlist-modify-private
            user-read-recently-played   :    for get playlist information
            playlist-modify-public      :    for modify public playlist (remove songs from playlist)
            user-read-currently-playing :    for getting a current track

        Returns:
            __connection (spotipy.client.Spotify): spotify connection
        """
        if cls.__connection is not None:
            return cls.__connection

        config = Config().get_config()
        client_id = config['SPOTIPY']['SPOTIPY_CLIENT_ID']
        client_secret = config['SPOTIPY']['SPOTIPY_CLIENT_SECRET']
        redirect_uri = 'https://google.com'
        scope = 'user-library-read \
                 playlist-modify-private \
                 user-read-recently-played \
                 playlist-modify-public \
                 user-read-currently-playing'

        info('Start connecting Spotify')
        auth_manager = SpotifyOAuth(client_id=client_id,
                                    client_secret=client_secret,
                                    redirect_uri=redirect_uri,
                                    scope=scope,
                                    open_browser=False)

        try:
            # Connect spotify
            cls.__connection = spotipy.Spotify(auth_manager=auth_manager, language='en')
            info('Succeed in connecting Spotify...')
        except Exception as err:
            error_stack_trace(
                f"Fail to connect Sptify. error: {err}, \
                client_id: {client_id}, \
                client_secret: {client_secret}, \
                redirect_uri: {redirect_uri}, \
                scope: {scope}")

        return cls.__connection
