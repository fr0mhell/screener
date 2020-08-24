import vk_api
from configparser import RawConfigParser
import pyscreenshot
import uuid


config = RawConfigParser()
config.read_file(open('credentials.cfg'))

username = config.get('vk', 'user')
password = config.get('vk', 'password')
album = config.get('vk', 'album')

if __name__ == '__main__':
    vk_session = vk_api.VkApi(username, password)
    vk_session.auth()
    vk = vk_session.get_api()

    # grab fullscreen
    img = pyscreenshot.grab()
    filename = f'{uuid.uuid4()}.png'
    img.save(filename)

    upload = vk_api.VkUpload(vk_session)
    upload.photo(
        photos=[filename, ],
        album_id=album,
    )
