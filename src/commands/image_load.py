from src.utils import choose_file
from vkbottle.tools import PhotoMessageUploader, DocMessagesUploader
from vkbottle.api import API
from random import randint
from aiofiles import open as aioopen


async def get_photo(photo_dir_path: str, vk_api: API) -> str:
    """Returns an attachment as a photo, uploaded on a server

    :param photo_dir_path: Path to a directory the photo is in
    :param vk_api: Api for a bot
    :returns: An attachment string
    :raises: TODO
    """
    msg_uploader: PhotoMessageUploader = PhotoMessageUploader(vk_api)
    random_file: str = await choose_file(photo_dir_path)
    upload_str = await msg_uploader.upload(random_file)
    return upload_str


async def get_document(document_dir_path: str, doc_type: str, vk_api: API, pid: int) -> str:
    """Returns an attachment as a document, uploaded on a server

    :param document_dir_path: Path to a directory the document is in
    :param doc_type: File extension of a document
    :param vk_api: Api for a bot
    :param peer_id: Peer_id of a chat for uploading the document to
    :returns: An attachment string
    :raises: TODO
    """
    msg_uploader: DocMessagesUploader = DocMessagesUploader(vk_api)
    random_file: str = await choose_file(document_dir_path)
    upload_str = await msg_uploader.upload(f"dance-{randint(1, 999999)}.{doc_type}",
                                           random_file, peer_id=pid)
    return upload_str
