from src.utils import choose_file
from vkbottle.tools import PhotoMessageUploader, DocMessagesUploader
from vkbottle.api import API
from random import randint


async def get_photo(photo_path: str, vk_api: API) -> str:
    """Returns an attachment as a photo, uploaded on a server

    :param photo_path: Path to a photo
    :param vk_api: Api for a bot
    :returns: An attachment string
    :raises: TODO
    """
    msg_uploader: PhotoMessageUploader = PhotoMessageUploader(vk_api)
    upload_str = await msg_uploader.upload(photo_path)
    return upload_str


async def get_document(document_path: str, vk_api: API, pid: int) -> str:
    """Returns an attachment as a document, uploaded on a server

    :param document_path: Path to a document
    :param vk_api: Api for a bot
    :param peer_id: Peer_id of a chat for uploading the document to
    :returns: An attachment string
    :raises: TODO
    """
    msg_uploader: DocMessagesUploader = DocMessagesUploader(vk_api)
    _, doctype = document_path.split(".")
    upload_str = await msg_uploader.upload(f"dance-{randint(1, 999999)}.{doctype}",
                                           document_path, peer_id=pid)
    return upload_str
