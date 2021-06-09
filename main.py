from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.replykeyboardmarkup import ReplyKeyboardMarkup
from telegram.replykeyboardremove import ReplyKeyboardRemove
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth

#PORT = int(os.environ.get('PORT', 5000))
#gauth = GoogleAuth()
#gauth.CommandLineAuth()
#gauth.LocalWebserverAuth() 
#drive = GoogleDrive(gauth)

TOKEN = "1428504700:AAGWNviK8XYFYhDc-YFkRZdmUmiNpbehtVM"
updater = Updater(TOKEN, use_context=True)
keybordLayouts = {
    "main": [['السنة الأولى', 'السنة الثانية'], ['السنة الثالثة', 'السنة الرابعة']],
    "Year1": [['الفيزياء 2', 'التحليل الرياضي 2'], ['البرمجة 1', 'أسس الدارات الكهربائية'] , ['العودة']],
    "Year2": [['الدارات الكهربائية 2'] , ['أسس الهندسة الإلكترونية', 'الخوارزميات'], ['الدارات المنطقية', 'الرياضيات المتقطعة'] , ['العودة']],
    "Year3": [['الدارات الالكترونية 2', 'التحكم الآلي 2'], ['تحليل النظم', 'المعالجات'] ,['القياسات الالكترونية', 'أسس هندسة الاتصالات'] , ['العودة']],
    "Year4": [['معالجة الإشارة', 'التحكم اللاخطي'], ['هيك شي', 'نظم التشغيل '] , ['العودة']],
    "Choice": [['محاضرة' , 'ملحق'] , ['العودة']]
}
subjectsList = [
    'البرمجة 1' , 'التحليل الرياضي 2', 'الفيزياء 2' , 'أسس الدارات الكهربائية' 
    , 'الخوارزميات' , 'أسس الهندسة الإلكترونية', 'الدارات الكهربائية 2' , 'الدارات المنطقية' , 'الرياضيات المتقطعة'
    , 'التحكم الآلي 2' , 'الدارات الالكترونية 2', 'المعالجات' , 'تحليل النظم' , 'القياسات الالكترونية' , 'أسس هندسة الاتصالات'
    , 'التحكم اللاخطي' , 'معالجة الإشارة' , 'نظم التشغيل' , 'هيك شي'
]
sub = ""
#ON Public Server
#URL = ''
# ON LOCAL SERVER
URL = '/home/montazer/Documents/Programming/Python/RBCsSocialBot/'
URL1 = URL
MfileName = ''
folderName1 = ''
answer1 = ''
answer = ''

def start(update: Update, context: CallbackContext):
    kbd = ReplyKeyboardMarkup(keybordLayouts["main"])
    usrname = ''
    usrr = update.message.from_user['username']
    id = update.message.chat_id
    print(id)
    if (id == 'Umna3bbar'):
        usrname = ' يمنى '
    elif(id == 21338789):
        usrname = 'نور'
    elif(id == 'Bouthina_Ammar'):
        usrname = 'بثينة'
    elif(id == 'RamaShell'):
        usrname = 'راما'
    elif(id == 'Rnoom_k'):
        usrname = 'رنيم'
    elif(id == 'ayatbkr27'):
        usrname = 'آيات'
    else:
        usrname = 'تسنيم او نور او مريم 😂😂😂'
    update.message.reply_text(text = "مرحباً "+usrname+' ❤️' , reply_markup=None)
    update.message.reply_text(text = "اختر السنة:" , reply_markup=kbd)


def downloader(update, context):
    context.bot.get_file(update.message.document).download(custom_path=URL1)
    print("Downloaded!")
    #update
    #reply_markup = ReplyKeyboardRemove()
    update.message.reply_text(text=':التسمية المعتمدة' , reply_markup=None)
    update.message.reply_text(text=MfileName , reply_markup=None)
    update.message.reply_text(text="سأرسل لك الآن الملف بالتسمية المعتمدة:", reply_markup=None)
    chat_id = update.message.chat_id
    context.bot.sendDocument(chat_id = chat_id,document = open(URL+MfileName , 'rb'))
    #update.message.reply_text(text="الرجاء الانتظار ريثما يتم رفع الملف على منصة Drive", reply_markup=None)
    #upload(MfileName , URL1 , sub)
    #print("Uploaded!")
    update.message.reply_text(text="تم رفع الملف على منصة Drive", reply_markup=None)
    
    
