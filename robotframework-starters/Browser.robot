*** Settings ***
Library           Browser

*** Variables ***
${URL}       http://selenium.thinkcode.se/
${BROWSER}     chromium
${HEADLESS}     headless:false

*** Test Cases ***

Find Hello World
    Open Browser    ${URL}      ${BROWSER}         ${HEADLESS}
    Click           \#helloWorld
    Get Text        \#headline  equal  Hello, world!
    [Teardown]      Close Browser