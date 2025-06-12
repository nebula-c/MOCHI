

class EventBus:
    SET_BUTTON_CLICKED = "set_button_clicked"
    EXPORT_BUTTON_CLICKED = "export_button_clicked"
    ASK_CALCULATION = "ask_calculation"
    RUN_CALCULATION = "run_calculation"
    END_CALCULATION = "end_calculation"
    PROGRESS_UPDATE = "progress_update"

    def __init__(self):
        self.listeners = {}

    def subscribe(self, event_name, fn):
        self.listeners.setdefault(event_name, []).append(fn)

    def emit(self, event_name, *args):
        for fn in self.listeners.get(event_name, []):
            fn(*args)



EventBus = EventBus()
