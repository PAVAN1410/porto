# usser data

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
# end user data #############################

