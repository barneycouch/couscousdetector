from food_search import pretty_food_report
from send_email import send_email_to_list
from get_menu import formatted_menu_today

send_email_to_list(pretty_food_report("Cous Cous") + formatted_menu_today())