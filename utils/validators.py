VALID_STATUS=['Sent','Completed']
VALID_SENT_THROUGH=['WhatsApp','Email','Drive Link','Physical Copy']

def validate_record(data):
    required=['file_name','sector','area','handover_to','role_team','date_sent','sent_through','status']
    for field in required:
        if not data.get(field):
            return False,f'{field} is required'
    if data['status'] not in VALID_STATUS:
        return False,'Invalid Status'
    if data['sent_through'] not in VALID_SENT_THROUGH:
        return False,'Invalid Sent Through Value'
    return True,''
