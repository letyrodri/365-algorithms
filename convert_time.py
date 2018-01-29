def convert_time(stime):
    '''
    Description: Convert from 12-hour clock  to 24-hour clock 
    
    Input: stime time string in format hh:mm:ss[AM/PM] 12-hour-clock  

    Return: time string in format 24-hour clock
    
    Complexity: O(1)
                
    '''
    am_pm = stime[-2:]
    hour = int(stime[0:2])

    # 12:00 AM 0:00    
    if hour == 12:
        hour = 0

    if (am_pm == 'PM'):
        hour = hour+12
        
        
    return str(hour).zfill(2)+stime[2:len(stime)-2]



