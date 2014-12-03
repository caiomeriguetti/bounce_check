#coding=utf-8
import email

def check(s):
    b = email.message_from_string(s)
    return scan_mail(b,b)

def scan_mail(b,original):
    
    soft=['5.2.0','5.2.1','5.2.2','5.3.1','5.4.5','5.5.3']
    
    returndata={'isbounce':False,'status':''}
    
    if b.is_multipart():
        
        for payload in b.get_payload():
            
            resp =scan_mail(payload,original)
            
            if resp['isbounce'] == True: returndata['isbounce']=True
            if resp['status']: returndata['status']=resp['status']
    else:
        
        if 'Status' in b.keys() and b['Status']:
            returndata['status']=b['Status']
        
            if not( str(b['Status']).strip() in soft ) :
                returndata['isbounce']=True
    
    return returndata