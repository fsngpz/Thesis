from pathlib import Path
import telegram
from telegram import *
from telegram.ext import *
import SQLProcess
import SaveToMacro
import decodeQR
from datetime import datetime
from datetime import timedelta
import runMacro
from keras.models import model_from_json
import os
from tensorflow.keras.preprocessing import image
import numpy as np
from urllib import request
from io import BytesIO
from PIL import Image

LBO = "LBO"
PATROL = "PATROL"

global lbopatrol, status
Name= {}
Status= {}
LotSize= {}
LotNum= {}
LBOPATROL= {}
SampleSize= {}
LineLead = {}
MachineNum = {}
Major = {}
DC = {}
RA = {}
RM = {}
KPK = {}
menu = {}
pathPPT = {}
fileName = {}
partNum = {}
filesize = {}
serialNum = {}
deeplearning = {}
result = {}

pathSchedule = r"\\Apckranefa01pv\apckr001\CKR\APCKRMFLPT001P\G_Drive\Groups\QA\SQT by QE\MODULES\TeleBot\QC Molding System for Telebot.xlsm"
allowedUsernames = ['fsngpz', 'Salsatz15']
telegram.ReplyKeyboardRemove()

def start(update, context):
    Name[f"{update.effective_user.username}"] = ""
    Status[f"{update.effective_user.username}"] = ""
    LotSize[f"{update.effective_user.username}"] = ""
    LotNum[f"{update.effective_user.username}"] = ""
    LBOPATROL[f"{update.effective_user.username}"] = ""
    SampleSize[f"{update.effective_user.username}"] = ""
    LineLead[f"{update.effective_user.username}"] = ""
    MachineNum[f"{update.effective_user.username}"] = ""
    Major[f"{update.effective_user.username}"] = ""
    DC[f"{update.effective_user.username}"] = ""
    RA[f"{update.effective_user.username}"] = ""
    RM[f"{update.effective_user.username}"] = ""
    KPK[f"{update.effective_user.username}"] = ""
    menu[f"{update.effective_user.username}"] = ""
    pathPPT[f"{update.effective_user.username}"] = ""
    fileName[f"{update.effective_user.username}"] = ""
    partNum[f"{update.effective_user.username}"] = ""
    filesize[f"{update.effective_user.username}"] = ""
    serialNum[f"{update.effective_user.username}"] = ""
    deeplearning[f"{update.effective_user.username}"] = ""
    result[f"{update.effective_user.username}"] = ""


    if update.effective_chat.username not in allowedUsernames:
        print(update.effective_user.username)
        context.bot.send_message(reply_markup=ReplyKeyboardRemove() ,chat_id=update.effective_chat.id, text="You are not allowed to use this bot")
        return
    else:
        Status[f"{update.effective_user.username}"] = ''
        LotSize[f"{update.effective_user.username}"] = ''
        LotNum[f"{update.effective_user.username}"] = ''
        LBOPATROL[f"{update.effective_user.username}"] = ''
        SampleSize[f"{update.effective_user.username}"] = ''
        LineLead[f"{update.effective_user.username}"] = ''
        MachineNum[f"{update.effective_user.username}"] = ''
        Major[f"{update.effective_user.username}"] = ''
        DC[f"{update.effective_user.username}"] = ''
        RA[f"{update.effective_user.username}"] = ''
        RM[f"{update.effective_user.username}"] = ''
        KPK[f"{update.effective_user.username}"] = ''
        menu[f"{update.effective_user.username}"] = ''
        pathPPT[f'{update.effective_user.username}'] = ''
        if not menu or menu[f"{update.effective_user.username}"] == '':
            context.bot.send_message(chat_id=update.effective_chat.id, parse_mode='Markdown',
                                     text="Hi, Welcome to *Quality Department* system!")
            # update.message.reply_text(parse_mode='Markdown',
            #                           text="Please choose which system do you want to execute")
            buttons = [[KeyboardButton('Incoming Quality Control')], [KeyboardButton('Quality Control')]]
            context.bot.send_message(parse_mode='Markdown', chat_id=update.effective_chat.id,
                                     text="Please choose which _system_ do you want to execute",
                                     reply_markup=ReplyKeyboardMarkup(buttons))
        elif menu[f"{update.effective_user.username}"] == 'Incoming Quality Control':
            buttons = [[KeyboardButton('Help')], [KeyboardButton('Exit')]]
            context.bot.send_message(reply_markup=ReplyKeyboardMarkup(buttons), chat_id=update.effective_chat.id,
                                     parse_mode='Markdown',
                                     text=f"Hello {update.effective_user.first_name}, Welcome to *Incoming Quality Control Menu System*!")
            update.message.reply_text(parse_mode='Markdown',
                                      text="To find the latest report of the Incoming, please send me Picture or File of the *GRN*")
            menu[f"{update.effective_user.username}"] = "Incoming Quality Control"
            print(menu)
        elif menu[f"{update.effective_user.username}"] == 'Quality Control':
            buttons = [[KeyboardButton('PASS'), KeyboardButton('FAIL')], [KeyboardButton('BACK')]]
            context.bot.send_message(chat_id=update.effective_chat.id, parse_mode='Markdown',
                                     text=f"Hello {update.effective_user.first_name}, To find the PPT File of Inspection file please send me the photo of *LKP* :)!",
                                     reply_markup=ReplyKeyboardMarkup(buttons))
            menu[f"{update.effective_user.username}"] = "Quality Control"
            print(menu)


def message(update, context):

    update.message.reply_text(parse_mode='Markdown',
                              text="Sorry I dont understand what you mean :(")

def command_handler(update, context):
    update.message.reply_text(f"Sorry I dont understand command {update.message.text} :(")

def Pass(update, context):
    Status[f"{update.effective_user.username}"] = "PASS"
    context.bot.send_message(parse_mode='Markdown', chat_id=update.effective_chat.id,
                             text="Please select the Button from the Top!",
                             reply_markup=telegram.ReplyKeyboardRemove())
    buttons = [[InlineKeyboardButton("LBO", callback_data="LBO")],
               [InlineKeyboardButton("Patrol", callback_data="Patrol")]]
    context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons),
                             text="Please choose either it's LBO or PATROL")
    buttons = [[InlineKeyboardButton("1", callback_data="1"), InlineKeyboardButton("2", callback_data="2")],
               [InlineKeyboardButton("3", callback_data="3"), InlineKeyboardButton("4", callback_data="4")]]
    context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons),
                             text="Please choose the LOT#")
    buttons = [[InlineKeyboardButton("13", callback_data="13"), InlineKeyboardButton("20", callback_data="20")],
               [InlineKeyboardButton("32", callback_data="32")],
               [InlineKeyboardButton("50", callback_data="50"), InlineKeyboardButton("80", callback_data="80")]]
    context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons),
                             text="Please choose the sample size")
    buttons = [
        [InlineKeyboardButton("51-90", callback_data="51-90"), InlineKeyboardButton("91-150", callback_data="91-150")],
        [InlineKeyboardButton("151-280", callback_data="151-280"),
         InlineKeyboardButton("280-500", callback_data="280-500")],
        [InlineKeyboardButton("281-500", callback_data="281-500"),
         InlineKeyboardButton("501-1200", callback_data="501-1200")],
        [InlineKeyboardButton("601-1200", callback_data="601-1200"),
         InlineKeyboardButton("1201-3200", callback_data="1201-3200")], ]
    context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons),
                             text="Please choose the LOT Size")
    buttons = [[InlineKeyboardButton("Neti", callback_data="209056"),
                InlineKeyboardButton("Yuliawati", callback_data="136618")],
               [InlineKeyboardButton("Tri Purwanti", callback_data="171564"),
                InlineKeyboardButton("Muhammad Said", callback_data="410426")],
               [InlineKeyboardButton("Parman", callback_data="308071"),
                InlineKeyboardButton("Vivi", callback_data="313687")],
               [InlineKeyboardButton("Sutiah", callback_data="504246"),
                InlineKeyboardButton("Misran", callback_data="207184")],
               [InlineKeyboardButton("Slamet", callback_data="206180"),
                InlineKeyboardButton("Wiwi", callback_data="703179")],
               [InlineKeyboardButton("Rosmawati", callback_data="143801"),
                InlineKeyboardButton("Aan", callback_data="363898")],
               [InlineKeyboardButton("Muladsih", callback_data="128885"),
                InlineKeyboardButton("Dede Trimono", callback_data="353601")],
               [InlineKeyboardButton("Ira", callback_data="116002"),
                InlineKeyboardButton("Tri Widyaningsih", callback_data="186102")],
               [InlineKeyboardButton("Kosim", callback_data="409004"),
                InlineKeyboardButton("Rina Sugiarti", callback_data="903332")],
               [InlineKeyboardButton("Ali Wahyudi", callback_data="407097"),
                InlineKeyboardButton("Venny Anjarwati", callback_data="377498")],
               [InlineKeyboardButton("Wahyuni", callback_data="104852"),
                InlineKeyboardButton("Mulyani", callback_data="307021")],
               [InlineKeyboardButton("Lukik Dwi", callback_data="427464"),
                InlineKeyboardButton("Intan", callback_data="903127")],
               [InlineKeyboardButton("Umi", callback_data="183488")], ]
    context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons),
                             text="Please select the Lineleader")
    context.bot.send_message(chat_id=update.effective_chat.id, parse_mode='Markdown',
                             text="Type */exit* if you want to exit the Key In!")
def Fail(update, context):
    Status[f"{update.effective_user.username}"] = "FAIL"
    context.bot.send_message(parse_mode='Markdown', chat_id=update.effective_chat.id,
                             text="Please select the Button from the Top!",
                             reply_markup=telegram.ReplyKeyboardRemove())
    buttons = [[InlineKeyboardButton("LBO", callback_data="LBO")],
               [InlineKeyboardButton("Patrol", callback_data="Patrol")]]
    context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons),
                             text="Please choose either it's LBO or PATROL")
    buttons = [[InlineKeyboardButton("1", callback_data="1"), InlineKeyboardButton("2", callback_data="2")],
               [InlineKeyboardButton("3", callback_data="3"), InlineKeyboardButton("4", callback_data="4")]]
    context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons),
                             text="Please choose the LOT#")
    buttons = [[InlineKeyboardButton("13", callback_data="13"), InlineKeyboardButton("20", callback_data="20")],
               [InlineKeyboardButton("32", callback_data="32")],
               [InlineKeyboardButton("50", callback_data="50"), InlineKeyboardButton("80", callback_data="80")]]
    context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons),
                             text="Please choose the sample size")
    buttons = [[InlineKeyboardButton("51-90", callback_data="51-90"),
                InlineKeyboardButton("91-150", callback_data="91-150")],
               [InlineKeyboardButton("151-280", callback_data="151-280"),
                InlineKeyboardButton("280-500", callback_data="280-500")],
               [InlineKeyboardButton("281-500", callback_data="281-500"),
                InlineKeyboardButton("501-1200", callback_data="501-1200")],
               [InlineKeyboardButton("601-1200", callback_data="601-1200"),
                InlineKeyboardButton("1201-3200", callback_data="1201-3200")], ]
    context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons),
                             text="Please choose the LOT Size")
    buttons = [[InlineKeyboardButton("Neti", callback_data="209056"),
                InlineKeyboardButton("Yuliawati", callback_data="136618")],
               [InlineKeyboardButton("Tri Purwanti", callback_data="171564"),
                InlineKeyboardButton("Muhammad Said", callback_data="410426")],
               [InlineKeyboardButton("Parman", callback_data="308071"),
                InlineKeyboardButton("Vivi", callback_data="313687")],
               [InlineKeyboardButton("Sutiah", callback_data="504246"),
                InlineKeyboardButton("Misran", callback_data="207184")],
               [InlineKeyboardButton("Slamet", callback_data="206180"),
                InlineKeyboardButton("Wiwi", callback_data="703179")],
               [InlineKeyboardButton("Rosmawati", callback_data="143801"),
                InlineKeyboardButton("Aan", callback_data="363898")],
               [InlineKeyboardButton("Muladsih", callback_data="128885"),
                InlineKeyboardButton("Dede Trimono", callback_data="353601")],
               [InlineKeyboardButton("Ira", callback_data="116002"),
                InlineKeyboardButton("Tri Widyaningsih", callback_data="186102")],
               [InlineKeyboardButton("Kosim", callback_data="409004"),
                InlineKeyboardButton("Rina Sugiarti", callback_data="903332")],
               [InlineKeyboardButton("Ali Wahyudi", callback_data="407097"),
                InlineKeyboardButton("Venny Anjarwati", callback_data="377498")],
               [InlineKeyboardButton("Wahyuni", callback_data="104852"),
                InlineKeyboardButton("Mulyani", callback_data="307021")],
               [InlineKeyboardButton("Lukik Dwi", callback_data="427464"),
                InlineKeyboardButton("Intan", callback_data="903127")],
               [InlineKeyboardButton("Umi", callback_data="183488")], ]
    context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons),
                             text="Please select the Lineleader")
    context.bot.send_message(chat_id=update.effective_chat.id, parse_mode = 'Markdown', text="Type */exit* if you want to exit the Key In!")


