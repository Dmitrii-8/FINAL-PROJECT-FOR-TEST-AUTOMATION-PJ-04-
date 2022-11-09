## Description of files  📝
* *autotests_rostelecom.py contains web interface tests for Rostelecom*  

* *conftest.py stores all the necessary code to detect failed test cases and take a screenshot if any test fails*   

* *requirements.txt short list of requirements* 
### In the page folder:     
   * *auth_page.py authorization page for working with autotests*    
   * *base.py contains a Python implementation of the PageObject template*     
   * *pages/elements.py contains a helper class for defining web elements in web pages*      
   * *registration_page.py is the registration page for working with autotests*     
------
## Description of autotests :memo:
### Test-Case №1  
**test_start_page_is_correct**  
***Correct display of the authorization page***    
### Test case №2  
**test_the_presence_of_buttons_and_elements_on_the_page**  
***Checking the presence and correct display of buttons and elements on the page***  
### Test-Case №3 (FB-01)  
**test_location_of_page_blocks**  
***Checking for the presence of elements, both in the left and right blocks of the page***   
### Test-Case №4 (FB-02)  
**test_registration_page_and_continue_button**  
***Checking the correct operation of the "Continue" button in the registration form***   
### Test-Case №5  
**test_registration_with_an_incorrect_value_in_the_name_field**   
***Negative test. Incorrect entry of a value in the field "Name" more than two characters during user registration  
Subsequent appearance of the error hint text***    
### Test-Case №6 (FB-03)  
**test_phone_tab**  
***Selection tab name test "Number"***  
### Test-Case №7  
**test_registration_with_an_incorrect_value_in_the_last_name_field**  
***Negative test. Incorrect entry of a value in the "Last name" field of more than thirty characters, when registering a user   
Subsequent appearance of the error hint text***   
### Test-Case №8  
**test_registration_page_with_empty_name_field**   
***Checking for user registration with an empty "name" field followed by the error tooltip text***   
### Test-Case №9  
**test_registration_of_an_already_registered_user**  
***Negative test. User registration using a registered number
Display an alert about this***   
### Test-Case N-10  
**test_authorisation_valid**  
***Testing Registered User Authentication***   
### Test-Case №11   
**testing**  
***Checking the presence and clickability of the "Support", "Write", "X" buttons, as well as closing the opened form***   
### Test-Case №12 (FB-04)  
**test_notification_form**  
***Detailed test of window close button - "X"***
### Test-Case №13  
**test_authorization_of_a_user_with_an_invalid_password**  
***Registered user login with wrong password in "Authorization" form
"Forgot password" changes color to orange***   
### Test-Case №14   
**test_instead_of_cyrillic_invalid_characters**
***When registering a new user, in the "Last name" input field, invalid characters instead of Cyrillic ("Registration" form)***   
### Test-Case №15  
**test_invalid_email_or_mobile_phone**  
***Email in the input field is invalid (Email or mobile phone)***  
### Test-Case №16  
**test_incorrect_password_during_registration**  
***When registering a new user, the password is less than eight characters,
Subsequent appearance of error tooltip text***  
### Test-Caseс №17  
**test_password_and_password_confirmation_do_not_match**   
***The input fields "Password" and "Password Confirmation" do not match in the "Registration" form***   
:heavy_check_mark:

