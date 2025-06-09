

class EventBus:
    SET_BUTTON_CLICKED = "set_button_clicked"
    EXPORT_BUTTON_CLICKED = "export_button_clicked"

    def __init__(self):
        self.listeners = {}

    # def subscribe(self, func):
    #     self.subscribers.append(func)

    # def emit(self, *args, **kwargs):
    #     for func in self.subscribers:
    #         func(*args, **kwargs)


    def subscribe(self, event_name, fn):
        self.listeners.setdefault(event_name, []).append(fn)

    def emit(self, event_name, *args):
        for fn in self.listeners.get(event_name, []):
            fn(*args)



EventBus = EventBus()
