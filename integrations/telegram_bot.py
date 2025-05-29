# integrations/telegram_bot.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from agents.copybooster import melhorar_copy
from agents.reflexor import avaliar_resposta
from agents.deepagent import investigar

TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "7708281637:AAHaXP2SwoV1ct5IiVaTUwcEyf2QHxR-7uc")

# Comando de boas-vindas
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Olá! Eu sou o GPT Mestre Autônomo. Use /copy, /reflexor ou /deep.")

# Comando para gerar copy com emoção padrão
async def copy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = ' '.join(context.args)
    if not texto:
        await update.message.reply_text("⚠️ Envie um texto após o comando /copy.")
        return
    nova_copy, explicacao = melhorar_copy(texto, emocao='confiança', tipo='descricao')
    resposta = "📄 *Copy Gerada:*\n" + nova_copy + "\n\n💡 _" + explicacao + "_"
    await update.message.reply_text(resposta, parse_mode="Markdown")

# Comando para avaliar texto com o Reflexor
async def reflexor(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = ' '.join(context.args)
    if not texto:
        await update.message.reply_text("⚠️ Envie um texto após o comando /reflexor.")
        return
    avaliacao = avaliar_resposta(texto)
    nota = avaliacao.get("nota", 0)
    justificativa = avaliacao.get("justificativa", "")
    resposta = "🧠 *Reflexor:*\nNota " + str(nota) + "/10\n💬 " + justificativa
    await update.message.reply_text(resposta, parse_mode="Markdown")

# Comando para análise estratégica com DeepAgent
async def deep(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = ' '.join(context.args)
    if not texto:
        await update.message.reply_text("⚠️ Envie um texto após o comando /deep.")
        return
    resultado = investigar(texto, tipo='produto')
    mensagem = "🔎 *DeepAgent:*\n" + resultado
    await update.message.reply_text(mensagem, parse_mode="Markdown")

# Inicializador do bot
def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("copy", copy))
    app.add_handler(CommandHandler("reflexor", reflexor))
    app.add_handler(CommandHandler("deep", deep))

    print("✅ Bot rodando... Pressione Ctrl+C para parar.")
    app.run_polling()

if __name__ == "__main__":
    main()
