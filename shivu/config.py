class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "5909658683"
    sudo_users = "1881562083", "5909658683"
    GROUP_ID = -1002311769574
    TOKEN = ""
    mongo_url = "mongodb+srv://TEAMBABY01:UTTAMRATHORE09@cluster0.vmjl9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    PHOTO_URL = ["https://files.catbox.moe/sjzwp3.jpg", "https://files.catbox.moe/sjzwp3.jpg"]
    SUPPORT_CHAT = "iamvillain77"
    UPDATE_CHAT = "oldskoolgc"
    BOT_USERNAME = "Waifu_World_Robot"
    CHARA_CHANNEL_ID = "-1002311769574"
    api_id = "24061032"
    api_hash = "5ad029547f2eeb5a0b68b05d0db713be"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
