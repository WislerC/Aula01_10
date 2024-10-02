*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    https://www.amazon.com.br
${BROWSER}    chrome
${PRODUTO}    smartphone

*** Keywords ***
Pesquisar Produto
    [Arguments]    ${produto}
    Open Browser    ${URL}    ${BROWSER}
    Input Text    id=twotabsearchtextbox    ${produto}
    Click Button    id=nav-search-submit-button

Verificar Resultados
    [Arguments]    ${produto}
    Page Should Contain    ${produto}
    Element Should Be Visible    css=.s-main-slot

*** Test Cases ***
Teste Pesquisa Produto
    Pesquisar Produto    ${PRODUTO}
    Verificar Resultados    ${PRODUTO}
    Close Browser