def DL(context, update):
    print("udah masuk DL")
    filepath = photo.filepath
    print(filepath)
    response = request.urlopen(filepath).read()
    img = Image.open(BytesIO(response)).resize((200, 200))

    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights("model.h5")
    print("Loaded model from disk")

    ###
    X = image.img_to_array(img)
    X = np.expand_dims(X, axis=0)
    images = np.vstack([X])
    val = loaded_model.predict(images)
    classify = ""
    if val == 0:
        classify = "FAIL"
        context.bot.send_message(chat_id=update.effective_chat.id, parse_mode='Markdown',
                                 text=f"The part is *{classify}*. Please continue to Key-In the data")
        result[f'{update.effective_user.username}'] = classify
        deeplearning[f'{update.effective_user.username}'] = ""
        Fail(update, context)
    else:
        classify = "PASS"
        context.bot.send_message(chat_id=update.effective_chat.id, parse_mode='Markdown',
                                 text=f"The part is *{classify}*. Please continue to Key-In the data")
        result[f'{update.effective_user.username}'] = classify
        deeplearning[f'{update.effective_user.username}'] = ""
        Pass(update, context)


def photo(update: Update, context: CallbackContext):
    if not menu or menu[f"{update.effective_user.username}"] == '':
        context.bot.send_message(chat_id=update.effective_chat.id, text="You are not selecting any menu!")
        context.bot.send_message(chat_id=update.effective_chat.id, parse_mode='Markdown',
                                 text="Please type */start* to choose the Menu")

    elif menu[f"{update.effective_user.username}"] == "Quality Control":
        try:
            print(update)
            obj = context.bot.getFile(file_id=update.message.photo[-1].file_id)
            print(obj)
            filepath = obj['file_path']
            print(filepath)

            if not deeplearning or deeplearning[f"{update.effective_user.username}"] == "":
                print("Kosong")
                update.message.reply_text(parse_mode='MarkdownV2',
                                          text="_Please wait while we're finding the PPT of the Inspection\.\.\._")

            elif deeplearning[f'{update.effective_user.username}'] == 'Yes':
                update.message.reply_text(parse_mode='MarkdownV2',
                                          text="_Wait a second while the system determining whether"
                                               "the part is PASS or FAIL_")

                photo.filepath = filepath
                DL(context, update)
                return

            qr = decodeQR.process(menu[f"{update.effective_user.username}"], filepath)
            print("The QR is:", qr)
            if qr is None:
                update.message.reply_text(parse_mode='MarkdownV2',
                                          text="*Sorry, the Photo/LKP that you sent is not valid\.\.\.*")
                context.bot.send_message(parse_mode='Markdown', chat_id=update.effective_chat.id,
                                         text="_Please send me another Photo/LKP :)_")
            else:
                partNum[f'{update.effective_user.username}'] = qr[0]
                serialNum[f'{update.effective_user.username}'] = qr[1]
                print("Part Number :", partNum[f'{update.effective_user.username}'])
                molding = SQLProcess.qcmold(partNum[f'{update.effective_user.username}'])
                print(molding)
                if molding is None:
                    update.message.reply_text(parse_mode='Markdown', text="`This part has no Inspection!`")
                    update.message.reply_text(parse_mode='Markdown', text="`Please send me another LKP!`")
                    deeplearning[f"{update.effective_user.username}"] = ""
                    return

                elif molding[0] is not None and molding[1] == '':
                    buttons = [[KeyboardButton('PASS'), KeyboardButton('FAIL')], [KeyboardButton('BACK')]]
                    update.message.reply_text(parse_mode='Markdown',
                                              text="`This Part is ` *Critical* ` but does not have Inspection File`",
                                              reply_markup=ReplyKeyboardMarkup(buttons))
                elif molding[0] is not None and molding[1] is not None:
                    pathPPT[f'{update.effective_user.username}'] = molding[1]
                    fileName[f'{update.effective_user.username}'] = pathPPT[f'{update.effective_user.username}'][-10::]
                    update.message.reply_text(parse_mode='Markdown',
                                              text=f'_Yeay, We have found the File for Part Number_ *{partNum[f"{update.effective_user.username}"]}*')
                    update.message.reply_text(parse_mode='Markdown',
                                              text=f'The PPT file of this Part is refering to *{fileName[f"{update.effective_user.username}"]}*')
                    buttons = [[KeyboardButton('Yes')], [KeyboardButton('No')]]
                    context.bot.send_message(parse_mode='Markdown', chat_id=update.effective_chat.id,
                                             text='Do you want me to send the PPT file?',
                                             reply_markup=ReplyKeyboardMarkup(buttons))
                deeplearning[f'{update.effective_user.username}'] = "Yes"
        except telegram.error.TimedOut:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="_We are failed to get the_ *photo*, due to Timed Out error...")
            context.bot.send_message(chat_id=update.effective_chat.id, text="_Please re-send the photo!_")
        except Exception as e:
            print(str(e))

