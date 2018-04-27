# Vivaleak - By dTwoZ3r0
Vivaldi has a bug that keeps persistent personal info in sqlite tables even after clearing browser history.

### This affects all versions of Vivaldi Web Browser < 1.15 on Linux Systems. 
I did not verify windows and OSX versions. Someone else can verify the bug on those 2x operating systems and reach out to me if they wish.

Contact me on Twitter: @dTwoZ3r0
## These are the tables inside the Web Data database:

autofill                   masked_credit_cards      
autofill_model_type_state  meta                     
autofill_profile_emails    payment_method_manifest  
autofill_profile_names     server_address_metadata  
autofill_profile_phones    server_addresses         
autofill_profiles          server_card_metadata     
autofill_profiles_trash    token_service            
autofill_sync_metadata     unmasked_credit_cards    
credit_cards               web_app_manifest_section 
keywords

Once a user clears their browsers history and checked all boxes and chooses to delete (all time) data  from the drop down menu, there are 3x tables that cannot be erased.

autofill_profile_emails
autofill_profile_names
autofill_profile_phones

## Usage:

./vivaleak.py

You should see the data pulled from phone,email, and name tables that can't be deleted.


# Other Areas of Concern

### Directory
/home/username/.config/vivaldi/Default/Storage/ext/mpognobbkildjkofajifpdfhcoklimli/def


### Database File
Cookies 
-->This database stores cookies for every site visited and cannot be deleted unless you manually open the sqlite database and remove the items inside.

### Directory
/home/username/.config/vivaldi/Default/Storage/ext/mpognobbkildjkofajifpdfhcoklimli/def/Cache

This directory holds a huge list of data files that store information on every website visited since the browser has been installed and first used. This data also cannot be deleted
unless you manually go into the directory and remvoe the files.

## Easy Example: 

hexdump -C datafilename new_text_data_filename.txt

## Conclusion
Securing personal data has become a huge problem. Storing a persons first and last name, email address, and phone numbers in a non prived db for anyone to grab is
dangerous. Especcially with all the spy code being released. (cough* cough*...NSA) Just imagine a bad guy that knows exaclty where to look and creates an exploit to
grab this data because they know vivaldi doesn't properly clear your data when you ask it too.





