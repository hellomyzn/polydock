"""Entory point"""
#########################################################
# Builtin packages
#########################################################

#########################################################
# 3rd party packages
#########################################################

#########################################################
# Own packages
#########################################################
from common.logging import initialize_logger
from common.config import Config


def main():
    config = Config().config
    lp = config["LOG"]["PATH"]
    initialize_logger("main", lp, "info")


if __name__ == "__main__":
    main()
