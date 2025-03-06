import os

BOT_TOKEN = os.environ.get("7897121009:AAFy2EsicIZarjiDfE7MmdLHo9y2QzaJChk", "")
API_ID = int(os.environ.get("27081859", ""))
API_HASH = os.environ.get("7ea9276cf33c62b75209abedf1b13f97", "")
LOG_CHANNEL = int(os.environ.get("-1002288434806", ""))
AUTH_USERS = set(int(x) for x in os.environ.get("6421713963", "").split())
DB_URL = os.environ.get("mongodb+srv://yanstokakunold:jEPsGsOBfML86IoA@cluster0.77zir.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", "")
DB_NAME = os.environ.get("BROADCASTBOT", "BroadcastBot")
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
