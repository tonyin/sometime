import datetime
import parsedatetime.parsedatetime as pdt

crontable = []
outputs = []

def process_message(data):
    if data['channel'] == 'C04EW02AQ' and data['text'].startswith('<@U0K8SU35K>'):
        msg = data['text'][data['text'].find(' ')+1:]
        dt = get_datetime(msg)
        if dt is None:
            outputs.append([data['channel'], 'Speaka-English please. I couldn\'t understand the proposed time'])
        else:
            outputs.append([data['channel'], 'YO! :thumbsup: this msg if you\'d like to:\n\"' + msg + '\"\n(Or ' + str(dt) + ')'])

def get_datetime(s):
    c = pdt.Calendar()
    result,what = c.parse(s)
    dt = None

    # 0 = failed to parse
    # 1,2,3 = date, time, datetime
    if what in (1,2,3):
        dt = datetime.datetime(*result[:6]) # *result[:6] gets the y/m/d/h/m/s in tuple form
    if dt is None:
        print 'Really a date time string?: ' + s

    return dt
