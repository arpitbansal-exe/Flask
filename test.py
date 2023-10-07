from bs4 import BeautifulSoup 
import requests 
from flask import Flask, jsonify, make_response 
def get_profile_detail(email_list):
    all_details = []
    for email in email_list:
        user_handle = email.split('@')[0] 
    
        url = 'https://auth.geeksforgeeks.org/user/{}/profile'.format(user_handle) 
        print(url)
        response = requests.get(url) 
    
        soup = BeautifulSoup(response.content, 'html5lib') 
        description_div = soup.find('div', {'class': 'profile_details_section activity-container-1 section_card'}) 

        if not description_div: 
            # all_details.append({'user profile': "Not found", 'streak': None, 'institute rank': None})
            user_profile = "Not found"
            print('User not found')
        else:   
            name_block = description_div.find('div', {'class': 'profile_name'})
            user_profile = name_block.text.strip() 

            streak_block = description_div.find('div', {'class': 'streakCnt tooltipped'})
            if not streak_block:
                streak = None
            else:    
                    streak=streak_block.text.strip().split(' ')[0]

            rank_block = description_div.find('span', {'class': 'rankNum'})
            if not rank_block:
                institute_rank = "Not avaliable"
            else:

                institute_rank=rank_block.text.strip()
            all_details.append({'user_profile': user_profile, 'streak': streak, 'institute_rank': institute_rank})
    return all_details    