def file(update: Update, context: CallbackContext):
    print(menu)
    MachineNum[f"{update.effective_user.username}"] = ''
    if not menu or menu[f"{update.effective_user.username}"] == '':
        context.bot.send_message(chat_id = update.effective_chat.id, text="You are not selecting any menu!")
        context.bot.send_message(chat_id=update.effective_chat.id, parse_mode = 'Markdown', text="Please type */start* to choose the Menu")
    elif menu[f"{update.effective_user.username}"] == "Incoming Quality Control":
        try:
            update.message.reply_text(parse_mode='MarkdownV2',
                                      text="_Please wait while we're finding the report of the Incoming\.\.\._")
            print(update)
            obj = context.bot.getFile(file_id=update.message.document.file_id)
            print(obj)
            filepath = obj['file_path']
            print(filepath)
            qr = decodeQR.process(menu[f"{update.effective_user.username}"], filepath)
            print(qr)
            if qr is None:
                update.message.reply_text(parse_mode='MarkdownV2',
                                          text="*Sorry, the Photo/GRN that you sent is not valid\.\.\.*")
                context.bot.send_message(parse_mode='Markdown', chat_id=update.effective_chat.id,
                                         text="_Please send me another Photo/GRN :)_")
            else:
                print(qr[0])
                partnum = qr[2].find('-')
                res = qr[2][:partnum] + '\\' + qr[2][partnum:]
                suppclass = SQLProcess.suppclass(qr[1])
                pn = qr[2]
                sc = qr[1]
                status = suppclass[0]
                sclass = suppclass[1]
                print(status, "|", sclass)
                if status.lower() == 'certified':
                    print('CERTIFIED')
                    subcom = SQLProcess.subcom(qr[2])
                    print(subcom)
                    if subcom is None:
                        update.message.reply_text(parse_mode='MarkdownV2',
                                                  text="*Sorry, We cannot find the report for this GRN\!*")
                    else:
                        print(subcom)

                        materialrisk = SQLProcess.materialrisk(subcom[0], subcom[1])
                        risklevel = SQLProcess.risklevel(sclass, materialrisk[0], materialrisk[1])

                        result = SQLProcess.report(qr[2], risklevel[0], risklevel[1])
                        freqHE = str(risklevel[0])
                        freqPH = str(risklevel[1])

                        print(len(freqHE), len(freqPH))
                        if len(freqHE) > 3 and len(freqPH) > 3:
                            # Every Incoming
                            print("#Every Incoming")
                            RLHE = materialrisk[0]
                            RLPH = materialrisk[1]

                            # testHE = risklevel[0]
                            # testPH = risklevel[1]
                            testHE = freqHE
                            testPH = freqPH

                            batchHE = '-'
                            testinHE = '-'
                            dayHE = '-'

                            batchPH = '-'
                            testinPH = '-'
                            dayPH = '-'

                            LRPH = '-'
                            LRHE = '-'

                        elif len(freqHE) <= 3 and len(freqPH) <= 3:
                            print("HE:", freqHE, "\nPH:", freqPH)
                            result = SQLProcess.report(qr[2], risklevel[0], risklevel[1])
                            RLHE = materialrisk[0]
                            RLPH = materialrisk[1]
                            print(RLHE, RLPH)

                            testHE = str(risklevel[0]) + ' Days'
                            testPH = str(risklevel[1]) + ' Days'
                            if RLPH == 'N/A' and RLHE == 'N/A':
                                testHE = '-'
                                testPH = '-'
                            elif RLHE == 'N/A':
                                testHE = '-'
                            elif RLPH == 'N/A':
                                testPH = '-'
                            else:
                                testHE = str(risklevel[0]) + ' Days'
                                testPH = str(risklevel[1]) + ' Days'

                            batchHE = result[0]
                            testinHE = result[1]
                            dayHE = str(result[2]) + ' Days'

                            batchPH = result[3]
                            testinPH = result[4]
                            dayPH = str(result[5]) + ' Days'

                            LRPH = result[6]
                            LRHE = result[7]
                        elif len(freqHE) > 3 and len(freqPH) <= 3:
                            # HE Periodical, PH Every Incoming
                            testfreq = list(risklevel)
                            print(testfreq)
                            testfreq[0] = 0
                            risklevel = tuple(testfreq)
                            print(risklevel)

                            print(risklevel[0])
                            print("HE: Every Incoming", "\nPH: ", freqPH)
                            result = SQLProcess.report(qr[2], risklevel[0], risklevel[1])
                            RLHE = materialrisk[0]
                            RLPH = materialrisk[1]

                            testHE = freqHE
                            testPH = str(risklevel[1]) + ' Days'
                            batchHE = '-'
                            testinHE = '-'
                            dayHE = '-'

                            batchPH = result[3]
                            testinPH = result[4]
                            dayPH = str(result[5]) + ' Days'

                            LRPH = result[6]
                            LRHE = '-'
                        elif len(freqHE) <= 3 and len(freqPH) > 3:
                            # HE Every Incoming, PH Periodical
                            testfreq = list(risklevel)
                            print(testfreq)
                            testfreq[1] = 0
                            risklevel = tuple(testfreq)
                            print(risklevel)
                            print("HE:", freqHE, "PH Every Incoming")
                            result = SQLProcess.report(qr[2], risklevel[0], risklevel[1])
                            RLHE = materialrisk[0]
                            RLPH = materialrisk[1]

                            testHE = str(risklevel[0]) + ' Days'
                            testPH = freqPH
                            batchHE = result[0]
                            testinHE = result[1]
                            dayHE = str(result[2]) + ' Days'

                            batchPH = '-'
                            testinPH = '-'
                            dayPH = '-'

                            LRPH = '-'
                            LRHE = result[7]

                        print('BATCH HE:', batchHE)
                        print('HE Test in:', testinHE)
                        print('HE DAY:', dayHE)
                        print('BATCH HE:', batchPH)
                        print('HE Test in:', testinPH)
                        print('HE DAY:', dayPH)
                        update.message.reply_text(parse_mode='MarkdownV2',
                                                  text="Here is the result of your Incoming report\n\n" +
                                                       f'`Supplier Class: `*_ __{str(qr[1])}___*\n\n' +
                                                       f'`Part Number:` *__{str(res)}__*\n\n ' +
                                                       f"`Certified Class {sclass}`\n\n " +
                                                       "`Phthalate`\n" +
                                                       f"`-Risk Level: {RLPH}`\n" +
                                                       f"`-Test Frequent: {testPH}`\n" +
                                                       "`-Report:`\n" +
                                                       f"```python Batch\#: {batchPH}```\n" +
                                                       f"```python Latest Report: {LRPH}```\n" +
                                                       f"```python Need Test at: {testinPH}```\n" +
                                                       f"```python In: {dayPH}```\n\n" +
                                                       "`Heavy Element`\n" +
                                                       f"`-Risk Level: {RLHE}`\n" +
                                                       f"`-Test Frequent: {testHE}`\n" +
                                                       "`-Report:`\n" +
                                                       f"```python Batch\#: {batchHE}```\n" +
                                                       f"```python Latest Report: {LRHE}```\n" +
                                                       f"```python Need Test at: {testinHE}```\n" +
                                                       f"```python In: {dayHE}```\n\n"

                                                  )

                elif 'subcon' in status.lower():
                    print('SUBCON')
                    # update.message.reply_text(parse_mode='MarkdownV2',
                    #                           text="*Subcontractor is underdevelopment\!*")
                    subcom = SQLProcess.subcom(qr[2])
                    print("SUBCOM: ", subcom)
                    if subcom is None:
                        context.bot.send_message(chat_id=update.effective_chat.id,
                                                 text="Sorry, we cannot found the *Commodity* and "
                                                      "*Subcommodity* based on the data that you sent to us!",
                                                 parse_mode="Markdown")
                        context.bot.send_message(chat_id=update.effective_chat.id,
                                                 text="Please send me another data... "
                                                      "but before you sent the text to me, please double check the data :)",
                                                 parse_mode="Markdown")
                        return
                    materialrisk = SQLProcess.materialrisk(subcom[0], subcom[1])
                    print("Material Risk : ", materialrisk)
                    tipeClass = SQLProcess.typeClass(subcom[0], subcom[1])
                    print(tipeClass)
                    risklevelSubcon = SQLProcess.risklevelSubcon(sclass, materialrisk[0], materialrisk[1])
                    print(risklevelSubcon)
                    result = SQLProcess.report(qr[2], risklevelSubcon[0], risklevelSubcon[1])
                    freqHE = str(risklevelSubcon[0])
                    freqPH = str(risklevelSubcon[1])
                    print(len(freqHE), len(freqPH))
                    print("RLHE:", freqHE, "; RLPH:", freqPH)
                    #tipeClass = "1"
                    if tipeClass == "1":

                        if len(freqHE) > 3 and len(freqPH) > 3:
                            # Every Incoming
                            print("#Every Incoming")
                            RLHE = materialrisk[0]
                            RLPH = materialrisk[1]

                            # testHE = risklevel[0]
                            # testPH = risklevel[1]
                            testHE = freqHE
                            testPH = freqPH

                            batchHE = '-'
                            testinHE = '-'
                            dayHE = '-'

                            batchPH = '-'
                            testinPH = '-'
                            dayPH = '-'

                            LRPH = '-'
                            LRHE = '-'

                        elif len(freqHE) <= 3 and len(freqPH) <= 3:
                            print("HE:", freqHE, "\nPH:", freqPH)
                            result = SQLProcess.report(qr[2], risklevelSubcon[0], risklevelSubcon[1])
                            RLHE = materialrisk[0]
                            RLPH = materialrisk[1]
                            print(RLHE, RLPH)

                            testHE = str(risklevelSubcon[0]) + ' Days'
                            testPH = str(risklevelSubcon[1]) + ' Days'
                            if RLPH == 'N/A' and RLHE == 'N/A':
                                testHE = '-'
                                testPH = '-'
                            elif RLHE == 'N/A':
                                testHE = '-'
                            elif RLPH == 'N/A':
                                testPH = '-'
                            else:
                                testHE = str(risklevelSubcon[0]) + ' Days'
                                testPH = str(risklevelSubcon[1]) + ' Days'

                            batchHE = result[0]
                            testinHE = result[1]
                            dayHE = str(result[2]) + ' Days'

                            batchPH = result[3]
                            testinPH = result[4]
                            dayPH = str(result[5]) + ' Days'

                            LRPH = result[6]
                            LRHE = result[7]
                        elif len(freqHE) > 3 and len(freqPH) <= 3:
                            # HE Periodical, PH Every Incoming
                            testfreq = list(risklevelSubcon)
                            print(testfreq)
                            testfreq[0] = 0
                            risklevel = tuple(testfreq)
                            print(risklevel)

                            print(risklevel[0])
                            print("HE: Every Incoming", "\nPH: ", freqPH)
                            result = SQLProcess.report(qr[2], risklevel[0], risklevel[1])
                            RLHE = materialrisk[0]
                            RLPH = materialrisk[1]

                            testHE = freqHE
                            testPH = str(risklevel[1]) + ' Days'
                            batchHE = '-'
                            testinHE = '-'
                            dayHE = '-'

                            batchPH = result[3]
                            testinPH = result[4]
                            dayPH = str(result[5]) + ' Days'

                            LRPH = result[6]
                            LRHE = '-'
                        elif len(freqHE) <= 3 and len(freqPH) > 3:
                            # HE Every Incoming, PH Periodical
                            testfreq = list(risklevelSubcon)
                            print(testfreq)
                            testfreq[1] = 0
                            risklevel = tuple(testfreq)
                            print(risklevel)
                            print("HE:", freqHE, "PH Every Incoming")
                            result = SQLProcess.report(qr[2], risklevel[0], risklevel[1])
                            RLHE = materialrisk[0]
                            RLPH = materialrisk[1]

                            testHE = str(risklevel[0]) + ' Days'
                            testPH = freqPH
                            batchHE = result[0]
                            testinHE = result[1]
                            dayHE = str(result[2]) + ' Days'

                            batchPH = '-'
                            testinPH = '-'
                            dayPH = '-'

                            LRPH = '-'
                            LRHE = result[7]

                        print('BATCH HE:', batchHE)
                        print('HE Test in:', testinHE)
                        print('HE DAY:', dayHE)
                        print('BATCH HE:', batchPH)
                        print('HE Test in:', testinPH)
                        print('HE DAY:', dayPH)
                        update.message.reply_text(parse_mode='MarkdownV2',
                                                  text="Here is the result of your Incoming report\n\n" +
                                                       f'`Subcontractor Class: `*_ __{str(qr[1])}___*\n\n' +
                                                       f'`Type Class: `*_ __{str(tipeClass)}___*\n\n' +
                                                       f'`Part Number:` *__{str(res)}__*\n\n ' +
                                                       f"`Subcontractor Class {sclass}`\n\n " +
                                                       "`Phthalate`\n" +
                                                       f"`-Risk Level: {RLPH}`\n" +
                                                       f"`-Test Frequent: {testPH}`\n" +
                                                       "`-Report:`\n" +
                                                       f"```python Batch\#: {batchPH}```\n" +
                                                       f"```python Latest Report: {LRPH}```\n" +
                                                       f"```python Need Test at: {testinPH}```\n" +
                                                       f"```python In: {dayPH}```\n\n" +
                                                       "`Heavy Element`\n" +
                                                       f"`-Risk Level: {RLHE}`\n" +
                                                       f"`-Test Frequent: {testHE}`\n" +
                                                       "`-Report:`\n" +
                                                       f"```python Batch\#: {batchHE}```\n" +
                                                       f"```python Latest Report: {LRHE}```\n" +
                                                       f"```python Need Test at: {testinHE}```\n" +
                                                       f"```python In: {dayHE}```\n\n"

                                                  )
                    elif tipeClass == '2':
                        print("Type 2")
                        RLHE = materialrisk[0]
                        RLPH = materialrisk[1]
                        print("Risk Level HE", RLHE)
                        print("Risk Level PH", RLPH)

                        rawMat = SQLProcess.PNRawMat(pn)
                        print("PN: ", rawMat)
                        if rawMat is None:
                            context.bot.send_message(chat_id=update.effective_chat.id, parse_mode="Markdown",
                                                     text="We cannot found the *Raw Material* for this *Part Number* :(")
                            context.bot.send_message(chat_id=update.effective_chat.id,
                                                     text="Please send me another data... "
                                                          "but before you sent the text to me, please double check the data :)",
                                                     parse_mode="Markdown")
                            return
                        report = (SQLProcess.rawMatLER(rawMat, sc))
                        print("Report", report)
                        subconName = report[1].split(":")
                        PNRawMat = report[1].split(":")
                        if report[0] is None and len(report) == 2:
                            print("HEHEHEHHEHEHEHE")
                            if "Subcon" in report[1]:
                                context.bot.send_message(chat_id=update.effective_chat.id, parse_mode='Markdown',
                                                         text=f"Sorry, we cannot found Report for Subcontractor *{subconName[1]}*")
                                context.bot.send_message(chat_id=update.effective_chat.id, parse_mode='Markdown',
                                                         text=f"Please send me another *GRN* :)")
                            elif "PNRawMat" in report[1]:
                                context.bot.send_message(chat_id=update.effective_chat.id, parse_mode='Markdown',
                                                         text=f"Sorry, we cannot found Report for Part Num Raw Material *{PNRawMat[1]}*")
                                context.bot.send_message(chat_id=update.effective_chat.id, parse_mode='Markdown',
                                                         text=f"Please send me another *GRN* :)")
                            return
                        elif report[0] is None and len(report) == 3:
                            print("HHAHAHAHAHHAHA")
                            context.bot.send_message(chat_id=update.effective_chat.id, parse_mode='Markdown',
                                                     text=f"Sorry, we cannot found Report for Part Num Raw Material *{PNRawMat[1]}*"
                                                          f"and  Subcontractor *{subconName[1]}*")
                            context.bot.send_message(chat_id=update.effective_chat.id, parse_mode='Markdown',
                                                    text=f"Please send me another *GRN* :)")
                            return


                        HEReport = report[0]
                        HEDate = report[1]
                        PHReport = report[2]
                        PHDate = report[3]
                        now = datetime.now()

                        if freqHE.isnumeric() == True and HEDate != None:
                            freqHE = int(freqHE)
                            testinHE = (datetime.strptime(HEDate, '%Y-%m-%d') + timedelta(days=freqHE))
                            dayHE = str((testinHE - now).days) + " Days"
                            testinHE = testinHE.strftime("%Y-%m-%d")

                        else:
                            print("Gak Numeric :(")
                            testinHE = "-"
                            freqHE = "-"
                            dayHE = "-"

                        if freqPH.isnumeric() == True and PHDate != None:
                            freqPH = int(freqPH)
                            testinPH = (datetime.strptime(PHDate, '%Y-%m-%d') + timedelta(days=freqPH))
                            dayPH = str((testinPH - now).days) + " Days"
                            testinPH = testinPH.strftime("%Y-%m-%d")

                        else:
                            print("Gak Numeric :(")
                            testinPH = "-"
                            freqPH = "-"
                            dayPH = "-"

                        context.bot.send_message(parse_mode='MarkdownV2', chat_id=update.effective_chat.id,
                                                 text="Here is the result of your Incoming report\n\n" +
                                                      f'`Subcontractor Class: `*_ __{str(qr[1])}___*\n\n' +
                                                      f'`Type Class: `*_ __{str(tipeClass)}___*\n\n' +
                                                      f'`Part Number:` *__{str(res)}__*\n\n ' +
                                                      f"`Certified Class {sclass}`\n\n " +
                                                      "`Phthalate`\n" +
                                                      f"`-Risk Level: {RLPH}`\n" +
                                                      f"`-Test Frequent: {freqPH}`\n" +
                                                      "`-Report:`\n" +
                                                      f"```python Batch\#: {PHReport}```\n" +
                                                      f"```python Latest Report: {PHDate}```\n" +
                                                      f"```python Need Test at: {testinPH}```\n" +
                                                      f"```python In: {dayPH}```\n\n" +
                                                      "`Heavy Element`\n" +
                                                      f"`-Risk Level: {RLHE}`\n" +
                                                      f"`-Test Frequent: {freqHE}`\n" +
                                                      "`-Report:`\n" +
                                                      f"```python Batch\#: {HEReport}```\n" +
                                                      f"```python Latest Report: {HEDate}```\n" +
                                                      f"```python Need Test at: {testinHE}```\n" +
                                                      f"```python In: {dayHE}```\n\n"

                                                 )


                elif status.lower() == 'non certified':
                    sclass = 'NON'
                    subcom = SQLProcess.subcom(qr[2])
                    print(subcom)
                    if subcom is None:
                        update.message.reply_text(parse_mode='MarkdownV2',
                                                  text="*Sorry, We cannot find the report for this GRN\!*")
                    else:
                        materialrisk = SQLProcess.materialrisk(subcom[0], subcom[1])
                        risklevel = SQLProcess.risklevel(sclass, materialrisk[0], materialrisk[1])
                        RLHE = materialrisk[0]
                        RLPH = materialrisk[1]
                        testHE = risklevel[0]
                        testPH = risklevel[1]
                        print(materialrisk)
                        print(risklevel)

                        update.message.reply_text(parse_mode='MarkdownV2',
                                                  text="Here is the result of your Incoming report\n\n" +
                                                       f'`Supplier Class: `*_ __{str(qr[1])}___*\n\n' +
                                                       f'`Part Number:` *__{str(res)}__*\n\n ' +
                                                       f"`Non Certified Class`\n\n " +
                                                       "`Phthalate`\n" +
                                                       f"`-Risk Level: {RLPH}`\n" +
                                                       f"`-Test Frequent: {testPH}`\n\n" +
                                                       "`Heavy Element`\n" +
                                                       f"`-Risk Level: {RLHE}`\n" +
                                                       f"`-Test Frequent: {testHE}`\n"
                                                  )
        except telegram.error.TimedOut:
            context.bot.send_message(chat_id= update.effective_chat.id, text="_We are failed to get the_ *photo*, due to Timed Out error...")
            context.bot.send_message(chat_id= update.effective_chat.id, text="_Please re-send the photo!_")
        except Exception as e:
            print(str(e))
    elif menu[f"{update.effective_user.username}"] == "Quality Control":
        # print("QC System is Underdevelopment!")
        # context.bot.send_message(chat_id = update.effective_chat.id, text="Sorry, QC System is Underdevelopment")
        try:
            update.message.reply_text(parse_mode='MarkdownV2',
                                      text="_Please wait while we're finding the PPT of the Inspection\.\.\._")
            print(update)
            obj = context.bot.getFile(file_id=update.message.document.file_id)
            print(obj)
            filepath = obj['file_path']
            print(filepath)
            qr = decodeQR.process(menu[f"{update.effective_user.username}"], filepath)
            print("The QR is:", qr)
            if qr is None:
                update.message.reply_text(parse_mode='MarkdownV2',
                                          text="*Sorry, the Photo/LKP that you sent is not valid\.\.\.*")
                context.bot.send_message(parse_mode='Markdown', chat_id=update.effective_chat.id,
                                          text="_Please send me another Photo/LKP :)_")
            else:
                partNum[f'{update.effective_user.username}'] = qr[0]
                serialNum[f'{update.effective_user.username}'] = qr[1]
                print("Part Number :", partNum[f'{update.effective_user.username}'])
                molding = SQLProcess.qcmold(partNum[f'{update.effective_user.username}'])
                print(molding)
                if molding is None:
                    update.message.reply_text(parse_mode='Markdown', text="`This part has no Inspection!`")
                    update.message.reply_text(parse_mode='Markdown', text="`Please send me another LKP!`")
                    deeplearning[f"{update.effective_user.username}"] = ""
                    return
                elif molding[0] is not None and molding[1] == '':
                    buttons = [[KeyboardButton('PASS'), KeyboardButton('FAIL')], [KeyboardButton('BACK')]]
                    update.message.reply_text(parse_mode='Markdown',
                                              text="`This Part is ` *Critical* ` but does not have Inspection File`",
                                              reply_markup=ReplyKeyboardMarkup(buttons))
                elif molding[0] is not None and molding[1] is not None:
                    pathPPT[f'{update.effective_user.username}'] = molding[1]
                    fileName[f'{update.effective_user.username}'] = pathPPT[f'{update.effective_user.username}'][-10::]
                    update.message.reply_text(parse_mode='Markdown',
                                              text=f'_Yeay, We have found the File for Part Number_ *{partNum[f"{update.effective_user.username}"]}*')
                    update.message.reply_text(parse_mode='Markdown',
                                              text=f'The PPT file of this Part is refering to *{fileName[f"{update.effective_user.username}"]}*')
                    buttons = [[KeyboardButton('Yes')], [KeyboardButton('No')]]
                    context.bot.send_message(parse_mode='Markdown', chat_id=update.effective_chat.id,
                                             text='Do you want me to send the PPT file?',
                                             reply_markup=ReplyKeyboardMarkup(buttons))
        except telegram.error.TimedOut:
            context.bot.send_message(chat_id= update.effective_chat.id, text="_We are failed to get the_ *photo*, due to Timed Out error...")
            context.bot.send_message(chat_id= update.effective_chat.id, text="_Please re-send the photo!_")
        except Exception as e:
            print(str(e))

