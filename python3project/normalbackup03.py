#!/usr/bin/python3

import time
import random

usa = {

            'Alaska Standard Time' : 
                            ['Alaska'],

            'Hawaii Standard Time' : 
                            ['Hawaii'],

            'Pacific Standard Time' : 
                            ['Washington',
                             'Oragan',
          		     'Nevada',
          		     'California',
              		     'Idaho'],

            'Arizona Mountain Standard Time' : 
                            ['Arizona'],

            'Mountain Standard Time' :  
                            ['Montana',
			     'Idaho',
			     'Wyoming',
			     'Utah',
			     'Colorado',
			     'Arizona',
			     'New Mexico',
			     'Texas',
			     'North Dakota',
			     'South Dakota',
			     'Nebraska',
			     'Kansas'],

            'Central Standard Time' :  
                            ['North Dakota',
			     'South Dakota',
			     'Nebraska',
			     'Kansas',
			     'Oklahoma',
			     'Texas',
			     'Minnesota',
			     'Iowa',
		             'Missouri',
			     'Arkansas',
			     'Louisiana',
			     'Michigan',
			     'Wisconsin',
			     'Illinois',
			     'Indiana',
			     'Kentucky',
			     'Tennessee',
			     'Mississippi',
			     'Alabama',
			     'Florida'],

            'Eastern Standard Time' : 
                            ['Michigan',
			     'Indiana',
			     'Kentucky',
			     'Tennessee',
			     'Georgia',
			     'Florida',
			     'Ohio',
			     'West Virginia',
			     'Virginia',
			     'North Carolina',
			     'South Carolina',
			     'Pennsylvania',
			     'Maryland',
			     'Delaware',
			     'New Jersey',
			     'New York',
			     'Connecticut',
			     'Rhode Island',
			     'Massachusetts',
			     'Vermont',
			     'New Hampshire',
			     'Maine',
			     'District of Columbia']
            
         }

zone= random.choice(list(usa))
state= random.choice(list(usa['Eastern Standard Time']))
def normal():
    print(zone)
    print(state)
    #print(random.choice(list(usa.keys())))
    #print(random.choice(list(usa.items())))
    #print(random.choice(list(usa)))
    #for x in usa:
    #    print(x)
                                                  
def main():
    normal()

if __name__ == "__main__":
    main()
