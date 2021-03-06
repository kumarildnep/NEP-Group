import time

from behave import *
from lib.locators.l_search import SearchLocators as SL
from lib.pages.p_search import Search


# Scenario: Book Search

@When(u'user navigates to book search page')
def step_impl(context):
    context.execute_steps(u'when user enters valid "{}" and "{}"'.format('User Name', 'Password'))
    context.execute_steps(u'when user clicks on Login button')
    time.sleep(1)


@When(u'user clicks on goto book store button')
def step_impl(context):
    ob_SL = Search(context.browser)
    ob_SL.press_enterkey_at_element(SL.gotoBookStoreButton)


@When(u'user types the "{searchKey}" in search input')
def step_impl(context, searchKey):
    ob_SL = Search(context.browser)
    ob_SL.set_element_value(SL.searchBookInput, ob_SL.property(searchKey))
    ob_SL.press_enterkey_at_element(SL.searchBookInput)


@Then(u'books related "{searchKey}" are displayed')
def step_impl(context, searchKey):
    ob_SL = Search(context.browser)
    bookDesc = ob_SL.get_element_text(SL.searchBookLink)
    if ob_SL.property(searchKey) in bookDesc:
        pass
    else:
        raise AssertionError("Wrong search")


# Scenario: Verify search book details

@When(u'user clicks on the link prompted')
def step_impl(context):
    ob_SL = Search(context.browser)
    ob_SL.press_enterkey_at_element(SL.searchBookLink)
    time.sleep(1)


@Then(u'details of the book are displayed')
def step_impl(context):
    ob_SL = Search(context.browser)
    ob_SL.check_element(SL.bookISBN)
