# NEP-Group Framework Approach and Guidance
Automation framework developed using Behavior-driven development(or BDD), Selenium Webdriver, and Python scripts. For all Selenium stuff, see https://www.selenium.dev/ as well as the python selenium module https://selenium-python.readthedocs.io

Test Structure:
The tests are written in Gherkin syntax, using Behave as a testrunner, with the actions/locations coded in an Object Orientated manner following the Page-Object approach. Can run the behave from the command line/Terminal – refer to the Behave docs on https://behave.readthedocs.io/en/latest/behave.html#command-line-arguments

Features:
BDD is a cycle of interactions with well-defined outputs resulting in tested software. The tests are written using Gerkin syntax (“Given, When, Then”) and divided into “Features” which are contained in their own folder. The tests themselves are documented as “Scenarios” in the .feature file in each of these folders. Behave (the python port of jbehave) is used to run the tests, and this maps the Steps listed in the Scenarios in each .feature file to functions defined in the .py file in the ./steps folder of the Feature

Steps:
Steps correlate directly to the steps in the scenarios in the feature – the step name identified using decorators which match from the feature file: given, when and then. The decorator accepts a string containing the rest of the phrase used in the scenario step it belongs to e.g.

Feature: Authentication 

Scenario: Verify user authentication

    Given user navigates to login page
    
    When user enters valid "User Name" and "Password"
    
    And user clicks on Login button
    
    Then user successfully login

Feature keyword - describes which part of the functionality scenarios are being created for
Scenario keyword - is used to describe the test case title
Given keyword - describes pre-conditions required to complete the scenario
When keyword - is used to describe the scenario's steps
Then keyword - describes the expected result of the scenario
And keyword - can be used for Given, When and Then keywords to describe additional steps

Step code implementation looks like...
@given(u'user navigates DemoQA website')

def step_impl(context):
context.browser.get('https://demoqa.com/')

"Page" Library Files

Steps import classes from one (or more) page libraries (in addition to the generic class in “Base_Page_Object.py” and use their methods to run the test (e.g. using selenium to drive the webpages). The methods contained in these pages describe the actions needed for the test steps to run and should be named so they are understandable as to their action. The methods do not describe how to find objects on the pages – these definitions are held in the locator library files

"Locator" Library Files

Locators describe, in a tuple, how to find objects on the pages. These are made up of a method of finding the object (e.g. by ID, by CSS class, by XPATH, by LINK TEXT/PARTIAL LINK TEXT), and then the data used to find it (e.g. the id, class name, XPath expression, etc.).

These should be unique on the page, and immutable in the application. If they are changed by a code change in the platform code, this should be the only place it needs to be changed with the result cascading back through all the page methods it is referenced in.

Wait Commands

There are instances where time.sleep() is used to delay the script, this is due to selenium getting “ahead” of a javascript function but the test will run quickly enough that it will try and interact with objects on the page that exist in the DOM, but are not fully visible/editable until the javascript action completes.
Certainly, better ways of handling this – explicit waits are probably the wait to approach this, and lots of resources available on this online (e.g. by using WebDriverWait in conjunction with the ExpectedConditions class to force the selenium driven browser to wait in a loop for a condition to be true/false – e.g. visible, editable, selectable, presence, etc

Error Handling

There are cases where error handling could be made more informative, A common failure mode would be where a find_element call fails and throws an “element not found” exception. Added user-friendly string assertions so it’s often reasonably easy to trace the failing step and the locator it is referring to.

Modules installed using pip:

selenium

behave

nose.tools

time

signal

and any other dependencies via pip

Guidelines to run tests locally:

Navigate to the features folder in the cmd prompt or terminal i.e. cd <localpath>\demoqa\tests\features

Run single scenario: behave authentication.feature -n 'Verify user authentication'

Run single feature file: behave authentication.feature
