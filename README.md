# Vivaleak - By dTwoZ3r0
Vivaldi has a bug that keeps persistent personal info in sqlite tables even after clearing browser history.


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


Securing personal data has become a huge problem. Storing a persons first and last name, email address, and phone numbers in a non prived db for anyone to grab is
dangerous. Especcially with all the spy code being released. (cough* cough*...NSA) Just imagine a bad guy that knows exaclty where to look and creates an exploit to
grab this data because they know vivaldi doesn't properly clear your data when you ask it too.

I contemplated releasing the malware to drive this point home. I don't want fingers pointed at me, so i'm not releasing that.

### This affects all versions of Vivaldi Web Browser < 1.14 on Linux Systems. 
I did not verify windows and OSX versions. Someone else can verify the bug on those 2x operating systems and reach out to me if they wish.



##Usage:

./vivaleak.py

You should see the data pulled from phone,email, and name tables that can't be deleted.
