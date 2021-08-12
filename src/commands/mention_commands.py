from vkbottle_types.objects import UsersUserXtrCounters
from src.utils import replace_string_username
from src.commands.base_commands import get_localization_with_choice
from src.utils import replace_string_username


async def string_with_user(
    localizationFile: str,
    user: UsersUserXtrCounters
) -> str:
    localizationStr: str = await get_localization_with_choice(localizationFile)
    return await replace_string_username(localizationStr, user.first_name)


async def string_with_everyone(localizationFile: str) -> str:
    return await get_localization_with_choice(localizationFile)
