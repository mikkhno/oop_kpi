import telebot, wikipedia, re
# Setting the API-ID
bot = telebot.TeleBot('5606399410:AAFghKqT1JV0bWP_cghk87xOEElVZODyrm4')
# Setting the language
wikipedia.set_lang("en")


# Starting the bot.
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Write your word ->')


# Showing found information.
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, getwiki(message.text))


# Looking for an information about the given word.
@bot.message_handler(commands=["lookup"])
def getwiki(s):
    # Formatting, cleaning and pasting requested information.
    try:
        # Adding a page with requested meaning.
        ny = wikipedia.page(s)
        # Getting information(max. 1000 symbols).
        wikitext = ny.content[:1000]
        # Split sentences with dots.
        wiki_array = wikitext.split('.')
        # Removing extra sentences.
        wiki_array = wiki_array[:-1]
        # Creating empty variable for the text.
        wikitext2 = ''
        # Formatting text to avoid unexpected operations with attribution.
        for x in wiki_array:
            if not ('==' in x):
                # When we have a sentence more with 3 symbols, we are returning it with lost dots.
                if (len((x.strip())) > 3):
                        wikitext2 = wikitext2 + x + '.'
                else:
                    break
        # Deleting unnecessary elements from text.
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\{[^\{\}]*\}', '', wikitext2)
        # Returning formatted and cleaned information as a text.
        return wikitext2
        # Exception in case the information is not found.
    except Exception as e:
        return 'The meaning of the word you are looking for is not found.'


# Launching the bot.
bot.polling(none_stop=True, interval=0)
