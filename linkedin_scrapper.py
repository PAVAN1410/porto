import os,random, sys, time,json,re
from urllib.parse import urlparse
from selenium import webdriver
from bs4 import BeautifulSoup




def scrapper(link):
    browser=webdriver.Chrome('driver/chromedriver.exe')

    browser.get('https://www.linkedin.com/uas/login')

    file = open('config.txt')
    lines=file.readlines()
    username=lines[0]
    password=lines[1]
    username

    username_id=browser.find_element_by_id('username')
    username_id.send_keys(username)

    password_id=browser.find_element_by_id('password')
    password_id.send_keys(password)

    username_id.submit()

    # visitingProfileId='https://www.linkedin.com/in/rohit-volety-745253135/'
    # visitingProfileId='https://www.linkedin.com/in/pranavm-9487/'
    # visitingProfileId='https://www.linkedin.com/in/krishna-pavan-ayitha/'
    # visitingProfileId='https://www.linkedin.com/in/amaan-iqbal/'
    # visitingProfileId=
    # visitingProfileId=
    # visitingProfileId=
    # visitingProfileId='https://www.linkedin.com/in/rohit-volety-745253135/'
    visitingProfileId=link


    browser.get(visitingProfileId)

    #pause before scrolling
    SCROLL_PAUSE_TIME = 6

    #Get the scroll height of the page
    last_height = browser.execute_script("return document.body.scrollHeight")

    #scroll the entire page due to dynamic loading of the webpage we need to load the entire webpage by scrolling
    for i in range(3):
        # Scroll down to bottom
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight/3);")
        time.sleep(SCROLL_PAUSE_TIME/2)
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight*(2/3));")
        time.sleep(SCROLL_PAUSE_TIME/2)
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = browser.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height



    try:    
        xy=browser.find_element_by_css_selector("section[id='experience-section'] button[class='pv-profile-section__see-more-inline pv-profile-section__text-truncate-toggle artdeco-button artdeco-button--tertiary artdeco-button--muted']")
        browser.execute_script("arguments[0].click();",xy)
    #     src=browser.page_source
    #     soup = BeautifulSoup(src,'lxml')
        # print(soup)

    except Exception as e:
        # print(e)
        pass


    try:    
        xy=browser.find_element_by_css_selector("section[id='certifications-section'] button[class='pv-profile-section__see-more-inline pv-profile-section__text-truncate-toggle artdeco-button artdeco-button--tertiary artdeco-button--muted']")
        browser.execute_script("arguments[0].click();",xy)
        browser.execute_script("arguments[0].click();",xy)

    except Exception as e:
        # print(e)
        pass
    # finally:
    #     src=browser.page_source
    #     soup = BeautifulSoup(src,'lxml')
    #     print(soup)
        

    try:    
        xy=browser.find_element_by_css_selector("button[class='pv-profile-section__card-action-bar pv-skills-section__additional-skills artdeco-container-card-action-bar artdeco-button artdeco-button--tertiary artdeco-button--3 artdeco-button--fluid artdeco-button--muted']")
        browser.execute_script("arguments[0].click();",xy)

    except Exception as e:
        # print(e)
        pass
    # finally:
    #     src=browser.page_source
    #     soup = BeautifulSoup(src,'lxml')
    #     print(soup)


    src=browser.page_source
    soup = BeautifulSoup(src,'lxml')

    name_div = soup.find('div',{'class':'display-flex justify-space-between pt2'})
    user_data={}
    name_loc = name_div.find('div').find_all('div')
    user_data['name']=name_loc[0].get_text().strip()
    user_data['address']=name_loc[2].get_text().strip().split('\n')[0]
    user_data['profile_title']=name_loc[1].get_text().strip().split(',')
    x=[]
    for i in range(len(user_data['profile_title'])):
        x.append(user_data['profile_title'][i].split('||'))
    x=sum(x,[])
    user_data['profile_title']=x
    try:
    # 
        img=soup.find('img',{'class':'presence-entity__image EntityPhoto-circle-1 lazy-image ember-view'})
        user_data['image_src']=img['src']
    except Exception as e:
        # print(e)
        pass

    # 
    user_data