def GRN(update: Update, context: CallbackContext):

    qr = (update.message.text.split(' '))
    if len(qr) < 2:
        context.bot.send_message(chat_id=update.effective_chat.id, parse_mode='Markdown',
                                 text="Please type the *GRN* completely!")
        context.bot.send_message(chat_id=update.effective_chat.id, parse_mode='Markdown',
                                 text="Type the GRN in format /GRN *SupplierClass PartNumber*")
        return

    #---------------PASTE FROM BELOW YEAH--------------#

    print(qr[0])
    partnum = qr[2].find('-')
    res = qr[2][:partnum] + '\\' + qr[2][partnum:]
    suppclass = SQLProcess.suppclass(qr[1])
    pn = qr[2]
    sc = qr[1]
    status = suppclass[0]
    sclass = suppclass[1]
    print(status, "|", sclass)
    if status.lower() == 'certified':
        print('CERTIFIED')
        subcom = SQLProcess.subcom(qr[2])
        print(subcom)
        if subcom is None:
            update.message.reply_text(parse_mode='MarkdownV2',
                                      text="*Sorry, We cannot find the report for this GRN\!*")
        else:
            print(subcom)

            materialrisk = SQLProcess.materialrisk(subcom[0], subcom[1])
            risklevel = SQLProcess.risklevel(sclass, materialrisk[0], materialrisk[1])

            result = SQLProcess.report(qr[2], risklevel[0], risklevel[1])
            freqHE = str(risklevel[0])
            freqPH = str(risklevel[1])

            print(len(freqHE), len(freqPH))
            if len(freqHE) > 3 and len(freqPH) > 3:
                # Every Incoming
                print("#Every Incoming")
                RLHE = materialrisk[0]
                RLPH = materialrisk[1]

                # testHE = risklevel[0]
                # testPH = risklevel[1]
                testHE = freqHE
                testPH = freqPH

                batchHE = '-'
                testinHE = '-'
                dayHE = '-'

                batchPH = '-'
                testinPH = '-'
                dayPH = '-'

                LRPH = '-'
                LRHE = '-'

            elif len(freqHE) <= 3 and len(freqPH) <= 3:
                print("HE:", freqHE, "\nPH:", freqPH)
                result = SQLProcess.report(qr[2], risklevel[0], risklevel[1])
                RLHE = materialrisk[0]
                RLPH = materialrisk[1]
                print(RLHE, RLPH)

                testHE = str(risklevel[0]) + ' Days'
                testPH = str(risklevel[1]) + ' Days'
                if RLPH == 'N/A' and RLHE == 'N/A':
                    testHE = '-'
                    testPH = '-'
                elif RLHE == 'N/A':
                    testHE = '-'
                elif RLPH == 'N/A':
                    testPH = '-'
                else:
                    testHE = str(risklevel[0]) + ' Days'
                    testPH = str(risklevel[1]) + ' Days'

                batchHE = result[0]
                testinHE = result[1]
                dayHE = str(result[2]) + ' Days'

                batchPH = result[3]
                testinPH = result[4]
                dayPH = str(result[5]) + ' Days'

                LRPH = result[6]
                LRHE = result[7]
            elif len(freqHE) > 3 and len(freqPH) <= 3:
                # HE Periodical, PH Every Incoming
                testfreq = list(risklevel)
                print(testfreq)
                testfreq[0] = 0
                risklevel = tuple(testfreq)
                print(risklevel)

                print(risklevel[0])
                print("HE: Every Incoming", "\nPH: ", freqPH)
                result = SQLProcess.report(qr[2], risklevel[0], risklevel[1])
                RLHE = materialrisk[0]
                RLPH = materialrisk[1]

                testHE = freqHE
                testPH = str(risklevel[1]) + ' Days'
                batchHE = '-'
                testinHE = '-'
                dayHE = '-'

                batchPH = result[3]
                testinPH = result[4]
                dayPH = str(result[5]) + ' Days'

                LRPH = result[6]
                LRHE = '-'
            elif len(freqHE) <= 3 and len(freqPH) > 3:
                # HE Every Incoming, PH Periodical
                testfreq = list(risklevel)
                print(testfreq)
                testfreq[1] = 0
                risklevel = tuple(testfreq)
                print(risklevel)
                print("HE:", freqHE, "PH Every Incoming")
                result = SQLProcess.report(qr[2], risklevel[0], risklevel[1])
                RLHE = materialrisk[0]
                RLPH = materialrisk[1]

                testHE = str(risklevel[0]) + ' Days'
                testPH = freqPH
                batchHE = result[0]
                testinHE = result[1]
                dayHE = str(result[2]) + ' Days'

                batchPH = '-'
                testinPH = '-'
                dayPH = '-'

                LRPH = '-'
                LRHE = result[7]

            print('BATCH HE:', batchHE)
            print('HE Test in:', testinHE)
            print('HE DAY:', dayHE)
            print('BATCH HE:', batchPH)
            print('HE Test in:', testinPH)
            print('HE DAY:', dayPH)
            update.message.reply_text(parse_mode='MarkdownV2',
                                      text="Here is the result of your Incoming report\n\n" +
                                           f'`Supplier Class: `*_ __{str(qr[1])}___*\n\n' +
                                           f'`Part Number:` *__{str(res)}__*\n\n ' +
                                           f"`Certified Class {sclass}`\n\n " +
                                           "`Phthalate`\n" +
                                           f"`-Risk Level: {RLPH}`\n" +
                                           f"`-Test Frequent: {testPH}`\n" +
                                           "`-Report:`\n" +
                                           f"```python Batch\#: {batchPH}```\n" +
                                           f"```python Latest Report: {LRPH}```\n" +
                                           f"```python Need Test at: {testinPH}```\n" +
                                           f"```python In: {dayPH}```\n\n" +
                                           "`Heavy Element`\n" +
                                           f"`-Risk Level: {RLHE}`\n" +
                                           f"`-Test Frequent: {testHE}`\n" +
                                           "`-Report:`\n" +
                                           f"```python Batch\#: {batchHE}```\n" +
                                           f"```python Latest Report: {LRHE}```\n" +
                                           f"```python Need Test at: {testinHE}```\n" +
                                           f"```python In: {dayHE}```\n\n"

                                      )

    elif 'subcon' in status.lower():
        print('SUBCON')
        # update.message.reply_text(parse_mode='MarkdownV2',
        #                           text="*Subcontractor is underdevelopment\!*")
        subcom = SQLProcess.subcom(qr[2])
        print("SUBCOM: ", subcom)
        if subcom is None:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="Sorry, we cannot found the *Commodity* and "
                                          "*Subcommodity* based on the data that you sent to us!",
                                     parse_mode="Markdown")
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="Please send me another data... "
                                          "but before you sent the text to me, please double check the data :)",
                                     parse_mode="Markdown")
            return
        materialrisk = SQLProcess.materialrisk(subcom[0], subcom[1])
        print("Material Risk : ", materialrisk)
        tipeClass = SQLProcess.typeClass(subcom[0], subcom[1])
        print(tipeClass)
        risklevelSubcon = SQLProcess.risklevelSubcon(sclass, materialrisk[0], materialrisk[1])
        print(risklevelSubcon)
        result = SQLProcess.report(qr[2], risklevelSubcon[0], risklevelSubcon[1])
        freqHE = str(risklevelSubcon[0])
        freqPH = str(risklevelSubcon[1])
        print(len(freqHE), len(freqPH))
        print("RLHE:", freqHE, "; RLPH:", freqPH)
        # tipeClass = "1"
        if tipeClass == "1":

            if len(freqHE) > 3 and len(freqPH) > 3:
                # Every Incoming
                print("#Every Incoming")
                RLHE = materialrisk[0]
                RLPH = materialrisk[1]

                # testHE = risklevel[0]
                # testPH = risklevel[1]
                testHE = freqHE
                testPH = freqPH

                batchHE = '-'
                testinHE = '-'
                dayHE = '-'

                batchPH = '-'
                testinPH = '-'
                dayPH = '-'

                LRPH = '-'
                LRHE = '-'

            elif len(freqHE) <= 3 and len(freqPH) <= 3:
                print("HE:", freqHE, "\nPH:", freqPH)
                result = SQLProcess.report(qr[2], risklevelSubcon[0], risklevelSubcon[1])
                RLHE = materialrisk[0]
                RLPH = materialrisk[1]
                print(RLHE, RLPH)

                testHE = str(risklevelSubcon[0]) + ' Days'
                testPH = str(risklevelSubcon[1]) + ' Days'
                if RLPH == 'N/A' and RLHE == 'N/A':
                    testHE = '-'
                    testPH = '-'
                elif RLHE == 'N/A':
                    testHE = '-'
                elif RLPH == 'N/A':
                    testPH = '-'
                else:
                    testHE = str(risklevelSubcon[0]) + ' Days'
                    testPH = str(risklevelSubcon[1]) + ' Days'

                batchHE = result[0]
                testinHE = result[1]
                dayHE = str(result[2]) + ' Days'

                batchPH = result[3]
                testinPH = result[4]
                dayPH = str(result[5]) + ' Days'

                LRPH = result[6]
                LRHE = result[7]
            elif len(freqHE) > 3 and len(freqPH) <= 3:
                # HE Periodical, PH Every Incoming
                testfreq = list(risklevelSubcon)
                print(testfreq)
                testfreq[0] = 0
                risklevel = tuple(testfreq)
                print(risklevel)

                print(risklevel[0])
                print("HE: Every Incoming", "\nPH: ", freqPH)
                result = SQLProcess.report(qr[2], risklevel[0], risklevel[1])
                RLHE = materialrisk[0]
                RLPH = materialrisk[1]

                testHE = freqHE
                testPH = str(risklevel[1]) + ' Days'
                batchHE = '-'
                testinHE = '-'
                dayHE = '-'

                batchPH = result[3]
                testinPH = result[4]
                dayPH = str(result[5]) + ' Days'

                LRPH = result[6]
                LRHE = '-'
            elif len(freqHE) <= 3 and len(freqPH) > 3:
                # HE Every Incoming, PH Periodical
                testfreq = list(risklevelSubcon)
                print(testfreq)
                testfreq[1] = 0
                risklevel = tuple(testfreq)
                print(risklevel)
                print("HE:", freqHE, "PH Every Incoming")
                result = SQLProcess.report(qr[2], risklevel[0], risklevel[1])
                RLHE = materialrisk[0]
                RLPH = materialrisk[1]

                testHE = str(risklevel[0]) + ' Days'
                testPH = freqPH
                batchHE = result[0]
                testinHE = result[1]
                dayHE = str(result[2]) + ' Days'

                batchPH = '-'
                testinPH = '-'
                dayPH = '-'

                LRPH = '-'
                LRHE = result[7]

            print('BATCH HE:', batchHE)
            print('HE Test in:', testinHE)
            print('HE DAY:', dayHE)
            print('BATCH HE:', batchPH)
            print('HE Test in:', testinPH)
            print('HE DAY:', dayPH)
            update.message.reply_text(parse_mode='MarkdownV2',
                                      text="Here is the result of your Incoming report\n\n" +
                                           f'`Subcontractor Class: `*_ __{str(qr[1])}___*\n\n' +
                                           f'`Type Class: `*_ __{str(tipeClass)}___*\n\n' +
                                           f'`Part Number:` *__{str(res)}__*\n\n ' +
                                           f"`Subcontractor Class {sclass}`\n\n " +
                                           "`Phthalate`\n" +
                                           f"`-Risk Level: {RLPH}`\n" +
                                           f"`-Test Frequent: {testPH}`\n" +
                                           "`-Report:`\n" +
                                           f"```python Batch\#: {batchPH}```\n" +
                                           f"```python Latest Report: {LRPH}```\n" +
                                           f"```python Need Test at: {testinPH}```\n" +
                                           f"```python In: {dayPH}```\n\n" +
                                           "`Heavy Element`\n" +
                                           f"`-Risk Level: {RLHE}`\n" +
                                           f"`-Test Frequent: {testHE}`\n" +
                                           "`-Report:`\n" +
                                           f"```python Batch\#: {batchHE}```\n" +
                                           f"```python Latest Report: {LRHE}```\n" +
                                           f"```python Need Test at: {testinHE}```\n" +
                                           f"```python In: {dayHE}```\n\n"

                                      )
        elif tipeClass == '2':
            print("Type 2")
            RLHE = materialrisk[0]
            RLPH = materialrisk[1]
            print("Risk Level HE", RLHE)
            print("Risk Level PH", RLPH)

            rawMat = SQLProcess.PNRawMat(pn)
            print("PN: ", rawMat)
            if rawMat is None:
                context.bot.send_message(chat_id=update.effective_chat.id, parse_mode="Markdown",
                                         text="We cannot found the *Raw Material* for this *Part Number* :(")
                context.bot.send_message(chat_id=update.effective_chat.id,
                                         text="Please send me another data... "
                                              "but before you sent the text to me, please double check the data :)",
                                         parse_mode="Markdown")
                return
            report = (SQLProcess.rawMatLER(rawMat, sc))
            print("Report", report)
            subconName = report[1].split(":")
            PNRawMat = report[1].split(":")
            if report[0] is None and len(report) == 2:
                print("HEHEHEHHEHEHEHE")
                if "Subcon" in report[1]:
                    context.bot.send_message(chat_id=update.effective_chat.id, parse_mode='Markdown',
                                             text=f"Sorry, we cannot found Report for Subcontractor *{subconName[1]}*")
                    context.bot.send_message(chat_id=update.effective_chat.id, parse_mode='Markdown',
                                             text=f"Please send me another *GRN* :)")
                elif "PNRawMat" in report[1]:
                    context.bot.send_message(chat_id=update.effective_chat.id, parse_mode='Markdown',
                                             text=f"Sorry, we cannot found Report for Part Num Raw Material *{PNRawMat[1]}*")
                    context.bot.send_message(chat_id=update.effective_chat.id, parse_mode='Markdown',
                                             text=f"Please send me another *GRN* :)")
                return
            elif report[0] is None and len(report) == 3:
                print("HHAHAHAHAHHAHA")
                context.bot.send_message(chat_id=update.effective_chat.id, parse_mode='Markdown',
                                         text=f"Sorry, we cannot found Report for Part Num Raw Material *{PNRawMat[1]}*"
                                              f"and  Subcontractor *{subconName[1]}*")
                context.bot.send_message(chat_id=update.effective_chat.id, parse_mode='Markdown',
                                         text=f"Please send me another *GRN* :)")
                return

            HEReport = report[0]
            HEDate = report[1]
            PHReport = report[2]
            PHDate = report[3]
            now = datetime.now()

            if freqHE.isnumeric() == True and HEDate != None:
                freqHE = int(freqHE)
                testinHE = (datetime.strptime(HEDate, '%Y-%m-%d') + timedelta(days=freqHE))
                dayHE = str((testinHE - now).days) + " Days"
                testinHE = testinHE.strftime("%Y-%m-%d")

            else:
                print("Gak Numeric :(")
                testinHE = "-"
                freqHE = "-"
                dayHE = "-"

            if freqPH.isnumeric() == True and PHDate != None:
                freqPH = int(freqPH)
                testinPH = (datetime.strptime(PHDate, '%Y-%m-%d') + timedelta(days=freqPH))
                dayPH = str((testinPH - now).days) + " Days"
                testinPH = testinPH.strftime("%Y-%m-%d")

            else:
                print("Gak Numeric :(")
                testinPH = "-"
                freqPH = "-"
                dayPH = "-"

            context.bot.send_message(parse_mode='MarkdownV2', chat_id=update.effective_chat.id,
                                     text="Here is the result of your Incoming report\n\n" +
                                          f'`Subcontractor Class: `*_ __{str(qr[1])}___*\n\n' +
                                          f'`Type Class: `*_ __{str(tipeClass)}___*\n\n' +
                                          f'`Part Number:` *__{str(res)}__*\n\n ' +
                                          f"`Certified Class {sclass}`\n\n " +
                                          "`Phthalate`\n" +
                                          f"`-Risk Level: {RLPH}`\n" +
                                          f"`-Test Frequent: {freqPH}`\n" +
                                          "`-Report:`\n" +
                                          f"```python Batch\#: {PHReport}```\n" +
                                          f"```python Latest Report: {PHDate}```\n" +
                                          f"```python Need Test at: {testinPH}```\n" +
                                          f"```python In: {dayPH}```\n\n" +
                                          "`Heavy Element`\n" +
                                          f"`-Risk Level: {RLHE}`\n" +
                                          f"`-Test Frequent: {freqHE}`\n" +
                                          "`-Report:`\n" +
                                          f"```python Batch\#: {HEReport}```\n" +
                                          f"```python Latest Report: {HEDate}```\n" +
                                          f"```python Need Test at: {testinHE}```\n" +
                                          f"```python In: {dayHE}```\n\n"

                                     )


    elif status.lower() == 'non certified':
        sclass = 'NON'
        subcom = SQLProcess.subcom(qr[2])
        print(subcom)
        if subcom is None:
            update.message.reply_text(parse_mode='MarkdownV2',
                                      text="*Sorry, We cannot find the report for this GRN\!*")
        else:
            materialrisk = SQLProcess.materialrisk(subcom[0], subcom[1])
            risklevel = SQLProcess.risklevel(sclass, materialrisk[0], materialrisk[1])
            RLHE = materialrisk[0]
            RLPH = materialrisk[1]
            testHE = risklevel[0]
            testPH = risklevel[1]
            print(materialrisk)
            print(risklevel)

            update.message.reply_text(parse_mode='MarkdownV2',
                                      text="Here is the result of your Incoming report\n\n" +
                                           f'`Supplier Class: `*_ __{str(qr[1])}___*\n\n' +
                                           f'`Part Number:` *__{str(res)}__*\n\n ' +
                                           f"`Non Certified Class`\n\n " +
                                           "`Phthalate`\n" +
                                           f"`-Risk Level: {RLPH}`\n" +
                                           f"`-Test Frequent: {testPH}`\n\n" +
                                           "`Heavy Element`\n" +
                                           f"`-Risk Level: {RLHE}`\n" +
                                           f"`-Test Frequent: {testHE}`\n"
                                      )

