# suit_guardian versioning:
# <suit version updated>.<guardian version updated>.<hotfix>
__SUIT_VERSION__ = '0.2.8'
__GUARDIAN_VERSION__ = '1.2.0'
__HOTFIX__ = 0

__VERSION__ = u'{}.{}.{}'.format(
    __SUIT_VERSION__.replace('.', ''),
    __GUARDIAN_VERSION__.replace('.', ''),
    __HOTFIX__
)
