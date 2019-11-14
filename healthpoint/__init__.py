"""
      ___           ___       __   __         ___
|__| |__   /\  |     |  |__| |__) /  \ | |\ |  |
|  | |___ /~~\ |___  |  |  | |    \__/ | | \|  |

"""
VERSION = (0, 3, 0, 'final', 0)

__title__ = 'django-healthpoint'
__version_info__ = VERSION
__version__ = '.'.join(map(str, VERSION[:3])) + ('-{}{}'.format(
    VERSION[3], VERSION[4] or '') if VERSION[3] != 'final' else '')
__author__ = 'Raymond Penners'
__license__ = 'MIT'
__copyright__ = 'Copyright 2018-2019 Raymond Penners and contributors'
