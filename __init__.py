from aqt import gui_hooks, mw
from aqt.utils import showInfo
from anki import db


IMPORTANT_DECK_PATH = "ENG::Vocab"

# https://www.reddit.com/r/Anki/comments/3b1uf7/is_it_possible_to_edit_historical_data_for_a_deck/
def my_func(*args):
    # db.execute("SELECT name FROM sqlite_master WHERE type='table';")
    # mw.col.db.execute("SELECT name FROM sqlite_master WHERE type='table';")
    showInfo(str(mw.col.db.all("SELECT name FROM sqlite_master WHERE type='table';")))
    showInfo(str(mw.col.db.all("SELECT * FROM decks")))
    # deck = deck.decks.children(deck.decks.id(path))


gui_hooks.overview_did_refresh.append(my_func)
# gui_hooks.reviewer_did_answer_card.append(my_func)
# gui_hooks.reviewer_did_show_answer.append(my_func)