# print(GRN(update= Update, context= CallbackContext, SupplierClass="4715" ,PartNum="GKH23-2109"))

def Exit(update: Update, context: CallbackContext):
    Status[f"{update.effective_user.username}"] = ''
    buttons = [[KeyboardButton('Incoming Quality Control')], [KeyboardButton('Quality Control')]]
    context.bot.send_message(parse_mode='Markdown', chat_id=update.effective_chat.id,
                             text="Please choose which _system_ do you want to execute",
                             reply_markup=ReplyKeyboardMarkup(buttons))
    # print(PASS)

def input(update: Update, context: CallbackContext):
    buttons = [[KeyboardButton('PASS')], [KeyboardButton('FAIL')]]

    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Data entry for QC Molding System. Please select either the part PASS or FAIL!",
                             reply_markup=ReplyKeyboardMarkup(buttons))
    context.bot.send_document(chat_id=update.effective_chat.id, document=open(r"\\Apckranefa01pv\apckr001\CKR\APCKRMFLPT001P\G_Drive\Groups\QA\SQT by QE\MODULES\TeleBot\2021-11-02\ScheduleToday.xlsx", "rb"), filename='ScheduleToday.xlsx')

def messageHandler(update: Update, context: CallbackContext):
    # PASS.clear()
    if update.effective_chat.username not in allowedUsernames:
        context.bot.send_message(chat_id=update.effective_chat.id, text="You are not allowed to use this bot")
        return
    else:
        Name[f"{update.effective_user.username}"] = update.effective_user.first_name
        print(LineLead)

        if 'Yes, show me' == update.message.text:
            print("Test Menu:", menu)
            if not menu:
                context.bot.send_message(reply_markup=telegram.ReplyKeyboardRemove(), chat_id=update.effective_chat.id,
                                         parse_mode='Markdown',
                                         text=f"_Hi, you are not selecting any menu..._ type /start to begin :)")
            elif menu[f"{update.effective_user.username}"] == "Quality Control":
                context.bot.send_message(chat_id=update.effective_chat.id, parse_mode='Markdown', text = "`Please wait, we are preparing the Schedule File for you :)`")
                xl = runMacro.saveone(pathSchedule)
                print(xl)
                xl = Path(xl)
                print(xl)
                if xl is None:
                    context.bot.send_message(reply_markup=telegram.ReplyKeyboardRemove(), parse_mode='Markdown',
                                           chat_id=update.effective_chat.id,
                                             text="`Sorry, we cannot generate the production schedule :(`")
                else:
                    try:
                        context.bot.send_message(reply_markup=telegram.ReplyKeyboardRemove(), parse_mode='Markdown',
                                                 chat_id=update.effective_chat.id,
                                                 text="This is the Excel file of the Production Schedule for today")
                        context.bot.send_document(chat_id=update.effective_chat.id, document=open(
                            rf"{xl}",
                            "rb"), filename='ScheduleToday.xlsx')

                    except OSError:
                        context.bot.send_message(reply_markup=telegram.ReplyKeyboardRemove(), parse_mode = 'Markdown',
                                                 chat_id = update.effective_chat.id,
                                                 text = "`Sorry, we cannot found the file with the specify link :(`")

                    except telegram.error.NetworkError:
                        context.bot.send_message(reply_markup=telegram.ReplyKeyboardRemove(), parse_mode='Markdown',
                                                 chat_id=update.effective_chat.id,
                                                 text="`We are having some trouble to getting the Schedule File, due too large size of the file :(`")
                    context.bot.send_message(reply_markup=telegram.ReplyKeyboardRemove(), chat_id=update.effective_chat.id, parse_mode='Markdown',
                                     text=f"To find the PPT File of Inspection file please send me the photo of *LKP* :)")
            elif menu[f"{update.effective_user.username}"] == "Incoming Quality Control":
                context.bot.send_message(reply_markup=telegram.ReplyKeyboardRemove(), chat_id=update.effective_chat.id,
                                         parse_mode='Markdown', text=f"_Sorry, you are in the wrong menu! type_ /exit, _we will direct you to the Main Menu..._")

        elif 'No, thanks' == update.message.text:
            context.bot.send_message(reply_markup=telegram.ReplyKeyboardRemove(), chat_id=update.effective_chat.id, parse_mode='Markdown',
                                     text=f"To find the PPT File of Inspection file please send me the photo of *LKP* :)")

        if pathPPT[f'{update.effective_user.username}'] != '' and 'Yes' == update.message.text:
            print("Bakal keluarin PPT nya")
            buttons = [[KeyboardButton('PASS'), KeyboardButton('FAIL')], [KeyboardButton('BACK')]]
            # pathPPT[f'{update.effective_user.username}'] = '\\Apckranefa01pv\apckr001\CKR\APCKRMFLPT001P\G_Drive\Groups\QA\SQT by QE\SQT PPT File\GFF156.pptx'
            context.bot.send_message(parse_mode='Markdown', chat_id=update.effective_chat.id, reply_markup=ReplyKeyboardRemove()
                                     ,text='_We are preparing the PPT file for you. Once it ready, we will directly send the PPT File :)_')


            if fileName[f'{update.effective_user.username}'] == 'Collector':
                pathPPT[f'{update.effective_user.username}'] = r"C:\Users\User\Documents\President University\Thesis\SQT\Barbie Collector.pptx"
                fileName[f'{update.effective_user.username}'] = 'Collector.pptx'
                print(fileName[f'{update.effective_user.username}'])
                print("Pathnya: ", pathPPT[f'{update.effective_user.username}'])
            try:
                context.bot.send_document(chat_id=update.effective_chat.id, document=open(
                    f"{pathPPT[f'{update.effective_user.username}']}",
                    "rb"), filename=fileName[f'{update.effective_user.username}'])
                context.bot.send_message(parse_mode='Markdown', chat_id=update.effective_chat.id,
                                         text='_Please send me a photo of the part_')


            except OSError:
                context.bot.send_message(parse_mode = 'Markdown',
                                         chat_id = update.effective_chat.id,
                                         text = "`Sorry, we cannot found the file with the specify link :(`",
                                         reply_markup = ReplyKeyboardRemove())
                context.bot.send_message(parse_mode='Markdown',
                                         chat_id=update.effective_chat.id,
                                         text="`Please send me photo of the part`")
            except telegram.error.NetworkError:
                context.bot.send_message(parse_mode='Markdown',
                                         chat_id=update.effective_chat.id,
                                         text="`We are very sorry because we cannot getting the PPT File. Due too large size of the file :(`")
                context.bot.send_message(parse_mode='Markdown', chat_id=update.effective_chat.id,
                                         text='_Please send me a photo of the part_')
        elif pathPPT[f'{update.effective_user.username}'] != '' and 'No' == update.message.text:
            buttons = [[KeyboardButton('PASS'), KeyboardButton('FAIL')], [KeyboardButton('BACK')]]
            context.bot.send_message(parse_mode='Markdown', chat_id=update.effective_chat.id,
                                     text='_Please send me a photo of the part_', reply_markup=telegram.ReplyKeyboardRemove())

        if not ("Quality Control" in update.message.text or "FAIL" in update.message.text or "PASS" in update.message.text
            or "Exit" in update.message.text or "BACK" in update.message.text) \
            and (MachineNum[f"{update.effective_user.username}"] == ''
            or MachineNum[f"{update.effective_user.username}"] is None) and \
            LineLead[f"{update.effective_user.username}"] != '':
                if (not menu or menu[f"{update.effective_user.username}"] != "Quality Control"):
                    if not menu:
                        context.bot.send_message(chat_id=update.effective_chat.id,
                                                 reply_markup=telegram.ReplyKeyboardRemove(),
                                                 parse_mode='Markdown',
                                                 text=f'_Hi_ *{update.effective_user.first_name}*, _I think you are not selected any menu..._')
                        context.bot.send_message(chat_id=update.effective_chat.id,
                                                 parse_mode='Markdown', text="_To open the menu, you can type_ /start")
                    elif menu[f"{update.effective_user.username}"] != "Quality Control":
                        context.bot.send_message(chat_id=update.effective_chat.id,
                                                 reply_markup=telegram.ReplyKeyboardRemove(),
                                                 parse_mode='Markdown',
                                                 text=f'_Hi_ *{update.effective_user.first_name}*, _I think you are in the wrong menu..._')
                        context.bot.send_message(chat_id=update.effective_chat.id,
                                                 parse_mode='Markdown', text="_To open the menu, you can type_ /start")
                elif (not Name or Name[f"{update.effective_user.username}"] == '') or \
                        (not LBOPATROL or LBOPATROL[f"{update.effective_user.username}"] == '') or \
                        (not LotNum or LotNum[f"{update.effective_user.username}"] == '') or \
                        (not SampleSize or SampleSize[f"{update.effective_user.username}"] == '') or \
                        (not LotSize or LotSize[f"{update.effective_user.username}"] == '') or \
                        (not LineLead or LineLead[f"{update.effective_user.username}"] == ''):
                    context.bot.send_message(parse_mode='Markdown', reply_markup=telegram.ReplyKeyboardRemove(),
                                             chat_id=update.effective_chat.id,
                                             text="Please make sure that you have fulfill all the *required data*!")
                else:
                    print("Storing the Machine Number")
                    MachineNum[f"{update.effective_user.username}"] = update.message.text
                    print(MachineNum)
                    context.bot.send_message(chat_id=update.effective_chat.id,
                                             text=f"Machine# : {MachineNum[f'{update.effective_user.username}']}")
                    if Status[f"{update.effective_user.username}"] == 'PASS':
                        sn = serialNum[f'{update.effective_user.username}']
                        st = Status[f"{update.effective_user.username}"]
                        fn = Name[f"{update.effective_user.username}"]
                        lp = LBOPATROL[f"{update.effective_user.username}"]
                        ln = LotNum[f"{update.effective_user.username}"]
                        ss = SampleSize[f"{update.effective_user.username}"]
                        ls = LotSize[f"{update.effective_user.username}"]
                        mn = MachineNum[f"{update.effective_user.username}"]
                        ll = LineLead[f"{update.effective_user.username}"]
                        kpk = ""
                        mj = ""
                        dc = ""
                        ra = ""
                        rm = ""
                        print(sn, st, fn, lp, ln, ss, ls, mn, ll, kpk, mj, dc, ra, rm)
                        result = SaveToMacro.save(sn, st, fn, lp, ln, ss, ls, mn, ll, kpk, mj, dc, ra, rm)
                        serialNum[f'{update.effective_user.username}'] = ''
                        Status[f"{update.effective_user.username}"] = ''
                        Name[f"{update.effective_user.username}"] = ''
                        LBOPATROL[f"{update.effective_user.username}"] = ''
                        LotNum[f"{update.effective_user.username}"] = ''
                        SampleSize[f"{update.effective_user.username}"] = ''
                        LotSize[f"{update.effective_user.username}"] = ''
                        MachineNum[f"{update.effective_user.username}"] = ''
                        LineLead[f"{update.effective_user.username}"] = ''
                        context.bot.send_message(parse_mode='Markdown', reply_markup=telegram.ReplyKeyboardRemove(),
                                                 chat_id=update.effective_chat.id, text=f"`{result}`")
                        context.bot.send_message(parse_mode='Markdown', chat_id=update.effective_chat.id,
                                                 text="`To Key-In another data, please send me another LKP photo :)`")
                    elif Status[f"{update.effective_user.username}"] == 'FAIL':
                        context.bot.send_message(parse_mode='Markdown', chat_id=update.effective_chat.id,
                                                 text="Please type the *Major*")
        elif not ("Quality Control" in update.message.text or "FAIL" in update.message.text or "PASS" in update.message.text
            or "Exit" in update.message.text or "BACK" in update.message.text) \
            and (Major[f"{update.effective_user.username}"] == ''
            or Major[f"{update.effective_user.username}"] is None) and \
            MachineNum[f"{update.effective_user.username}"] != '':

            Major[f"{update.effective_user.username}"] = update.message.text
            print("Major : ", Major)
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text=f"Major : {Major[f'{update.effective_user.username}']}")
            context.bot.send_message(parse_mode='Markdown', chat_id=update.effective_chat.id,
                                     text="Please type the *Defect Code*")

        elif not ("Quality Control" in update.message.text or "FAIL" in update.message.text or "PASS" in update.message.text
            or "Exit" in update.message.text or "BACK" in update.message.text) \
            and (DC[f"{update.effective_user.username}"] == ''
            or DC[f"{update.effective_user.username}"] is None) and \
            Major[f"{update.effective_user.username}"] != '':
            DC[f"{update.effective_user.username}"] = update.message.text
            print("Defect Code :", DC)
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text=f"Defect Code : {DC[f'{update.effective_user.username}']}")
            context.bot.send_message(parse_mode='Markdown', chat_id=update.effective_chat.id,
                                     text="Please type the *Reaudit*")

        elif not ("Quality Control" in update.message.text or "FAIL" in update.message.text or "PASS" in update.message.text
            or "Exit" in update.message.text or "BACK" in update.message.text) \
            and (RA[f"{update.effective_user.username}"] == ''
            or RA[f"{update.effective_user.username}"] is None) and \
            DC[f"{update.effective_user.username}"] != '':
            RA[f"{update.effective_user.username}"] = update.message.text
            print("Reaudit :", RA)
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text=f"Reaudit : {RA[f'{update.effective_user.username}']}")
            context.bot.send_message(parse_mode='Markdown', chat_id=update.effective_chat.id,
                                     text="Please type the *KPK Operator*")

        elif not ("Quality Control" in update.message.text or "FAIL" in update.message.text or "PASS" in update.message.text
            or "Exit" in update.message.text or "BACK" in update.message.text) \
            and (KPK[f"{update.effective_user.username}"] == ''
            or KPK[f"{update.effective_user.username}"] is None) and \
            RA[f"{update.effective_user.username}"] != '':

            if update.message.text.isnumeric() == True:

                KPK[f"{update.effective_user.username}"] = update.message.text
                print("KPK :", KPK)
                context.bot.send_message(chat_id=update.effective_chat.id,
                                         text=f"KPK Operator: {KPK[f'{update.effective_user.username}']}")
                context.bot.send_message(parse_mode='Markdown', chat_id=update.effective_chat.id,
                                         text="Please type the *Remarks*")
            else:
                print("Not numeric")
                context.bot.send_message(parse_mode='Markdown', chat_id=update.effective_chat.id,
                                         text="Seems like you type the non-numeric of KPK Operator")
                context.bot.send_message(parse_mode='Markdown', chat_id=update.effective_chat.id,
                                         text="Please type the *KPK Operator* in Numeric")

        elif not ("Quality Control" in update.message.text or "FAIL" in update.message.text or "PASS" in update.message.text
            or "Exit" in update.message.text or "BACK" in update.message.text) \
            and (RM[f"{update.effective_user.username}"] == ''
            or RM[f"{update.effective_user.username}"] is None) and \
            KPK[f"{update.effective_user.username}"] != '':

            RM[f"{update.effective_user.username}"] = update.message.text
            print("Remarks :",  RM)
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text=f"Remarks: {RM[f'{update.effective_user.username}']}")
            # SAVE TO MACRO
            sn = serialNum[f'{update.effective_user.username}']
            st = Status[f"{update.effective_user.username}"]
            fn = Name[f"{update.effective_user.username}"]
            lp = LBOPATROL[f"{update.effective_user.username}"]
            ln = LotNum[f"{update.effective_user.username}"]
            ss = SampleSize[f"{update.effective_user.username}"]
            ls = LotSize[f"{update.effective_user.username}"]
            mn = MachineNum[f"{update.effective_user.username}"]
            ll = LineLead[f"{update.effective_user.username}"]
            kpk = KPK[f"{update.effective_user.username}"]
            mj = Major[f"{update.effective_user.username}"]
            dc = DC[f"{update.effective_user.username}"]
            ra = RA[f"{update.effective_user.username}"]
            rm = RM[f"{update.effective_user.username}"]
            print(sn, st, fn, lp, ln, ss, ls, mn, ll, kpk, mj, dc, ra, rm)
            result = SaveToMacro.save(sn, st, fn, lp, ln, ss, ls, mn, ll, kpk, mj, dc, ra, rm)
            serialNum[f'{update.effective_user.username}'] = ''
            Status[f"{update.effective_user.username}"] = ''
            Name[f"{update.effective_user.username}"] = ''
            LBOPATROL[f"{update.effective_user.username}"] = ''
            LotNum[f"{update.effective_user.username}"] = ''
            SampleSize[f"{update.effective_user.username}"] = ''
            LotSize[f"{update.effective_user.username}"] = ''
            MachineNum[f"{update.effective_user.username}"] = ''
            LineLead[f"{update.effective_user.username}"] = ''
            Major[f"{update.effective_user.username}"] = ''
            DC[f"{update.effective_user.username}"] = ''
            KPK[f"{update.effective_user.username}"] = ''
            RA[f"{update.effective_user.username}"] = ''
            RM[f"{update.effective_user.username}"] = ''
            context.bot.send_message(parse_mode='Markdown', reply_markup=telegram.ReplyKeyboardRemove(),
                                     chat_id=update.effective_chat.id, text=f"`{result}`")
            context.bot.send_message(parse_mode='Markdown', chat_id=update.effective_chat.id,
                                     text="`To Key-In another data, please send me another LKP photo :)`")



        if 'BACK' == update.message.text:
            buttons = [[KeyboardButton('Incoming Quality Control')], [KeyboardButton('Quality Control')]]
            context.bot.send_message(parse_mode='Markdown', chat_id=update.effective_chat.id,
                                     text="Please choose which _system_ do you want to execute",
                                     reply_markup=ReplyKeyboardMarkup(buttons))
            menu[f"{update.effective_user.username}"] = ""
        elif 'Exit' == update.message.text:
            buttons = [[KeyboardButton('Incoming Quality Control')], [KeyboardButton('Quality Control')]]
            context.bot.send_message(parse_mode='Markdown', chat_id=update.effective_chat.id,
                                     text="Please choose which _system_ do you want to execute",
                                     reply_markup=ReplyKeyboardMarkup(buttons))

        if "Quality Control" == update.message.text:
            buttons = [[KeyboardButton('Yes, show me')], [KeyboardButton('No, thanks')]]
            context.bot.send_message(chat_id=update.effective_chat.id, parse_mode='Markdown',
                                     #text=f"Hello {update.effective_user.first_name}, To find the PPT File of Inspection file please send me the photo of *LKP* :)",
                                     text=f"Hello {update.effective_user.first_name}, Do you want me to send *production* schedule for today? ",
                                     reply_markup=ReplyKeyboardMarkup(buttons))
            menu[f"{update.effective_user.username}"] = "Quality Control"
            print(menu)
        if "Incoming Quality Control" == update.message.text:
            buttons = [[KeyboardButton('Help')], [KeyboardButton('Exit')]]
            context.bot.send_message(reply_markup = ReplyKeyboardMarkup(buttons), chat_id=update.effective_chat.id, parse_mode='Markdown',
                                     text=f"Hello {update.effective_user.first_name}, Welcome to *Incoming Quality Control Menu System*!")
            context.bot.send_message(parse_mode='Markdown', chat_id=update.effective_chat.id,
                                     text="To find the latest report of the Incoming, please send me Picture or File of the *GRN*")
            context.bot.send_message(parse_mode='Markdown', chat_id=update.effective_chat.id,
                                     text=f"Or you can type manualy "
                                          "the GRN in format \n /GRN *SupplierClass* *PartNumber*")
            menu[f"{update.effective_user.username}"] = "Incoming Quality Control"
        print ("MENU:", menu)
        # if 'PASS' in update.message.text:
        #     Status[f"{update.effective_user.username}"] = "PASS"
        #     context.bot.send_message(parse_mode='Markdown', chat_id=update.effective_chat.id,
        #                              text="Please select the Button from the Top!",
        #                              reply_markup=telegram.ReplyKeyboardRemove())
        # elif 'FAIL' in update.message.text:
        #     Status[f"{update.effective_user.username}"] = "FAIL"
        #     context.bot.send_message(parse_mode='Markdown', chat_id=update.effective_chat.id,
        #                              text="Please select the Button from the Top!",
        #                              reply_markup=telegram.ReplyKeyboardRemove())
        print("STATUS:", Status)
        if 'PASS' in update.message.text and Status[f"{update.effective_user.username}"] == 'PASS':
            print(Status[f"{update.effective_user.username}"])
        elif 'FAIL' in update.message.text and Status[f"{update.effective_user.username}"] == 'FAIL':
            print(Status[f"{update.effective_user.username}"])

            # context.bot.send_message(chat_id=update.effective _chat.id)
            # buttons = [[InlineKeyboardButton("LBO", callback_data="LBO")],
            #            [InlineKeyboardButton("Patrol", callback_data="Patrol")]]
            # context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons),
            #                          text="Please choose either it's LBO or PATROL")
            # buttons = [[InlineKeyboardButton("1", callback_data="1"), InlineKeyboardButton("2", callback_data="2")],
            #            [InlineKeyboardButton("3", callback_data="3"), InlineKeyboardButton("4", callback_data="4")]]
            # context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons),
            #                          text="Please choose the LOT#")
            # buttons = [[InlineKeyboardButton("13", callback_data="13"), InlineKeyboardButton("20", callback_data="20")],
            #            [InlineKeyboardButton("32", callback_data="32")],
            #            [InlineKeyboardButton("50", callback_data="50"), InlineKeyboardButton("80", callback_data="80")]]
            # context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons),
            #                          text="Please choose the sample size")
            # buttons = [[InlineKeyboardButton("51-90", callback_data="51-90"),
            #             InlineKeyboardButton("91-150", callback_data="91-150")],
            #            [InlineKeyboardButton("151-280", callback_data="151-280"),
            #             InlineKeyboardButton("280-500", callback_data="280-500")],
            #            [InlineKeyboardButton("281-500", callback_data="281-500"),
            #             InlineKeyboardButton("501-1200", callback_data="501-1200")],
            #            [InlineKeyboardButton("601-1200", callback_data="601-1200"),
            #             InlineKeyboardButton("1201-3200", callback_data="1201-3200")], ]
            # context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons),
            #                          text="Please choose the LOT Size")
            # buttons = [[InlineKeyboardButton("Neti", callback_data="209056"),
            #             InlineKeyboardButton("Yuliawati", callback_data="136618")],
            #            [InlineKeyboardButton("Tri Purwanti", callback_data="171564"),
            #             InlineKeyboardButton("Muhammad Said", callback_data="410426")],
            #            [InlineKeyboardButton("Parman", callback_data="308071"),
            #             InlineKeyboardButton("Vivi", callback_data="313687")],
            #            [InlineKeyboardButton("Sutiah", callback_data="504246"),
            #             InlineKeyboardButton("Misran", callback_data="207184")],
            #            [InlineKeyboardButton("Slamet", callback_data="206180"),
            #             InlineKeyboardButton("Wiwi", callback_data="703179")],
            #            [InlineKeyboardButton("Rosmawati", callback_data="143801"),
            #             InlineKeyboardButton("Aan", callback_data="363898")],
            #            [InlineKeyboardButton("Muladsih", callback_data="128885"),
            #             InlineKeyboardButton("Dede Trimono", callback_data="353601")],
            #            [InlineKeyboardButton("Ira", callback_data="116002"),
            #             InlineKeyboardButton("Tri Widyaningsih", callback_data="186102")],
            #            [InlineKeyboardButton("Kosim", callback_data="409004"),
            #             InlineKeyboardButton("Rina Sugiarti", callback_data="903332")],
            #            [InlineKeyboardButton("Ali Wahyudi", callback_data="407097"),
            #             InlineKeyboardButton("Venny Anjarwati", callback_data="377498")],
            #            [InlineKeyboardButton("Wahyuni", callback_data="104852"),
            #             InlineKeyboardButton("Mulyani", callback_data="307021")],
            #            [InlineKeyboardButton("Lukik Dwi", callback_data="427464"),
            #             InlineKeyboardButton("Intan", callback_data="903127")],
            #            [InlineKeyboardButton("Umi", callback_data="183488")], ]
            # context.bot.send_message(chat_id=update.effective_chat.id, reply_markup=InlineKeyboardMarkup(buttons),
            #                          text="Please select the Lineleader")
            # context.bot.send_message(chat_id=update.effective_chat.id, parse_mode = 'Markdown', text="Type */exit* if you want to exit the Key In!")


