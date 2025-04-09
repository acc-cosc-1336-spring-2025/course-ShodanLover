def add_inventory(widgets, widget_name, quantity):
    """
    Adds a widget to the inventory dictionary or updates its quantity if it exists.

    Args:
        widgets (dict): The inventory dictionary.
        widget_name (str): The name of the widget to add or update.
        quantity (int): The quantity of the widget to add or update.
    """
    if widget_name in widgets:
        widgets[widget_name] = widgets[widget_name] + quantity
    else:
        widgets[widget_name] = quantity

def remove_inventory_widget(widgets, widget_name):
    """
    Removes a widget from the inventory dictionary if it exists.

    Args:
        widgets (dict): The inventory dictionary.
        widget_name (str): The name of the widget to remove.

    Returns:
        str: 'Record deleted' if the widget was removed, 'Item not found' otherwise.
    """
    if widget_name in widgets:
        del widgets[widget_name]
        return 'Record deleted'
    else:
        return 'Item not found'