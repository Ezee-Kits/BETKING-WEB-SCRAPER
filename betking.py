from func import scrolling,requesting_init,saving_files,drop_duplicate,main_date,simple_scroll,headless_selenium_init,saving_path_csv
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time



def betking_func():
    path = f'{saving_path_csv}/BETKING.csv'
    driver,wait,EC,By = headless_selenium_init()
    driver.get('https://m.betking.com/sports/football/todaysMatches?ic_source=internal&ic_medium=quicklinks&ic_campaign=todaysevents')

    wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/app-root/app-wrapper/div/sports-home-page/div/div/sports-todays-events-wrapper/div/sports-prematch-container/div/div/div/div[1]/sports-prematch-single-line/div/div/div/div/div[2]/div[2]/app-odd-group/div[2]/app-odd/span')))

    simple_scroll(driver=driver,speed=1000,t_runs = 17)


    matches = wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/app-root/app-wrapper/div/sports-home-page/div/div/sports-todays-events-wrapper/div/sports-prematch-container/div/div/div')))
    matches = matches.text.replace('\n','!').split('!')
    print(matches)


    int_vals = [str(x) for x in range(1,3)]
    int_exp = ['X','Today','bar_chart','Tomorrow','...']
    int_vals = int_vals + int_exp

    new_matches = []
    for x in matches:
        x = x.strip()
        if x in int_vals or '+' in x or '-' in x:
            pass
        else:
            new_matches.append(x)

    time_value = []
    time_index = []

    for i,x in enumerate(new_matches):
        if ':' in x:
            indx = new_matches.index(x,i,len(new_matches))
            time_index.append(indx)
            time_value.append(x)

    # print(new_matches)
    # print(time_index)
    # print(time_value)

    for x in time_index:
        try:
            f_elem_indx = time_index.index(x)
            s_elem_indx = time_index.index(x) + 1

            if (time_index[s_elem_indx] - time_index[f_elem_indx]) == 6:
                all_info = new_matches[ time_index[f_elem_indx]:time_index[s_elem_indx] ]
                match_time = all_info[0]

                home_team = all_info[1]
                away_team = all_info[2]

                home_odd = float(all_info[3])
                draw_odd = float(all_info[4])
                away_odd = float(all_info[5])
                bookmaker = 'BETKING'

                data = {
                    'TIME':match_time,
                    'HOME TEAM':home_team,
                    'AWAY TEAM':away_team,

                    'HOME ODD': home_odd,
                    'DRAW ODD':draw_odd,
                    'AWAY ODD':away_odd,
                    'BOOKMAKER':bookmaker
                }
                saving_files(data=[data],path=path)
        except:
            pass

    drop_duplicate(path=path)