def queryHandler(update: Update, context: CallbackContext):
    query = update.callback_query.data
    update.callback_query.answer()

    update.callback_query.message.edit_reply_markup(
        reply_markup=InlineKeyboardMarkup([])
    )

    if 'LBO' == query:
        LBOPATROL[f"{update.effective_user.username}"] = query
        print(LBOPATROL)
        update.callback_query.message.edit_text(text=f"LBO/PATROL: {query}")
    elif 'Patrol' == query:
        LBOPATROL[f"{update.effective_user.username}"] = query
        print(LBOPATROL)
        update.callback_query.message.edit_text(text=f"LBO/PATROL: {query}")
    if "1" == query:
        LotNum[f"{update.effective_user.username}"] = query
        print(LotNum)
        update.callback_query.message.edit_text(text=f"LOT#: {query}")
    elif "2" == query:
        LotNum[f"{update.effective_user.username}"] = query
        print(LotNum)
        update.callback_query.message.edit_text(text=f"LOT#: {query}")
    elif "3" == query:
        LotNum[f"{update.effective_user.username}"] = query
        print(LotNum)
        update.callback_query.message.edit_text(text=f"LOT#: {query}")
    elif "4" == query:
        LotNum[f"{update.effective_user.username}"] = query
        print(LotNum)
        update.callback_query.message.edit_text(text=f"LOT#: {query}")

    if "13" == query:
        SampleSize[f"{update.effective_user.username}"] = query
        print(SampleSize)
        update.callback_query.message.edit_text(text=f"Sample Size: {query}")
    elif "20" == query:
        SampleSize[f"{update.effective_user.username}"] = query
        print(SampleSize)
        update.callback_query.message.edit_text(text=f"Sample Size: {query}")
    elif "32" == query:
        SampleSize[f"{update.effective_user.username}"] = query
        print(SampleSize)
        update.callback_query.message.edit_text(text=f"Sample Size: {query}")
    elif '50' == query:
        SampleSize[f"{update.effective_user.username}"] = query
        print(SampleSize)
        update.callback_query.message.edit_text(text=f"Sample Size: {query}")
    elif "80" == query:
        SampleSize[f"{update.effective_user.username}"] = query
        print(SampleSize)
        update.callback_query.message.edit_text(text=f"Sample Size: {query}")
    if "51-90" == query:
        LotSize[f"{update.effective_user.username}"] = query
        print(LotSize)
        update.callback_query.message.edit_text(text=f"Lot Size: {query}")
    elif "91-150" == query:
        LotSize[f"{update.effective_user.username}"] = query
        print(LotSize)
        update.callback_query.message.edit_text(text=f"Lot Size: {query}")
    elif "151-280" == query:
        LotSize[f"{update.effective_user.username}"] = query
        print(LotSize)
        update.callback_query.message.edit_text(text=f"Lot Size: {query}")
    elif "280-500" == query:
        LotSize[f"{update.effective_user.username}"] = query
        print(LotSize)
        update.callback_query.message.edit_text(text=f"Lot Size: {query}")
    elif "281-500" == query:
        LotSize[f"{update.effective_user.username}"] = query
        print(LotSize)
        update.callback_query.message.edit_text(text=f"Lot Size: {query}")
    elif "501-1200" == query:
        LotSize[f"{update.effective_user.username}"] = query
        print(LotSize)
        update.callback_query.message.edit_text(text=f"Lot Size: {query}")
    elif "601-1200" == query:
        LotSize[f"{update.effective_user.username}"] = query
        print(LotSize)
        update.callback_query.message.edit_text(text=f"Lot Size: {query}")
    elif "1201-3200" == query:
        LotSize[f"{update.effective_user.username}"] = query
        print(LotSize)
        update.callback_query.message.edit_text(text=f"Lot Size: {query}")
    if "209056" == query:
        LineLead[f"{update.effective_user.username}"] = query
        print(LineLead)
        update.callback_query.message.edit_text(text="Line Leader: Neti Fitriana")
        context.bot.send_message(parse_mode='Markdown', chat_id=update.effective_chat.id,
                                 text="Please type the *Machine Number*")

    elif "136618" == query:
        LineLead[f"{update.effective_user.username}"] = query
        print(LineLead)
        update.callback_query.message.edit_text(text="Line Leader: Yuliawati")
        context.bot.send_message(parse_mode='Markdown', chat_id=update.effective_chat.id,
                                 text="Please type the *Machine Number*")

    elif "171564" == query:
        LineLead[f"{update.effective_user.username}"] = query
        print(LineLead)
        update.callback_query.message.edit_text(text="Line Leader: Tri Purwanti")
        context.bot.send_message(parse_mode='Markdown', chat_id=update.effective_chat.id,
                                 text="Please type the *Machine Number*")

    elif "410426" == query:
        LineLead[f"{update.effective_user.username}"] = query
        print(LineLead)
        update.callback_query.message.edit_text(text="Line Leader: Muhammad Said")
        context.bot.send_message(parse_mode='Markdown', chat_id=update.effective_chat.id,
                                 text="Please type the *Machine Number*")

    elif "308071" == query:
        LineLead[f"{update.effective_user.username}"] = query
        print(LineLead)
        update.callback_query.message.edit_text(text="Line Leader: Parman Kurniawan")
        context.bot.send_message(parse_mode='Markdown', chat_id=update.effective_chat.id,
                                 text="Please type the *Machine Number*")

    elif "313687" == query:
        LineLead[f"{update.effective_user.username}"] = query
        print(LineLead)
        update.callback_query.message.edit_text(text="Line Leader: Vivi Oktavia")
        context.bot.send_message(parse_mode='Markdown', chat_id=update.effective_chat.id,
                                 text="Please type the *Machine Number*")

    elif "504246" == query:
        LineLead[f"{update.effective_user.username}"] = query
        print(LineLead)
        update.callback_query.message.edit_text(text="Line Leader: Sutiah")
        context.bot.send_message(parse_mode='Markdown', chat_id=update.effective_chat.id,
                                 text="Please type the *Machine Number*")

    elif "207184" == query:
        LineLead[f"{update.effective_user.username}"] = query
        print(LineLead)
        update.callback_query.message.edit_text(text="Line Leader: Misran Fildianto")
        context.bot.send_message(parse_mode='Markdown', chat_id=update.effective_chat.id,
                                 text="Please type the *Machine Number*")

    elif "206180" == query:
        LineLead[f"{update.effective_user.username}"] = query
        print(LineLead)
        update.callback_query.message.edit_text(text="Line Leader: Slamet Tursadi")
        context.bot.send_message(parse_mode='Markdown', chat_id=update.effective_chat.id,
                                 text="Please type the *Machine Number*")

    elif "703179" == query:
        LineLead[f"{update.effective_user.username}"] = query
        print(LineLead)
        update.callback_query.message.edit_text(text="Line Leader: Wiwi Mulyanti")
        context.bot.send_message(parse_mode='Markdown', chat_id=update.effective_chat.id,
                                 text="Please type the *Machine Number*")

    elif "143801" == query:
        LineLead[f"{update.effective_user.username}"] = query
        print(LineLead)
        update.callback_query.message.edit_text(text="Line Leader: Rosmawati")
        context.bot.send_message(parse_mode='Markdown', chat_id=update.effective_chat.id,
                                 text="Please type the *Machine Number*")

    elif "363898" == query:
        LineLead[f"{update.effective_user.username}"] = query
        print(LineLead)
        update.callback_query.message.edit_text(text="Line Leader: Aan Darwati")
        context.bot.send_message(parse_mode='Markdown', chat_id=update.effective_chat.id,
                                 text="Please type the *Machine Number*")

    elif "128885" == query:
        LineLead[f"{update.effective_user.username}"] = query
        print(LineLead)
        update.callback_query.message.edit_text(text="Line Leader: Muladsih Sri Untari")
        context.bot.send_message(parse_mode='Markdown', chat_id=update.effective_chat.id,
                                 text="Please type the *Machine Number*")

    elif "353601" == query:
        LineLead[f"{update.effective_user.username}"] = query
        print(LineLead)
        update.callback_query.message.edit_text(text="Line Leader: Dede Trimono")
        context.bot.send_message(parse_mode='Markdown', chat_id=update.effective_chat.id,
                                 text="Please type the *Machine Number*")

    elif "116002" == query:
        LineLead[f"{update.effective_user.username}"] = query
        print(LineLead)
        update.callback_query.message.edit_text(text="Line Leader: Ira Daniyati")
        context.bot.send_message(parse_mode='Markdown', chat_id=update.effective_chat.id,
                                 text="Please type the *Machine Number*")

    elif "186102" == query:
        LineLead[f"{update.effective_user.username}"] = query
        print(LineLead)
        update.callback_query.message.edit_text(text="Line Leader: Tri Widyaningsih")
        context.bot.send_message(parse_mode='Markdown', chat_id=update.effective_chat.id,
                                 text="Please type the *Machine Number*")

    elif "409004" == query:
        LineLead[f"{update.effective_user.username}"] = query
        print(LineLead)
        update.callback_query.message.edit_text(text="Line Leader: Kosim")
        context.bot.send_message(parse_mode='Markdown', chat_id=update.effective_chat.id,
                                 text="Please type the *Machine Number*")

    elif "903332" == query:
        LineLead[f"{update.effective_user.username}"] = query
        print(LineLead)
        update.callback_query.message.edit_text(text="Line Leader: Rina Sugiarti")
        context.bot.send_message(parse_mode='Markdown', chat_id=update.effective_chat.id,
                                 text="Please type the *Machine Number*")

    elif "407097" == query:
        LineLead[f"{update.effective_user.username}"] = query
        print(LineLead)
        update.callback_query.message.edit_text(text="Line Leader: Muhammad Ali Wahyudi")
        context.bot.send_message(parse_mode='Markdown', chat_id=update.effective_chat.id,
                                 text="Please type the *Machine Number*")

    elif "377498" == query:
        LineLead[f"{update.effective_user.username}"] = query
        print(LineLead)
        update.callback_query.message.edit_text(text="Line Leader: Venny Anjarwati")
        context.bot.send_message(parse_mode='Markdown', chat_id=update.effective_chat.id,
                                 text="Please type the *Machine Number*")

    elif "104852" == query:
        LineLead[f"{update.effective_user.username}"] = query
        print(LineLead)
        update.callback_query.message.edit_text(text="Line Leader: Wahyuni")
        context.bot.send_message(parse_mode='Markdown', chat_id=update.effective_chat.id,
                                 text="Please type the *Machine Number*")

    elif "307021" == query:
        LineLead[f"{update.effective_user.username}"] = query
        print(LineLead)
        update.callback_query.message.edit_text(text="Line Leader: Mulyani")
        context.bot.send_message(parse_mode='Markdown', chat_id=update.effective_chat.id,
                                 text="Please type the *Machine Number*")

    elif "427464" == query:
        LineLead[f"{update.effective_user.username}"] = query
        print(LineLead)
        update.callback_query.message.edit_text(text="Line Leader: Lukik Dwi Rita")
        context.bot.send_message(parse_mode='Markdown', chat_id=update.effective_chat.id,
                                 text="Please type the *Machine Number*")

    elif "903127" == query:
        LineLead[f"{update.effective_user.username}"] = query
        print(LineLead)
        update.callback_query.message.edit_text(text="Line Leader: Intan Juariah")
        context.bot.send_message(parse_mode='Markdown', chat_id=update.effective_chat.id,
                                 text="Please type the *Machine Number*")
    elif "183488" == query:
        LineLead[f"{update.effective_user.username}"] = query
        print(LineLead)
        update.callback_query.message.edit_text(text="Line Leader: Umi Kasanah")
        context.bot.send_message(parse_mode='Markdown', chat_id=update.effective_chat.id,
                                 text="Please type the *Machine Number*")



def main():
    updater = Updater(token='5021063058:AAEwnq5_dPaGrLMbEvfuNG5DcfENscnHgMk', use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('GRN', GRN))
    dp.add_handler(MessageHandler(Filters.photo, photo))
    dp.add_handler(MessageHandler(Filters.document.jpg, file))
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('input', input))
    dp.add_handler(CallbackQueryHandler(queryHandler))
    dp.add_handler(CommandHandler('exit', Exit))
    # dp.add_handler(CommandHandler('machine', machine))
    # dp.add_handler(CommandHandler('mjr', major))
    # dp.add_handler(CommandHandler('ra', readuit))
    # dp.add_handler(CommandHandler('kpk', KPKOp))
    # dp.add_handler(CommandHandler('rm', remarks))
    # dp.add_handler(CommandHandler('dc', defectCode))
    dp.add_handler(MessageHandler(Filters.command, command_handler))
    dp.add_handler(MessageHandler(Filters.text, messageHandler))
    dp.add_handler(MessageHandler(Filters.text, message))
    updater.start_polling()
    updater.idle()
if __name__ == "__main__":
    main()