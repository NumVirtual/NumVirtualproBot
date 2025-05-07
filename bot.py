import json
from telebot import TeleBot, types
from telebot.types import WebAppInfo

TOKEN = 8036648453:AAHa179J-r2obuOQYbLRMLTp-I76zq3cqLI
bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(msg):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton(
        "🎮 Abrir App",
        web_app=WebAppInfo(url="https://numvirtual.github.io/NumVirtualproBot/index.html")
    )
    markup.add(btn)
    bot.send_message(msg.chat.id, "¡Bienvenido! Abre tu mini‑app 👇", reply_markup=markup)

@bot.web_app_data_handler()
def handle_web_app_data(msg):
    data = json.loads(msg.web_app_data.data)
    action = data.get('action')
    chat_id = msg.chat.id

    if action === 'números' or action==='🔢':
        bot.send_message(chat_id, "🔢 Números disponibles:\n1) +1‑202‑555‑0135\n2) +44‑20‑7946‑0958")
    elif action==='compras' or action==='🛒':
        bot.send_message(chat_id, "🛒 Tus compras:\n• #12345 – USDT TRC20\n• #12346 – BTC")
    elif action==='pagos' or action==='💳':
        bot.send_message(chat_id, "💳 Métodos de pago:\nUSDT, BTC, BNB, TRX")
    else:
        bot.send_message(chat_id, "❓ Acción desconocida: " + action)

if __name__ == '__main__':
    print("🤖 Bot iniciado...")
    bot.infinity_polling()
