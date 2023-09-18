"""common.google_spreadsheet.gss_accessor"""
#########################################################
# Builtin packages
#########################################################

#########################################################
# 3rd party packages
#########################################################
import gspread
from oauth2client.service_account import ServiceAccountCredentials

#########################################################
# Own packages
#########################################################
from utils import Singleton
from common.config import Config
from common.logging import (
    info,
    error_stack_trace
)


class GssAccessor(Singleton):
    """
        Usage:
            1. put json file of your API key in src/src/json.
            2. put config below in src/common/config/config.ini
                - JSON_PATH
                - SHEET_KEY
                - SHEET_NAME

        Reference:
        - https://qiita.com/164kondo/items/eec4d1d8fd7648217935
        - https://www.cdatablog.jp/entry/2019/04/16/191006
    """
    # Shared connection
    connection = None

    def __init__(self):
        self.connect = GssAccessor.initialize()

    @classmethod
    def initialize(cls) -> gspread.client.Client:
        """Connect Google Spreadsheet

        Returns:
            connct: connection for google_spreadsheet
        """
        if cls.connection is not None:
            return cls.connection

        config = Config().get_config()
        json_path = config['GSS']['JSON_PATH']
        scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']

        info('Start connecting Google Spreadsheet')

        try:
            credentials = ServiceAccountCredentials.from_json_keyfile_name(json_path, scope)
            cls.connection = gspread.authorize(credentials)
            info('Succeed in connecting Google Spreadshee')

        except Exception as err:
            error_stack_trace(
                f"Fail to connect Google Spreadshee. error: {err}, json_path: {json_path}, scope: {scope}")

        return cls.connection
