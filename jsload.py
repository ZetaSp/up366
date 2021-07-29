import json

ifDebug = True

ifGapped = False
def debug(info='', depth=0):
    global ifDebug
    global ifGapped
    if ifDebug == True:
        if info != '':
            print('[de] ' + '    '*depth + str(info))
            ifGapped = False
        else:
            if ifGapped == False:
                print('')
                ifGapped = True

with open('page1.js', 'r', encoding='utf-8') as file:
    pageConfig = file.read()
pageConfig = pageConfig.split('var pageConfig=')[1]

Page = json.loads(pageConfig)
debug('Page loaded.')
debug()

for a, Slide in enumerate(Page['slides']):
    debug('Slide ' + str(a) + ' type ' + str(Slide['displayType']), 1)

    if Slide['displayType'] == '':
        debug('x', 2)

    else:
        for b,Question in enumerate(Slide['questionList']):
            debug('Question ' + str(b)  + ' type ' + str(Question['question_type']) + ' score ' + str(Question['question_score']), 2)

            debug('Media _', 3)
            debug('File [' + str(Question['media']['file']) + '] => [media/dittol.mp3]', 4)
            Question['media']['file'] = 'media/dittol.mp3'
            for c,Media in enumerate(Question['medias']):
                debug('Media ' + str(c), 3)
                debug('File [' + str(Media['file']) + '] => [media/dittol.mp3]', 4)
                Media['file'] = 'media/dittol.mp3'
            for c,Record in enumerate(Question['record_follow_read']['mode_list']):
                debug('Record ' + str(c), 3)
                debug('File [' + str(Record['media_file']) + '] => [media/dittol.mp3]', 4)
                Record['media_file'] = 'media/dittol.mp3'
                for d,Sentence in enumerate(Record['sentences']):
                    debug('Sentence [' + Sentence['startTime'] + ' - ' + Sentence['endTime'] + '] => [0]', 4)
                    Sentence['startTime'] = '0:00.000'
                    Sentence['endTime'] = '0:00.000'
            debug()

            if Question['question_type'] == 1:
                Answer = Question['answer_text']
                debug('Ans [' + Answer + '] => [ANSWER]', 3)
                for Option in Question['options']:
                    debug('Option [' + str(Option['id']) + '] ' + Option['content'], 3)
                    if Option['id'] == Answer:
                        Option['content'] = '-->ANSWER<--'
                    else:
                        Option['content'] = 'x'

            elif Question['question_type'] == 99:
                for c,Questioo in enumerate(Question['questions_list']):
                    debug('Questioo ' + str(c)  + ' type ' + str(Questioo['question_type']) + ' score ' + str(Questioo['question_score']), 3)

                    Answer = Questioo['answer_text']
                    debug('Ans [' + Answer + '] => [ANSWER]', 4)
                    for Option in Questioo['options']:
                        debug('Option [' + str(Option['id']) + '] ' + Option['content'], 4)
                        if Option['id'] == Answer:
                            Option['content'] = '-->ANSWER<--'
                        else:
                            Option['content'] = 'x'
                    debug()

            else:
                debug('UNKNOWN question_type ' + str(Question['question_type']), 2)
            debug()
    debug()

pageConfig = 'var pageConfig=' + json.dumps(Page, ensure_ascii=False)
with open('page1.js', 'w', encoding='utf-8') as file:
    file.write(pageConfig)
debug('Page saved.')