# 

    # img=soup.find('img',{'class':'ember-view pv-profile-sticky-header__image'})
    # user_data={}
    # name_loc = name_div.find_all('li')

    # print(name_loc)
    # user_data['name']=name_loc[0].get_text().strip()
    # address=name_div.find('li',{'class':'t-16 t-black t-normal inline-block'})
    # user_data['address']=address.get_text().strip()
    # conn=name_div.find('span',{'class':'t-16 t-black t-normal'})
    # user_data['linked_in_connections']=conn.get_text().strip()
    # user_data['profile_title']=name_div.find('h2').get_text().strip().split(',')
    # user_data['image_scr']=img['src']
    # user_data
# 
    # print(name_div)
    # img=soup.find('img',{'class':'ember-view pv-profile-sticky-header__image'})

    # user_data={}
    # name_loc = name_div.find_all('li')

    # # print(name_loc)
    # user_data['name']=name_loc[0].get_text().strip()
    # user_data['address']=name_loc[1].get_text().strip()
    # user_data['linked_in_connections']=name_loc[2].get_text().strip()
    # user_data['profile_title']=name_div.find('h2').get_text().strip().split(',')
    # user_data['image_scr']=img['src']
    # user_data

    # Experience




    try:
        exp_section = soup.find('section',{'id','experience-section'})
        # print(exp_section) 
    except Exception as e:
        # print(e)
        pass
    # print(exp_section.exp_section.find_all('li',{'class':'pv-entity__position-group-pager pv-profile-section__list-item ember-view'}))
    exp_section_fields=[]
    try:
        exp_section_fields= exp_section.find_all('li',{'class':'pv-entity__position-group-pager pv-profile-section__list-item ember-view'})
    #     exp_section_fields[0]
    except Exception as e:
        # print(e)
        pass
    # print(exp_section_fields)

    Experience=[]
    company={}
    for i in range(len(exp_section_fields)):
        # print(i)
        company={}
        
        try:
            company['img']=exp_section_fields[i].find('img')['src']
        except Exception as e:
            pass
    
        # 
        try:
            company['post']=exp_section_fields[i].find('h3').get_text().strip().split('\n')[0]
            if company['post']=='Company Name':
                company['post']=exp_section_fields[i].find('h3').get_text().strip().split('\n')[1]
        # 
        # try:
        #     company['post']=exp_section_fields[i].find('h3').get_text().strip().split('\n')[0]
        except Exception as e:
            pass
        try:    
            company['name']=exp_section_fields[i].find('p',{'class','pv-entity__secondary-title t-14 t-black t-normal'}).get_text().strip()
            company['name']=company['name'].split('\n')[0]
        except Exception as e:
            pass
        try:
            company['work_duration']=exp_section_fields[i].find('h4',{'class','pv-entity__date-range t-14 t-black--light t-normal'}).get_text().strip()
            company['work_duration']=company['work_duration'].split('\n')[1]
        except Exception as e:
            pass
        Experience.append(company)
    Experience

    # Education


    education=soup.find('section',{'id','education-section'})
    # education

    Education={}
    Education['college']=education.find('h3').get_text().strip()
    Education['degree']=education.find('p',{'class','pv-entity__secondary-title pv-entity__degree-name t-14 t-black t-normal'}).get_text().strip()
    Education['degree']=Education['degree'].split('\n')[1]
    Education['field_of_study']=education.find('p',{'class','pv-entity__secondary-title pv-entity__fos t-14 t-black t-normal'}).get_text().strip()
    Education['field_of_study']=Education['field_of_study'].split('\n')[1]


    Education


    # Licenses and certifications



    certifications_section = soup.find('section', {'id': 'certifications-section'})
    certifications_section

    certifications_section_fields=[]
    try:
        certifications_section_fields= certifications_section.find_all('li')
    # certifications_section_fields[0]
    except Exception as e:
            pass

    Certifications=[]
    for i in range(len(certifications_section_fields)):
        certificate={}    
        certificate['name']=certifications_section_fields[i].find('h3').get_text().strip()
        certificate['issued_by']=certifications_section_fields[i].find('p',{'class':'t-14'}).get_text().strip().split('\n')[-1].strip()
        Certifications.append(certificate)
    Certifications

    # skills and endorsements

