# User ID recommendation and Feature Implementation (kakao open recruitment)

# String manipulation
def solution(new_id):
    # little trick
    filtered_id = ['.']
    # allowed: alpha-numeric, '-', '_', '.'
    
    for ch in new_id:
        if len(filtered_id) == 16:
            break
            
        if ch.isalnum() or ch == '-' or ch == '_':
            # valid character: alpha-numeric, '-', '_'
            filtered_id.append(ch.lower())

        if ch == '.' and filtered_id[-1] != '.':
						# valid character "."
            fitlered_id.append(ch)
                
    if len(filtered_id) > 1 and filtered_id[-1] == '.':
        filtered_id.pop()
    
    if len(filtered_id) == 1:
        filtered_id.append('a')
    
    while len(filtered_id) < 4:
        filtered_id.append(filtered_id[-1])
    
    result = ''.join(filtered_id[1:16]) if len(filtered_id) >= 16 else ''.join(filtered_id[1:])
    
    return result