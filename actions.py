from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class PresentMenu(Action):
    def name(self) -> Text:
        return "action_present_menu"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        restaurant = "BINGO"  # Name of the restaurant

        # Define static menu data with images for BINGO
        menu_items = [
            {
                "name": "Pizza",
                "category": "Plat",
                "sizes": [
                    {"size": "petit", "price": "4000 CFA"},
                    {"size": "moyen", "price": "5000 CFA"},
                    {"size": "grand", "price": "6000 CFA"},
                ],
                "image": "https://img.freepik.com/free-photo/chicken-pizza-with-bell-peppers-tomato-cheese-round-wooden-board_140725-10493.jpg?t=st=1727876306~exp=1727879906~hmac=839ef618399a142b83fe3df1356fb0021f93fd48a8f149d02623c7d1836c2af5",
                "vegetarian": True
            },
            {
                "name": "Boisson Sucre",
                "category": "Boisson",
                "sizes": [
                    {"size": "verre", "price": "500 CFA"},
                ],
                "image": "https://img.freepik.com/free-photo/front-view-tasty-meat-burger-with-cheese-salad-dark-background_140725-89597.jpg?t=st=1727876306~exp=1727879906~hmac=12bdf320e4763b9ca6f103f69e336a83f923b41021792cb2f8fff150d4430165",
                "vegetarian": True
            },
            {
                "name": "Boisson Alcool",
                "category": "Boisson",
                "sizes": [
                    {"size": "verre", "price": "1000 CFA"},
                ],
                "image": "https://img.freepik.com/free-photo/mixed-pizza-with-sliced-lemon_140725-2808.jpg?t=st=1727876306~exp=1727879906~hmac=5b9bd6d17395c1330c2d1cb9ff410b2163ae3117980286f920c8206b62134d9b",
                "vegetarian": True
            }
        ]

        elements = []
        for item in menu_items:
            # Create buttons for different sizes and prices
            buttons = [
                {
                    "title": f"{size['size'].capitalize()} - {size['price']}",
                    "payload": f"/choose_{item['category'].lower()}{{\"item_name\": \"{item['name']}\", \"price\": \"{size['price']}\", \"size\": \"{size['size']}\"}}"
                }
                for size in item["sizes"]
            ]

            elements.append({
                "title": item['name'],
                "subtitle": f"Catégorie: {item['category']}",
                "image_url": item['image'],  # Add the image URL for visual display
                "buttons": buttons
            })

        # Show menu as a carousel with images, sizes, and prices
        dispatcher.utter_message(
            text=f"Voici le menu de {restaurant}, comprenant les pizzas et les boissons. Choisissez une option ci-dessous.",
            attachment={
                "type": "carousel",
                "elements": elements
            }
        )

        return []

class ChooseItem(Action):
    def name(self) -> Text:
        return "action_choose_item"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        item_name = tracker.get_slot("item_name")
        item_category = tracker.get_slot("item_category")
        item_size = tracker.get_slot("size")
        item_price = tracker.get_slot("price")

        # Respond based on the category of the item chosen
        if item_category.lower() == "boisson":
            dispatcher.utter_message(text=f"Vous avez choisi la {item_name} ({item_size}) pour {item_price}. Souhaitez-vous ajouter cette boisson à votre commande ?")
        else:
            dispatcher.utter_message(text=f"Vous avez choisi une {item_name} de taille {item_size} pour {item_price}. Souhaitez-vous ajouter cette option à votre commande ?")

        return []
