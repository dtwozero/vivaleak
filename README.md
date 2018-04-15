# vivaleak
Vivaldi has a bug that keeps persistent personal info in sqlite tables even after clearing browser history.

# These are the tables inside the Web Data database:

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

Even after a user clears their browsers history and checked all boxes and chooses from all time from the drop down menu, there are 3x tables that cannot be erased.

autofill_profile_emails
autofill_profile_names
autofill_profile_phones

# This affects all versions of Vivaldi Web Browser < 1.14 on Linux Systems. 
I cannot verify on windows because i hate windows and don't feel like installing a vm. However i think it's safe to assume this is affected OSX as well. Someone can
verify.


