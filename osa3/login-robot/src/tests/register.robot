*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  jaakko  kalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  sa  kalle123
    Output Should Contain  Username must be at least 4 characters long

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  kalle1  kalle123
    Output Should Contain  Username must contain only letters

Register With Valid Username And Too Short Password
    Input Credentials  kalevi  kal12
    Output Should Contain  Password must be at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  risto  qwertyuiop
    Output Should Contain  Password must not contain only letters

*** Keywords ***
Input New Command And Create User Command
    Input New Command
    Create User  kalle  kalle123
	