# 
    skills_section = soup.find('section', {'class': 'pv-profile-section pv-skill-categories-section artdeco-card mt4 p5 ember-view'})

    try:
        skills_set=[]
        skills_li=skills_section.find_all('span',{'class':'pv-skill-category-entity__name-text t-16 t-black t-bold'})
        for i in range(len(skills_li)):
                skills_set.append(skills_li[i].get_text().strip())

    except Exception as e:
            pass

# 


    accomplishments = soup.find('section',{'class':'pv-profile-section pv-accomplishments-section artdeco-card mv4 ember-view'})

    # accomplishments

    # projects_section= accomplishments.find('div',{'class':'pv-accomplishments-block__list-container','aria-labelledby'="projects-title"}).find('ul').find_all('li')
    projects=[]
    try:
        projects_section= accomplishments.find('div',{'class':'pv-accomplishments-block__list-container','aria-labelledby':"projects-title"}).find('ul').find_all('li')

        projects_section

        projects=[]
        for i in range(len(projects_section)):
            projects.append(projects_section[i].get_text().strip())
    except Exception as e:
        projects=[]
        pass

    projects

    honors=[]
    try:
        honors_section= accomplishments.find('div',{'class':'pv-accomplishments-block__list-container','aria-labelledby':"honors-title"}).find('ul').find_all('li')
        honors_section
        honors=[]
        for i in range(len(honors_section)):
            honors.append(honors_section[i].get_text().strip())
    except Exception as e:
        honors=[]
        pass

    honors

    languages=[]
    try:
        languages_section= accomplishments.find('div',{'class':'pv-accomplishments-block__list-container','aria-labelledby':"languages-title"}).find('ul').find_all('li')
        languages=[]
        for i in range(len(languages_section)):
            languages.append(languages_section[i].get_text().strip())
    except Exception as e:
        languages=[]
        pass

    languages

    organizations=[]
    try:
        organizations_section= accomplishments.find('div',{'class':'pv-accomplishments-block__list-container','aria-labelledby':"organizations-title"}).find('ul').find_all('li')
        organizations=[]
        for i in range(len(organizations_section)):
            organizations.append(organizations_section[i].get_text().strip())
    except Exception as e:
        organizations=[]
        pass
    organizations

    publications=[]
    try:
        publication_section = accomplishments.find('div',{'class':'pv-accomplishments-block__list-container','aria-labelledby':"publications-title"}).find('ul').find_all('li')
        publications=[]
        for i in range(len(publication_section)):
            publications.append(publication_section[i].get_text().strip())
    except Exception as e:
        publications=[]
        pass

    # publications

    # print(user_data)
    # print('\n')
    # print(Experience)
    # print('\n')
    # print(Education)
    # print('\n')
    # print(Certifications)
    # print('\n')
    # print(skills_set)
    # print('\n')
    # print(projects)
    # print('\n')
    # print(honors)
    # print('\n')
    # print(languages)
    # print('\n')
    # print(organizations)
    # print('\n')
    # print(publications)

    user_profile={'user_data':user_data,'Experience':Experience,'Education':Education,'Certifications':Certifications,'skills_set':skills_set,'projects':projects,'honors':honors,'languages':languages,'organizations':organizations,'publications':publications}

    user_profile_json=json.dumps(user_profile,indent=4)

    print(user_profile_json)
    fileheader = open("static/test.json", 'w')

    fileheader.writelines(user_profile_json)


    fileheader = open("output/test.json", 'w')

    fileheader.writelines(user_profile_json)

    # browser.close()