def echo(update: Update, context: CallbackContext):
    global answer
    global answer1
    temp = update.message.text
    if temp == 'محاضرة' or temp == 'ملحق':
        answer1 = temp
        reply_markup = ReplyKeyboardRemove()
        if answer1 == 'محاضرة':
            print('lec')
            okay = False
            for subject in subjectsList:
                if answer == subject: 
                    okay = True
                    global sub
                    sub = subject
                    update.message.reply_text(text="أرسل رقم محاضرة "+answer, reply_markup=reply_markup)
                                  
        elif answer1 == 'ملحق':
            print('non lec')
            okay = False
            for subject in subjectsList:
                if answer == subject: 
                    okay = True
                    sub = subject
                    update.message.reply_text(text=" أرسل رقم ملحق "+answer+' على شكل تعداد نصي، مثال: الأول، الثاني مع مراعاة قواعد الإملاء باليز 😂', reply_markup=reply_markup)
    
    else:
        answer = temp
        if answer == 'السنة الأولى':
            kbd = ReplyKeyboardMarkup(keybordLayouts["Year1"])
            update.message.reply_text(text = "اختر المادة:" , reply_markup=kbd)

        elif answer == 'السنة الثانية':
            kbd = ReplyKeyboardMarkup(keybordLayouts["Year2"])
            update.message.reply_text(text = "اختر المادة:" , reply_markup=kbd)

        elif answer == 'السنة الثالثة':
            kbd = ReplyKeyboardMarkup(keybordLayouts["Year3"])
            update.message.reply_text(text = "اختر المادة:" , reply_markup=kbd)

        elif answer == 'السنة الرابعة':
            kbd = ReplyKeyboardMarkup(keybordLayouts["Year4"])
            update.message.reply_text(text = "اختر المادة:" , reply_markup=kbd)

        elif answer == 'العودة':
            kbd = ReplyKeyboardMarkup(keybordLayouts["main"])
            update.message.reply_text(text = "اختر السنة:" , reply_markup=kbd)

        else:
            subFound = False
            for subb in subjectsList:
                if answer == subb:
                    print('subs here')
                    kbd = ReplyKeyboardMarkup(keybordLayouts["Choice"])
                    update.message.reply_text(text = "محاضرة أم ملحق؟" , reply_markup=kbd)
                    subFound = True
                    
            if subFound == False:
                if answer1 == 'محاضرة':
                    for cnt in range(50):
                        if int(answer) == cnt:
                            global URL1
                            global MfileName
                            MfileName = sub+' - RBCs lec '
                            if cnt<10:
                                MfileName = MfileName+'0'
                            MfileName=MfileName+(str(cnt))+".pdf"
                            URL1 = URL+MfileName
                            update.message.reply_text(text="أرسل ملف "+sub+" المحاضرة "+str(cnt), reply_markup=None)
                elif answer1 == 'ملحق':
                    MfileName=sub+' - الملحق '+answer+'.pdf'
                    URL1 = URL+MfileName
                    update.message.reply_text(text="أرسل ملف "+sub+" الملحق "+answer, reply_markup=None)
            
    pass

'''
def upload(fileName , filePath , folderName):
 	folders = drive.ListFile({'q': "title='" + folderName + "' and mimeType='application/vnd.google-apps.folder' and trashed=false"}).GetList()
 	for folder in folders:
  	 if folder['title'] == folderName:
   	  file2 = drive.CreateFile({'parents': [{'id': folder['id']}] , 'title': fileName}) #file name
   	  file2.SetContentFile(filePath) #path to file
   	  file2.Upload()
'''

dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.regex(r""), echo))
dp.add_handler(MessageHandler(Filters.document, downloader))

updater.start_polling()