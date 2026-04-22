from config import PLANS, ADMIN_ID
from database import add_user, get_user, set_plan

def register(bot):

    @bot.message_handler(commands=['start'])
    def start(m):
        add_user(m.from_user.id)

        text = "👋 أهلاً بك\n\nاختر خطتك:\n"
        for k, v in PLANS.items():
            text += f"\n{k} - {v['price']}"

        bot.send_message(m.chat.id, text)

    @bot.message_handler(func=lambda m: True, content_types=['text', 'photo'])
    def handler(m):
        user = get_user(m.from_user.id)

        if not user:
            add_user(m.from_user.id)
            user = get_user(m.from_user.id)

        # اختيار خطة
        if m.content_type == 'text' and m.text in PLANS:

            set_plan(m.from_user.id, m.text)

            bot.send_message(
                m.chat.id,
                f"✅ تم اختيار {m.text}\n💳 أرسل صورة التحويل للادمن"
            )

        # صورة تحويل
        elif m.content_type == 'photo':

    bot.forward_message(
        ADMIN_ID,
        m.chat.id,
        m.message_id
    )

    bot.send_message(
        ADMIN_ID,
        f"📩 طلب جديد من {m.from_user.id}\nالباقة: {user['plan']}"
    )

    bot.send_message(
        m.chat.id,
        "⏳ تم إرسال طلبك للمراجعة"
    ) 


